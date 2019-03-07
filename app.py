import connexion
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
from providers.BaseAProvider import BaseAProvider
import requests
from injector import Binder

#Check token receveid from header
def check_token(token):

    header = {'Authorization': 'JWT {}'.format(token)}

    try:
        #Make a requisition to check credencials
        r = requests.get('http://127.0.0.1:5000/checkAuth', headers=header)
        if r.status_code == 200:
            return {'status': '200'}
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
