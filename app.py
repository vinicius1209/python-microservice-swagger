import connexion
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
from providers.BaseAProvider import BaseAProvider

from injector import Binder

def basic_auth(username, password, required_scopes=None):
    if username == 'admin' and password == 'secret':
        info = {'sub': 'admin', 'scope': 'secret'}
    elif username == 'foo' and password == 'bar':
        info = {'sub': 'user1', 'scope': ''}
    else:
        # optional: raise exception for custom error response
        return None
    return info

def configure(binder: Binder) -> Binder:
    binder.bind(
        BaseAProvider
    )

if __name__ == '__main__':
    app = connexion.App(__name__, port=9090, specification_dir='swagger/')
    app.add_api('service-docs.yaml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app, modules=[configure])
    app.run()