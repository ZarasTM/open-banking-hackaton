from flask import make_response, current_user
from db import queries
from endpoints.common import redirect_url, polish_api_data
import datetime
import enablebanking

def status():
    # TODO - Add actual status verification of used services
    res = {'statuses': [{'service_name' : 'YATI', 'service_status' : True}]}
    return make_response(res, 200)

# @login_required
def getToken(code):
    api_client = enablebanking.ApiClient("Alior", connector_settings=polish_api_data)  # Create client instance.
    auth_api = enablebanking.AuthApi(api_client)  # Create authentication interface.

    token = auth_api.make_token(grant_type="authorization_code",  # grant type, MUST be set to "authorization_code"
                                code=code,
                                # The code received in the query string when redirected from authorization
                                redirect_uri=redirect_url)

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

# @login_required
def tokenValid():
    token = queries.getTokenByUid(current_user.get_id())
    if token:
        # TODO - Check if token is still valid
        if enablebanking.Token.expires_in(token) < 1:
            return make_response('Token expired', 418)
        return make_response('', 200)
    return make_response('No token found', 418)