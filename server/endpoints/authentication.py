from flask import make_response
from flask_login import login_required, login_user, current_user, logout_user
from db import queries
import bcrypt

def register(body):
    email = body.get('email')
    password = body.get('password')
    company_name = body.get('company_name')
    tin = body.get('tin')
    address = body.get('address')
    account_number = body.get('account_number')
    
    # Password hashing
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)

    # Check data uniqueness 
    if queries.emailRegistered(email):
        return make_response('Email already in use', 409)

    # Create new user
    if queries.register(email, hashed, company_name, address, account_number, tin): 
        return make_response('', 200)
    return make_response('', 500)

def login(body):
    email = body.get('email')
    password = body.get('password')
    remember = body.get('remember')

    user = queries.getUserByEmail(email)
    if user != None and bcrypt.checkpw(password.encode(), user.password):
        login_user(user, remember=remember)
        return make_response('', 200)
    return make_response('', 401)

def isLogged():
    if current_user.is_authenticated:
        return make_response('', 200)    
    return make_response('', 401)

@login_required
def logout():
    logout_user()
    return make_response('', 200)