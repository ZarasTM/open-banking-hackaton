import logging
import enablebanking
import util
import datetime

REDIRECT_URL = "http://localhost:5005"  # PUT YOUR REDIRECT URI HERE

polish_api_data = {
        "clientId": "852f7d28-02b8-4b5d-9a16-a338e55e3de1",  # API client ID
        "clientSecret": "xI2kE6bC3rV0aH7xK4hS1dX5xX0lF5aJ7aE3cY6wX3hE7sL5wR",
        "certPath": None,  # Path or URI to QWAC certificate in PEM format
        "keyPath": None,  # Path or URI to QWAC certificate private key in PEM format
        "signKeyPath": None,
        "signPubKeySerial":None,
        "signFingerprint":None,
        "signCertUrl":None,
        "sandbox": True,
        "consentId": None,
        "accessToken": None,
        "refreshToken": None
    }

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