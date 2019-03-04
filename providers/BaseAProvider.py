import couchdb

COUCHDB_URL = 'http://localhost:5984/'

couch = couchdb.Server(COUCHDB_URL)

class BaseAProvider(object):

    def create_customer(self, payload):
        db = couch['customer']
        if payload['cpf'] in db:
            return {"error": "Found customer with existing CPF"}, 409
        else:
            db.save(payload)
            return payload, 201

    def read_customer(self, cpf) -> str:
        db = couch['customer']
        rows = db.view('_all_docs', include_docs=True)
        for row in rows:
            if cpf == row.doc['cpf']:
                return row.doc, 200

        return {"error": "customer not found"}, 400
