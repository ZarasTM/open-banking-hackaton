from config import db
from db.models import *
import sqlalchemy


def getUIDByEmail(email):
    # try:
    usr = UserLogin.query.filter(UserLogin.email == email).one_or_none()
    return usr.uid
    # except AttributeError:
    #     print(f'[ERROR] User not found: {email}')
    # except sqlalchemy.orm.exc.MultipleResultsFound:        
    #     print(f'[ERROR] Multiple records found for user: {email}')
    # finally:
    #     return usr.uid    

def getLogin(email):
    """
    Main login functionality - checks if an email exists in the db
    """
    return UserLogin.query.filter(UserLogin.email == email).one_or_none()

def getUserSettings(email):
    uid = getUIDByEmail(email)
    config = UserConfig.query.filter(UserConfig.uid == uid).one_or_none()
    if config:
        return {
            'default_currency' : config.default_currency, 
            'timezone' : config.timezone,
            'api_key' : config.api_key,
            'status' : config.status
        }
    else:
        print(f'[ERROR] Config not found for: {email}')
        return {
            'default_currency' : 'PLN', 
            'timezone' : 'UTC',
            'api_key' : '',
            'status' : ''
        }




        # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_working_with_joins.htm
# # TEMP
# q = (Session.query(User,Document,DocumentPermissions)
#     .filter(User.email == Document.author)
#     .filter(Document.name == DocumentPermissions.document)
#     .filter(User.email == 'someemail')
#     .all())

################################################################################# NEW CONCEPT

def emailRegistered(email):
    """
    :input: email address
    :returns: boolean | is there an user already registered with this email 
    """
    return True if UserLogin.query.filter(UserLogin.email == email).one_or_none() else False


def register(email, hashed, name, address, account_number, tin, totp_secret, api_key="Yachniaccio"): # TODO - Implement any other data necessary for company registration # TODO: do
    """
    :input: email, hashed password, name (company), address (string), account number / IBAN (string),
    tin (taxpayer Id number) (string), api_key (#TODO or toremove)
    :returns: boolean | did the registration succeed
    """
    try:
        new_user = UserLogin(uid=None, password=hashed, email=email, totp_secret=totp_secret)
        db.session.add(new_user)
        db.session.add(UserConfig(uid=new_user.uid, default_currency='PLN', timezone='UTC', api_key=api_key, status=0))
        db.session.add(UserInvoice(uid=new_user.uid, name=name, address=address, account_number=account_number, tin=tin))
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def getUserByEmail(email):
    """
    :input: email
    :returns: user | object with provided email (None if it doesn't exist)
    """
    return UserLogin.query.filter(UserLogin.email == email).one_or_none()

def getUserByID(id):
    """
    :input: uid
    :returns: user | object with provided email (None if it doesn't exist)
    """
    return UserLogin.query.get(int(id))

def getInvoicesSummary(id):
    """
    :input: uid
    :returns: tuple | list of user invoices as a buyer, list of user invoices as a seller
    """
    sellerInvoices = Invoice.query.filter(Invoice.seller==id).all()
    buyerInvoices = Invoice.query.filter(Invoice.buyer==id).all()
    return (buyerInvoices, sellerInvoices)

def getInvoice(id, inv_no):
    """
    :input: uid, invoice number
    :returns: invoice | object for given uid and invoice number OR None
    """
    return Invoice.query.filter(Invoice.iid == inv_no).filter(Invoice.seller == id, Invoice.buyer == id).one_or_none()

def getUserInvoiceConfigByTin(tin):
    """
    in : tin
    out : UserInvoice object
    """
    return UserInvoice.query.filter(UserInvoice.tin == tin).one_or_none()

def getUserInvoiceConfigByUid(uid):
    """
    in : uid
    out : UserInvoice object
    """
    return UserInvoice.query.filter(UserInvoice.uid == uid).one_or_none()

