from flask import make_response
from flask_login import login_required, current_user
from db import queries

@login_required
def fetchUserData():
    user = queries.getUserByID(current_user.get_id())
    # TODO - Implement mocked function
    # TODO - Determine necessary data
    if user != None:
        res = {'username': user.username,'total_balance': 20.05, 'friend_balances': [{'friend': 'Mati', 'amount': 20.05, 'currency': 'PLN'}], 'user_config': {'default_currency': 'PLN', 'timezone': 'UTF-8', 'simplify_debts': False}}
        return make_response(res, 200)
    return make_response('', 401)

#@login_required
def getUserInvoiceConfig(body):
    # user = queries.getUserByID(current_user.get_id())
    tin = body.get('tin')
    # TODO - Implement mocked function
    # TODO - Determine necessary data
    # TODO Check if tin is not none
    res = queries.getUserInvoiceConfig(tin)
    res = {'name' : res.name, 'address': res.address, 'account_number' : res.account_number, 'tin': tin}
    make_response(res, 200)