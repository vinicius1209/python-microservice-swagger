import couchdb
import flask

COUCHDB_URL = 'http://localhost:5984/'

couch = couchdb.Server(COUCHDB_URL)

class BaseAProvider(object):

    #Search a customer by CPF
    def read_customer(self, cpf) -> str:

        #Check auth header
        if 'Authorization' not in flask.request.headers:
            return {"error": "Not correctly authorized"}, 401

        db = couch['customer']
        rows = db.view('_all_docs', include_docs=True)

        #Return doc if founded
        for row in rows:
            if cpf == row.doc['cpf']:
                return row.doc, 200

        return {"error": "customer not found"}, 400
