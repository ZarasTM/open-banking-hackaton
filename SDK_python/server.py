from flask import Flask, request
app = Flask(__name__)

import datetime

import logging

import enablebanking

import util

# import do_magic.User


REDIRECT_URL = "http://localhost:5005"  # PUT YOUR REDIRECT URI HERE

def nordea_settings():
    return {
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


@app.route('/')
def keyRedirect():
    # token = auth_api.make_token(grant_type="authorization_code",  # grant type, MUST be set to "authorization_code"
    #                                 code=parsed_query.get("code"),
    #                                 # The code received in the query string when redirected from authorization
    #                                 redirect_uri=REDIRECT_URL)
    code = request.args.get("code")
    # print(f"\nCode: {code}\n\n")

    api_client = enablebanking.ApiClient("Alior", connector_settings=nordea_settings())  # Create client instance.

    auth_api = enablebanking.AuthApi(api_client)  # Create authentication interface.

    # auth_url = auth_api.get_auth(
    #     response_type="code",  # OAuth2 response type
    #     redirect_uri=REDIRECT_URL,  # redirect URI
    #     scope=["aisp"],  # API scopes
    #     state="okok").url # state to pass to redirect URL

    # redirected_url = util.read_redirected_url(auth_url, REDIRECT_URL)
    # parsed_query = util.parse_redirected_url(redirected_url)  # calling helper functions for CLI interaction
    # logging.info("Parsed query: %s", parsed_query)

    token = auth_api.make_token(grant_type="authorization_code",  # grant type, MUST be set to "authorization_code"
                                code=code,
                                # The code received in the query string when redirected from authorization
                                redirect_uri=REDIRECT_URL)
    # logging.info("Token: %s", token)

    aisp_api = enablebanking.AISPApi(api_client)  # api_client has already accessToken and refreshToken applied after call to makeToken()

    accounts = aisp_api.get_accounts()
    x = "Accounts info: %s" % accounts

    for account in accounts.accounts:
        transactions = aisp_api.get_account_transactions(account.account_id.iban, date_from=(datetime.datetime.now() - datetime.timedelta(days=89)).strftime('%Y-%m-%d'),
        date_to=datetime.datetime.now().strftime('%Y-%m-%d'))
        x += "Transactions info: %s"% transactions

        balances = aisp_api.get_account_balances(account.account_id.iban)
        x += "Balances info: %s"% balances
    # TODO: how to save it somewhere else
    # do_magic.magic(x)
    return x

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5005)    

def getResults():
    return result, count

