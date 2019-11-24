import logging
import enablebanking
import util
import datetime

def registerToken():
    api_client = enablebanking.ApiClient("Alior", connector_settings=polish_api_data)  # Create client instance.
    auth_api = enablebanking.AuthApi(api_client)  # Create authentication interface.
    auth_url = auth_api.get_auth(
        response_type="code",  # OAuth2 response type
        redirect_uri=REDIRECT_URL,  # redirect URI
        scope=["aisp"],  # API scopes
        state="okok", 
        access = enablebanking.Access(
            valid_until=(datetime.datetime.now() + datetime.timedelta(days=89)).strftime('%Y-%m-%d'),
            balances=enablebanking.BalancesAccess(),
            transactions=enablebanking.TransactionsAccess())).url # state to pass to redirect URL

    print(auth_url)
    # redirected_url = util.read_redirected_url(auth_url, REDIRECT_URL)
    # Here user is redirected to Alior Bank authentication

registerToken()