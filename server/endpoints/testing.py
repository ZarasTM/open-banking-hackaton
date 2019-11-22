from flask import make_response
from flask_login import login_required, login_user, current_user, logout_user
from db import queries


def test():
    v = queries.register('somemail', 'secretpass', 'company', 'street', 'PL1234', '2137', )
    user = queries.getUserByID(1)
    print(user.email)
    user2 = queries.getUserByEmail('somemail')
    print(user.password)
    # # TODO - Implement mocked function
    # # TODO - Determine necessary data
    # if user != None:
    #     res = {'username': user.username,'total_balance': 20.05, 'friend_balances': [{'friend': 'Mati', 'amount': 20.05, 'currency': 'PLN'}], 'user_config': {'default_currency': 'PLN', 'timezone': 'UTF-8', 'simplify_debts': False}}
    #     return make_response(res, 200)
    return make_response('', 401)