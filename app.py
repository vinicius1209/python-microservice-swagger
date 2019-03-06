import connexion
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
from providers.BaseAProvider import BaseAProvider
import requests
import json
from injector import Binder

def getAuth(username, password, required_scopes=None):

    data = {'username': username, 'password': password}
    header = {'Content-Type': 'application/json'}

    try:
        #Make a requisition to check credencials
        r = requests.post('http://127.0.0.1:5000/auth', json=data, headers=header)
        if r.status_code == 200:
            token = json.loads(r.text)
            print(token['access_token'])
        else:
            return None
    except Exception as e:
        print(e)
        return None
    return token

def configure(binder: Binder) -> Binder:
    binder.bind(
        BaseAProvider
    )

if __name__ == '__main__':
    app = connexion.App(__name__, port=9090, specification_dir='swagger/')
    app.add_api('service-docs.yaml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app, modules=[configure])
    app.run()
