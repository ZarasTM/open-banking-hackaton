from flask import make_response
from flask_login import login_required, current_user
from db import queries

# @login_required
def getTransactionsSummary():
    try:
        transactions_as_buyer, transactions_as_seller = queries.getTransactionsSummary(current_user.get_id())
        # res = {'as_seller': [{'title': 'Pizza payment', 'other_party': 'Muzyczna', 'amount': 35.00, 'currency': 'PLN', 'date': '23.04.2019'}],
        #         'as_buyer': [{{'title': 'Weekly tomatoes', 'other_party': 'Pomidorex Sp. z o.o.', 'amount': 200.00, 'currency': 'PLN', 'date': '22.04.2019'}}]}
        seller, buyer = serializeTransactions(transactions_as_buyer, transactions_as_seller)
        res = {'as_seller': seller, 'as_buyer': buyer}
        return make_response(res, 200)
    except:
        return make_response('', 401)

def serializeTransactions(buyertr, sellertr):
    b = []
    for i in buyertr:
        b.append(serializeBuyerTransaction(i))
    s = []
    for i in sellertr:
        s.append(serializeSellerTransaction(i))
    return s,b

def serializeSellerTransaction(transaction):
    return {
        "transaction_id" : transaction.tid,
        "title": transaction.name,
        "amount": transaction.amount,
        "other_party": queries.getUserInvoiceConfigByUid(transaction.buyer).name,
        "currency" : transaction.currency,
        "date" : transaction.timestamp
    }

def serializeBuyerTransaction(transaction):
    return {
        "transaction_id" : transaction.tid,
        "title": transaction.name,
        "amount": transaction.amount,
        "other_party": queries.getUserInvoiceConfigByUid(transaction.seller).name,
        "currency" : transaction.currency,
        "date" : transaction.timestamp
    }
