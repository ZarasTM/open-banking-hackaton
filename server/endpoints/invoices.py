from flask import make_response
from flask_login import login_required, current_user
from db import queries

@login_required
def getInvoicesSummary(body):
    # TODO - Implement mocked function
    try:
        # invoices_as_buyer, invoices_as_seller = queries.getInvoicesSummary(current_user.get_id())
        res = {'as_seller': [{'title': 'Pizza payment', 'other_party': 'Muzyczna', 'amount': 35.00, 'currency': 'PLN', 'date': '23.04.2019'}],
                'as_buyer': [{{'title': 'Weekly tomatoes', 'other_party': 'Pomidorex Sp. z o.o.', 'amount': 200.00, 'currency': 'PLN', 'date': '22.04.2019'}}]}
        return make_response(res, 200)
    except:
        return make_response('', 401)

@login_required
def getInvoice(body):
    # TODO - Implement mocked function
    try:
        # invoice = queries.getInvoice(current_user.get_id())
        res = {}
        return make_response(res, 200)
    except:
        return make_response('', 401)

