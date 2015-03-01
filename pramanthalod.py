__author__ = 'lorenzo'

import os


from flask import Flask
from flask import request, jsonify

from utilities import get_or_set
from contexts import ONTOLOGIES


app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return jsonify({
        "chronos": host + "/chronos/ontology",
        "sensors": host + "/sensors/ontology",
        "astronomy": host + "/astronomy/ontology",
        "engineering": host + "/engineering/ontology"
    })


@app.route("/<name>/ontology/", methods=['GET'])
def index(name):
    name = name.lower()
    if name in ONTOLOGIES.keys():
        ontology = get_or_set(name)
        return jsonify(ontology)
    return not_found()


@app.route("/<name>/ontology/<object>", methods=['GET'])
def chronos(name, object):
    name = name.lower()
    if name in ONTOLOGIES.keys():
        obj = get_or_set(name, object)
        return jsonify(obj)
    return not_found()


@app.errorhandler(404)
def not_found(e=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    if 'OPENSHIFT_DATA_DIR' in os.environ:
        #store = os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'newsletter.save')
        host = "http://pramantha.eu"
        app.config['DEBUG'] = True
    else:
        #store = os.path.join(os.path.dirname(__file__), 'newsletter.save')
        host = "http://127.0.0.1:5000"
        app.config['DEBUG'] = True

    app.config.from_object('config')
    app.run()