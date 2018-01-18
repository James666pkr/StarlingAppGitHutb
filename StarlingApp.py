import pyowm
import json
import requests

from bottle import run, route, template


redirect_uri = 'http://localhost:8080/callback'


@route('/starling/login/<access>')
def index(access):
    access_token = access
    headers = {'Authorization': access_token}
    url = "https://api-sandbox.starlingbank.com/api/v1/accounts/balance"
    response = requests.get(url, headers=headers)
    content = response.content
    print(content)
    return template('<b>Hi! Thank you for providing your access code, your transaction history is as follows:</b>!'
                        '<p> {{content}} <p>', access=access, content=content)

run(host='localhost', port=8080)

# go to http://localhost:8080/starling/login/
#after /login, enter 'Bearer {access_code}' from the Starling Sandbox, to see your account details.