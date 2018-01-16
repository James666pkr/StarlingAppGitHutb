import pyowm

from bottle import run, route, template


client_id = r'YUmpX3Vd3WabChjdLYw0'
client_secret = r'tPmR9ntzpfEJ8b7moPuz3XBAgNPUZ3tEP54X7us9'
redirect_uri = 'StarlingApp://authenticationResponse'

scope = ['balance:read',
         'transaction:read',
         'payee:read',
         'mandate:read',
         'savings-goal:read',
         'savings-goal-transfer:read',
         'account:read',
         'customer:read',
         'address:read',
         'card:read']


@route('/starling/login/<name>')
def index(name):
    return template('<b>Login below {{name}}</b>!'
                    '<a href="https://api-sandbox.starlingbank.com/?client_id=$YUmpX3Vd3WabChjdLYw0&response_type=code&state=$state&redirect_uri=$http://localhost:8080/callback">Login here</a>, '
                    , name=name)

run(host='localhost', port=8080)

