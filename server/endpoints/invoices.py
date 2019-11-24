from flask import make_response
from flask_login import login_required, current_user
import ast
from db import queries

# @login_required
def getInvoicesSummary():
    try:
        invoices_as_buyer, invoices_as_seller = queries.getInvoicesSummary(current_user.get_id())
        seller, buyer = serializeInvoices(invoices_as_buyer, invoices_as_seller)
        # res = {'as_seller': [{'title': 'Pizza payment', 'other_party': 'Muzyczna', 'amount': 35.00, 'currency': 'PLN', 'date': '23.04.2019'}],
        #         'as_buyer': [{{'title': 'Weekly tomatoes', 'other_party': 'Pomidorex Sp. z o.o.', 'amount': 200.00, 'currency': 'PLN', 'date': '22.04.2019'}}]}
        # sellerList = []
        res = {'as_seller': seller, 'as_buyer': buyer}
        return make_response(res, 200)
    except:
        return make_response('', 401)

@login_required
def getInvoice(body):
    inv_no = body.get('invoice_id')
    # try:
    res = queries.getInvoice(current_user.get_id(), inv_no)
    if res:
        # b, s = serializeInvoices(queries.getUserresConfigByUid(res.buyer), queries.getUserresConfigByUid(res.seller))
        res = {'invoice_id' : res.iid,
            'seller': serializeUserInvoiceData(queries.getUserInvoiceConfigByUid(res.seller)),
            'buyer': serializeUserInvoiceData(queries.getUserInvoiceConfigByUid(res.buyer)),
            'timestamp': res.timestamp,
            'amount': res.amount,
            'currency': res.currency,
            'title': res.name,
            'items': ast.literal_eval(res.items),
            'amount_paid': res.amount_paid,
            'payable': res.payable}
        return make_response(res, 200)
    return make_response('', 401)
    # except:
    #     return make_response('', 401)

# @login_required
def createInvoice(body):
    currency = body.get('currency') or 'PLN'
    seller_uid = queries.getUIDByTin(body.get('seller_nip'))
    buyer_uid = queries.getUIDByTin(body.get('buyer_nip'))
    queries.addNewInvoice(seller_uid, buyer_uid, body.get('title'), body.get('items'), currency)
    return make_response('', 200)

def serializeInvoices(buyerinv, sellerinv):
    b = []
    for i in buyerinv:
        b.append(serializeBuyerInvoice(i))
    s = []
    for i in sellerinv:
        s.append(serializeSellerInvoice(i))
    return s,b

def serializeSellerInvoice(invoice):
    return {
        "invoice_id" : invoice.iid,
        "title": invoice.name,
        "amount": invoice.amount,
        "other_party": queries.getUserInvoiceConfigByUid(invoice.buyer).name,
        "currency" : invoice.currency,
        "date" : invoice.timestamp
    }


def serializeBuyerInvoice(invoice):
    return {
        "invoice_id" : invoice.iid,
        "title": invoice.name,
        "amount": invoice.amount,
        "other_party": queries.getUserInvoiceConfigByUid(invoice.seller).name,
        "currency" : invoice.currency,
        "date" : invoice.timestamp
    }

def serializeUserInvoiceData(userInvoice):
    return {
        "uid": userInvoice.uid,
        "name": userInvoice.name,
        "address": userInvoice.address,
        "account_number": userInvoice.account_number,
        "tin": userInvoice.tin
    }