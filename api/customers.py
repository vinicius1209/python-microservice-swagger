from flask_injector import inject
from providers.BaseAProvider import BaseAProvider

@inject(data_provider=BaseAProvider)
def read_customer(data_provider, cpf) -> str:
    return data_provider.read_customer(cpf)
