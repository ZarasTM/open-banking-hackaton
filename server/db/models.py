from config import db, ma
from datetime import datetime
from flask_login import UserMixin

class UserLogin(UserMixin, db.Model):
    __tablename__ = 'user_login'
    uid = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)

    def get_id(self):
        return self.uid

class UserLoginSchema(ma.ModelSchema):
    class Meta:
        model = UserLogin
        sqla_session = db.session  


class UserConfig(db.Model):
    __tablename__ = 'user_config'
    uid = db.Column(db.Integer, db.ForeignKey('user_login.uid'), nullable=False, autoincrement=True, primary_key=True)
    default_currency = db.Column(db.String(64), nullable=False, default='PLN')
    timezone = db.Column(db.String(64), nullable=False, default='UTC')
    api_key = db.Column(db.String(64))
    status = db.Column(db.Integer, nullable=False, default=0)

class UserConfigSchema(ma.ModelSchema):
    class Meta:
        model = UserConfig
        sqla_session = db.session  

class UserInvoice(db.Model):
    __tablename__ = 'user_invoice'
    uid = db.Column(db.Integer, db.ForeignKey('user_login.uid'), nullable=False, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    account_number = db.Column(db.String(64), nullable=False)
    tin = db.Column(db.String(64), nullable=False)

class UserInvoiceSchema(ma.ModelSchema):
    class Meta:
        model = UserInvoice
        sqla_session = db.session  

class Balance(db.Model):
    __tablename__ = 'balance'
    seller = db.Column(db.Integer, db.ForeignKey('user_login.uid'), nullable=False, primary_key=True)
    buyer = db.Column(db.Integer, db.ForeignKey('user_login.uid'), nullable=False, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(64), nullable=False, default='PLN')
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

class BalanceSchema(ma.ModelSchema):
    class Meta:
        model = Balance
        sqla_session = db.session


class Invoice(db.Model):
    __tablename__ = 'invoice'
    iid = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    seller = db.Column(db.Integer, db.ForeignKey('user_login.uid'), nullable=False)
    buyer = db.Column(db.Integer, db.ForeignKey('user_login.uid'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(64), nullable=False, default='PLN')
    name = db.Column(db.String(64), nullable=False)
    items = db.Column(db.String(2137), nullable=False)

class InvoiceSchema(ma.ModelSchema):
    class Meta:
        model = Invoice
        sqla_session = db.session

class Transaction(db.Model):
    __tablename__ = 'transaction'
    tid = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    seller = db.Column(db.Integer, db.ForeignKey('user_login.uid'), nullable=False)
    buyer = db.Column(db.Integer, db.ForeignKey('user_login.uid'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(64), nullable=False, default='PLN')
    name = db.Column(db.String(64), nullable=False)

class TransactionSchema(ma.ModelSchema):
    class Meta:
        model = Transaction
        sqla_session = db.session

### NON-DB MODELS ###
class User():
    def __init__(self):
        self.is_authenticated = False
        self.is_active = False
        self.is_anonymous = False
    
    def get_id(self):
        pass