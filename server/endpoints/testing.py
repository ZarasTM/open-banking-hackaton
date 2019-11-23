from flask import make_response
from flask_login import login_required, login_user, current_user, logout_user
from db import queries


def test():
    # registerUsers()

    # print(queries.getUIDByEmail('email4'))
    # print(vars(queries.getLogin('email4')))
    # print(vars(queries.getUserByID(20)))
    # print(queries.getUserByID(20) == queries.getUserByID('20'))


    # print(queries.getUserSettings('email10'))

    #     return make_response(res, 200)
    return make_response('', 418)

def update():
    return make_response('', 200)

def registerUsers():
    for i in range(1,20):
        v = queries.register(f'email{i}', 'secretpass', f'Company {i}', f'Address {i}', f'PL{i}{i}', f'N{i}P', f'123')
