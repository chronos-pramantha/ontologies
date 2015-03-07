__author__ = 'lorenzo'

import os

from flask import Flask
from flask import request, jsonify, Response
import simplejson as json

from wsgi.utilities import get_or_set
from wsgi.contexts import ONTOLOGIES


app = Flask(__name__)

@app.route("/")
def hello():
    res = jsonify(
        {
            "chronos": ["a generic ontology for space activities", "/chronos"],
            "sensors": ["an ontology for detectors, device that use some kind of sensor", "/sensors"],
            "astronomy": ["an ontology for astronomical objects", "/astronomy"],
            "solarsystem" : ["an ontology for astronomical objects in the solar system"],
            "engineering": ["an ontology for engineering concepts", "/engineering"],
            "spacecraft": ["an ontology for a spacecraft and its systems", "/spacecraft"],
            "subsystems": ["an ontology for subsystems in a spacecraft", "/subsystems"]
        }
    )
    return res


@app.route("/<name>/", methods=['GET'])
def index(name):
    name = name.lower()
    if name and name in ONTOLOGIES.keys():
        #
        # serve name/ontology
        #
        ontology = get_or_set(name)
        res = Response(response=str(ontology), content_type="application/ld+json; charset=utf-8")
        print(res)
        return res
    return wrong_uri()


@app.route("/<name>/<obj>/", methods=['GET'])
def chronos(name, obj):
    name = name.lower()
    if name in ONTOLOGIES.keys():
        obj = get_or_set(name, obj)
        return Response(response=str(obj), content_type="application/ld+json; charset=utf-8")
    return wrong_object()


@app.errorhandler(404)
def wrong_uri(e=None):
    message = {
            "status": 404,
            "message": "Not one of Pramantha LOD URI: " + request.url,
    }
    resp = Response(response=str(message), content_type="application/ld+json; charset=utf-8")
    # resp.status_code = 404
    return resp

@app.errorhandler(404)
def wrong_object(e=None):
    message = {
            "status": 404,
            "message": "Object not in the ontology: " + request.url,
    }
    resp = Response(response=str(message), content_type="application/ld+json; charset=utf-8")
    # resp.status_code = 404
    return resp


if __name__ == "__main__":
    if 'OPENSHIFT_DATA_DIR' in os.environ:
        #store = os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'newsletter.save')
        host = "http://ontology.projectchronos.eu/"
        app.config['DEBUG'] = False
    else:
        #store = os.path.join(os.path.dirname(__file__), 'newsletter.save')
        host = "http://127.0.0.1:5000"
        app.config['DEBUG'] = True

    app.config.from_object('config')
    app.run()
