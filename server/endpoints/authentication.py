from flask import make_response
from flask_login import login_required, login_user, current_user, logout_user
from db import queries
import base64
import pyotp
import random
import hashlib
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
    
    # Create TOTP code
    totp_secret = base64.b32encode(hashlib.sha1(str(random.randint(1000, 10000)).encode('utf-8')).hexdigest().encode('utf-8'))#.upper()
    totp_link = pyotp.totp.TOTP(totp_secret).provisioning_uri(email, issuer_name="YATI")

    # Create new user
    if queries.emailRegistered(email):
        return make_response('Email already registered', 401)
    if queries.tinRegistered(tin):
        return make_response('Tin already registered', 401)

    if queries.register(email, hashed, company_name, address, account_number, tin, totp_secret): 
        return make_response({'totp_secret': str(totp_secret), 'totp_link': totp_link}, 200)
    return make_response('', 500)

def login(body):
    email = body.get('email')
    password = body.get('password')
    remember = body.get('remember')
    totp_code = body.get('totp_code')

    user = queries.getUserByEmail(email)
    totp = pyotp.TOTP(user.totp_secret)
    
    if user != None and totp.verify(totp_code) and bcrypt.checkpw(password.encode(), user.password):
        login_user(user, remember=remember)
        return make_response('', 200)
    return make_response('', 401)

def isLogged():
    if current_user.is_authenticated:
        return make_response('', 200)    
    return make_response('', 401)

# @login_required
def logout():
    logout_user()
    return make_response('', 200)