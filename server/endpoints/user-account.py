from flask import make_response
from flask_login import login_required, current_user
from db import queries

# @login_required
def fetchUserData():
    user = queries.getUserByID(current_user.get_id())
    if user != None:
        balances = queries.fetchUserBalance(user.uid)
        balances = [{'balance_user': serializeUserInvoice(queries.getUserInvoiceConfigByUid(x.buyer)), 'amount': x.amount, 'currency': x.currency}
                     for x in balances]
        print(vars(queries.getUserInvoiceConfigByUid(user.uid)))
        res = {'user_inv_data' : serializeUserInvoice(queries.getUserInvoiceConfigByUid(user.uid)), 'balances': balances}
        return make_response(res, 200)
    return make_response('', 401)

# @login_required
def getUserInvoiceConfig(body):
    tin = body.get('tin')
    if tin:
        res = queries.getUserInvoiceConfigByTin(tin)
        return make_response(res, 200)
    return make_response('', 401)

def serializeUserInvoice(userInvoice):
    return {
        "uid": userInvoice.uid,
        "name": userInvoice.name,
        "address": userInvoice.address,
        "account_number": userInvoice.account_number,
        "tin": userInvoice.tin
    }