def calculateSubtotal(items):
    #items == [item, item]
    #item =={ iid name quantity unit tax_rate net_ppu}	
    sum = 0.0
    for item in items: 
        item_price = item['net_ppu']
        item_tax_rate = item['tax_rate']
        item_tax = item_tax_rate * item_price
        item_total = item_price + item_tax
        sum += round(item_total * item['quantity'], 2)
    return sum

def addNewInvoice(seller, buyer, name, items, currency='PLN'):
    subtotal = calculateSubtotal(items)
    try:
        new_invoice = Invoice(iid=None, seller=seller, buyer=buyer,
        name=name, items=str(items), amount=subtotal, currency=currency)
        db.session.add(new_invoice)
        updateBalances(new_invoice)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def getMatchingInvoice(seller, buyer, name, amount):
    numbers = [int(s) for s in str.split() if s.isdigit()]
    #FOUND IID (likely)
    if numbers:
        number = numbers[0]
        #TODO: improve
        return Invoice.query.filter(Invoice.seller == seller and
        Invoice.buyer == buyer and Invoice.iid == number).one_or_none()
    else:
        return None

def addNewTransaction(seller, buyer, amount, name, currency='PLN'):
    invoice = getMatchingInvoice(seller, buyer, name, amount)
    try:
        new_transaction = Transaction(tid=None, seller=seller, buyer=buyer,
        name=name, amount=amount, currency=currency, invoice=invoice)
        db.session.add(new_transaction)
        if invoice:
            invoice.amount_paid = invoice.amount_paid + amount
        updateBalances(new_transaction)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def getTransactionsSummary(id):
    """
    :input: uid
    :returns: tuple | list of user Transactions as a buyer, list of user Transactions as a seller
    """
    sellerTransactions = Transaction.query.filter(Transaction.seller==id).all()
    buyerTransactions = Transaction.query.filter(Transaction.buyer==id).all()
    return (buyerTransactions, sellerTransactions)

def getHangingTransactions(seller):
    return Transaction.query.filter(Transaction.invoice == None).all()

def assignInvoiceToTransaction(tid, iid):
    transaction = Transaction.query.filter(Transaction.tid == tid).one_or_none()
    invoice = Invoice.query.filter(Invoice.iid == iid).one_or_none()
    if transaction and invoice:
        if not transaction.invoice:
            if transaction.seller == invoice.seller and transaction.buyer == invoice.buyer:
                try:
                    transaction.invoice = invoice.id
                    invoice.amount_paid = invoice.amount_paid + transaction.amount
                    db.session.commit()
                    return True
                except:
                    db.session.rollback()
                    return False
            else:
                print(f'AUUUU TRANSACTION {tid} AND INVOICE {iid} HAVE DIFFERENT USERS')
        else:
            print(f'AUUUUU TRANSACTION {tid} ALREADY GOT AN INVOICE')
    else:
        print(f'AUUUUUU TRANSACTION {tid} OR INVOICE {iid} WAS NOT FOUND!!!!')

def updateBalances(interaction):
    seller = interaction.seller
    buyer = interaction.buyer
    amount = interaction.amount
    currency = interaction.currency
    balance_record1 = Balance.query.filter(Balance.seller == seller and Balance.buyer == buyer).one_or_none()
    balance_record2 = Balance.query.filter(Balance.seller == buyer and Balance.buyer == seller).one_or_none()
    #Try/except/commit/rollback in the calling functions
    if balance_record1 and balance_record2:
        #update them 1 - seller is seller, transfer amount, 2 - amount * -1
        balance_record1.amount = balance_record1.amount + amount
        balance_record2.amount = balance_record2.amount + amount * -1
    else:
        #add 
        new_balance1 = Balance(seller=seller, buyer=buyer,
        amount=amount, currency=currency)
        db.session.add(new_balance1)
        new_balance2 =  Balance(seller=buyer, buyer=seller,
        amount=amount, currency=currency)
        db.session.add(new_balance2)

    def fetchUserBalance(uid):
        return Balance.query.filter(Balance.seller == uid).all()

