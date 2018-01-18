import pyowm
import json
import requests

from bottle import run, route, template


redirect_uri = 'http://localhost:8080/callback'
url = "https://api-sandbox.starlingbank.com/api/v1/accounts/balance" # users account balance
url_me = "https://api-sandbox.starlingbank.com/api/v1/me" #get current identity
url_details = "https://api-sandbox.starlingbank.com/api/v1/me/api/v1/customers" # users personal details
url_mastercard = "https://api-sandbox.starlingbank.com/api/v1/transactions/mastercard" # users debit card transactions
url_all_trans = "https://api-sandbox.starlingbank.com/api/v1/transactions" # all of users transactions
url_trans_out = "https://api-sandbox.starlingbank.com/api/v1/transactions/fps/out" # all of users outbound FPS transactions
url_trans_in = "https://api-sandbox.starlingbank.com/api/v1/transactions/fps/in" # all of users inbound FPS transactions



@route('/starling/login/<access>')
def index(access):
    access_token = access
    headers = {'Authorization': access_token}
    url_response = requests.get(url, headers=headers)
    json_data = json.loads(url_response.text)
    balance = json_data['clearedBalance']
    currency = json_data['currency']
    availableToSpend = json_data['availableToSpend']
    print(balance)
    print(json_data)
    return template('<b>Hi! Thank you for providing your access code, your balance is {{balance}} {{currency}} and you have {{availableToSpend}} {{currency}} available to spend!</b>!'
                    , balance=balance, currency=currency, availableToSpend=availableToSpend)


run(host='localhost', port=8080)

# go to http://localhost:8080/starling/login/
# after /login, enter 'Bearer {access_code}' from the Starling Sandbox, to see users account details.