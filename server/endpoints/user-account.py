from flask import make_response
from flask_login import login_required, current_user
from db import queries

# @login_required
def fetchUserData():
    user = queries.getUserByID(current_user.get_id())
    if user != None:
        balances = queries.fetchUserBalance(user.uid)
        balances = [{'balance_user': queries.getUserInvoiceConfigByUid(x.buyer), 'amount': x.amount, 'currency': x.currency}
                     for x in balances]

        res = {'user_inv_data' : queries.getUserInvoiceConfigByUid(user.uid), 'balances': balances}
        return make_response(res, 200)
    return make_response('', 401)

# @login_required
def getUserInvoiceConfig(body):
    tin = body.get('tin')
    if tin:
        res = queries.getUserInvoiceConfigByTin(tin)
        return make_response(res, 200)
    return make_response('', 401)
    