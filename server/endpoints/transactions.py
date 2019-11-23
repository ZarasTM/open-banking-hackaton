from flask import make_response
from flask_login import login_required, current_user
from db import queries

# @login_required
def getTransactionsSummary():
    try:
        invoices_as_buyer, invoices_as_seller = queries.getInvoicesSummary(current_user.get_id())
        # res = {'as_seller': [{'title': 'Pizza payment', 'other_party': 'Muzyczna', 'amount': 35.00, 'currency': 'PLN', 'date': '23.04.2019'}],
        #         'as_buyer': [{{'title': 'Weekly tomatoes', 'other_party': 'Pomidorex Sp. z o.o.', 'amount': 200.00, 'currency': 'PLN', 'date': '22.04.2019'}}]}
        
        res = {'as_seller': invoices_as_seller, 'as_buyer': invoices_as_buyer}
        return make_response(res, 200)
    except:
        return make_response('', 401)

# @login_required
# def getInvoice(body):
#     inv_no = body.get('invoice_id')
#     try:
#         res = queries.getInvoice(current_user.get_id(), inv_no)
#         if res:
#             res = {'res_id' : res.iid,
#                 'seller': queries.getUserresConfigByUid(res.seller),
#                 'buyer': queries.getUserresConfigByUid(res.buyer),
#                 'timestamp': res.timestamp,
#                 'amount': res.amount,
#                 'currency': res.currency,
#                 'title': res.name,
#                 'items': ast.literal_eval(res.items), # TODO - Security threat
#                 'amount_paid': res.amount_paid,
#                 'payable': res.payable}
#         return make_response(res, 200)
#     except:
#         return make_response('', 401)

# @login_required
# def createInvoice(body):
#     currency = body.get('currency') or 'PLN'
#     queries.addNewInvoice(body.get('seller_nip'), body.get('buyer_nip'), body.get('title'), body.get('items'), currency)
#     return make_response('', 200)

