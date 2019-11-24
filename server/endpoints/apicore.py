from flask import make_response
from flask_login import login_required, current_user
from db import queries
from endpoints.common import redirect_url, polish_api_data
import datetime
import enablebanking
import random

def status():
    # TODO - Add actual status verification of used services
    res = {'statuses': [{'service_name' : 'YATI', 'service_status' : True}]}
    return make_response(res, 200)

# @login_required
# TODO Token generated manually on localhost sevrer for now, implement redirecting to this server
def getToken(code):
    uid = current_user.get_id()
    api_client = enablebanking.ApiClient('Alior', connector_settings=polish_api_data)  # Create client instance.
    auth_api = enablebanking.AuthApi(api_client)
    token = auth_api.make_token(grant_type="authorization_code",  # grant type, MUST be set to "authorization_code"
                            code=code,
                            # The code received in the query string when redirected from authorization
                            redirect_uri=redirect_url)
    queries.updateToken(uid, token)


# @login_required
def generateToken():
    api_client = enablebanking.ApiClient('Alior', connector_settings=polish_api_data)  # Create client instance.
    auth_api = enablebanking.AuthApi(api_client)  # Create authentication interface.
    auth_url = auth_api.get_auth(
        response_type='code',  # OAuth2 response type
        redirect_uri=redirect_url,  # redirect URI
        scope=['aisp'],  # API scopes
        state='okok', 
        access = enablebanking.Access(
            valid_until=(datetime.datetime.now() + datetime.timedelta(days=89)).strftime('%Y-%m-%d'),
            balances=enablebanking.BalancesAccess(),
            transactions=enablebanking.TransactionsAccess())).url # state to pass to redirect URL
    res = {'oauth_link': auth_url}
    return make_response(res, 200)

@login_required
def tokenValid():
    token = queries.getTokenByUid(current_user.get_id())
    if token:
        # TODO - Check if token is still valid
        # if enablebanking.Token.expires_in(token) < 1:
            # return make_response('Token expired', 418)
        return make_response('', 200)
    return make_response('No token found', 418)

def getAccountBalance(uid):
    connector_settings = polish_api_data
    token = queries.getTokenByUid(uid)

    balance = 15000
    if token:
        connector_settings['accessToken'] = token
        api_client = enablebanking.ApiClient('Alior', connector_settings=connector_settings)  # Create client instance.
        aisp_api = enablebanking.AISPApi(api_client)
        user_config = queries.getUserInvoiceConfigByUid(uid)
        balance = aisp_api.get_account_balances(user_config.account_number)

    return balance.balances[0].balance_amount.amount

def getTransactionHistory(uid):
    connector_settings = polish_api_data
    token = queries.getTokenByUid(uid)

    if token:
        connector_settings['accessToken'] = token
        api_client = enablebanking.ApiClient('Alior', connector_settings=connector_settings)  # Create client instance.
        aisp_api = enablebanking.AISPApi(api_client)
        user_config = queries.getUserInvoiceConfigByUid(uid)

        date_from = queries.fetchLastUserTransaction(uid).timestamp
        print(date_from.strftime('%Y-%m-%d'), datetime.datetime.now().strftime('%Y-%m-%d'))

        transactions = aisp_api.get_account_transactions(user_config.account_number, date_from=date_from.strftime('%Y-%m-%d'),
        date_to=datetime.datetime.now().strftime('%Y-%m-%d'))
        print(transactions.transactions[0])
        # for transaction in transactions.transactions:
        #     transaction.entry_reference = 'PL64249010440000420042820498'
        #     user = queries.getUserByAccNo(transaction.entry_reference)
        #     if user:
        #         other_uid = user.uid
        #         ## Mocking some information due to lacking data from API
        #         if random.randint(0, 2) == 1:
        #             queries.addNewTransaction(uid, other_uid, transaction.transaction_amount.amount, f'Opłata za fakturę nr {random.randint(10000, 99999)}', transaction.transaction_amount.currency)
        #         else:
        #             queries.addNewTransaction(other_uid, uid, transaction.transaction_amount.amount, f'Opłata za fakturę nr {random.randint(10000, 99999)}', transaction.transaction_amount.currency)

    return None
