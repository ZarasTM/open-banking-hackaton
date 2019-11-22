from config import db
from db.models import *
import sqlalchemy


def getUIDByEmail(email):
    try:
        usr = db.session.query(UserLogin).filter(UserLogin.email == email).one_or_none()
        return usr.uid
    except AttributeError:
        print(f'[ERROR] User not found: {email}')
    except sqlalchemy.orm.exc.MultipleResultsFound:        
        print(f'[ERROR] Multiple records found for user: {email}')
    finally:
        return None   

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


#TODO: rework? or remove
def fetchUserState(data):
    #return DICT {total_balance: $bal, friend_balances: [{friend: ID, amount: $$, currency: CBN}, ...], groups: [{}], user_config: {opt1: val, opt2:val}}
    username = data.get('username')

    config = getUserSettings(username)
    #return {
    # 'total_balance': ,
    # 'friend_balances': , 
    # 'groups': groups,
    # 'user_config': config
    # }


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


def register(email, hashed, name, address, account_number, tin, api_key="Yachniaccio"): # TODO - Implement any other data necessary for company registration # TODO: do
    """
    :input: email, hashed password, name (company), address (string), account number / IBAN (string),
    tin (taxpayer Id number) (string), api_key (#TODO or toremove)
    :returns: boolean | did the registration succeed
    """
    try:
        new_user = UserLogin(uid=None, password=hashed, email=email)
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

def getUserByTIN(tin):
    return UserInvoice.query.filter(UserInvoice.tin == tin).one_or_none()

def getUserInvoiceConfig(tin):
    """
    in : tin
    out : UserInvoice object
    """
    user = getUserByTIN(tin)
    if user:
        uid = user.uid
        return UserInvoice.query.filter(UserInvoice.uid == uid).one_or_none()
    else:
        return None
#!!!!!!!!!!!!!!!!!!!!!!!! old ideas
#TODO invoice too
def addNewTransaction(seller, buyer, amount, currency='PLN'):
    pass

def getTransactionHistory(username):
    pass

def updateBalances():
    #search invoices, and transactions after timestamp, get + and - for each user

    pass