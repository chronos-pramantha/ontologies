__author__ = 'lorenzo'

import os
from os.path import dirname, join

from flask import Flask
from flask import request, Response, redirect, url_for, render_template
import simplejson as json
import requests

from src.cache import get_or_set, get_o_path
from src.contexts import ONTOLOGIES
from src.libs.utilities import classes_and_properties


app = Flask(__name__, template_folder=join(dirname(__file__), 'src', 'templates'))
app.config.from_object('config')

# url of Chronos APIs
CHRONOS_APIS = "http://chronosapi-chronoslod.rhcloud.com/"

if os.getenv('GAE_ENV', '').startswith('standard'):
  # Production in the standard environment
    host = "https://ontologies.pramantha.net/"
    app.config['DEBUG'] = False
else:
  # Local execution
    host = "http://127.0.0.1:5000/"
    app.config['DEBUG'] = True


def hello():
    """
    Returns template for the Homepage
    """
    res = {
        "chronos": ["a generic ontology for space activities semantically linked to Wikipedia documents", "/chronos", "/documentation/chronos"],
        "sensors": ["an ontology for detectors, device that use some kind of sensor", "/sensors", "/documentation/sensors"],
        "astronomy": ["an ontology for astronomical objects", "/astronomy", "/documentation/astronomy"],
        "solarsystem" : ["a taxonomy for astronomical objects in the solar system", "/solarsystem", "/documentation/solarsystem"],
        "engineering": ["an ontology for engineering concepts", "/engineering", "/documentation/engineering"],
        "spacecraft": ["an ontology for a spacecraft and its systems", "/spacecraft", "/documentation/spacecraft"],
        "subsystems": ["an ontology for subsystems in a spacecraft", "/subsystems", "/documentation/subsystems"],
        "exploration": ["an ontology for space exploration and mission design", "/exploration", "/documentation/exploration"]
}
    return render_template('index.html', content=res)


@app.route('/documentation/', defaults={'name': 'index'})
@app.route("/documentation/<name>", methods=['GET'])
def documentation(name):
    """
    Routes to index or specific ontology or Chronos APIs explorer
    :param name: name of the ontology, deafult is 'index' to return the homepage
    """
    name = name.lower()
    if name == 'index':
        return hello()   
    elif name and name in ONTOLOGIES.keys():
        if request.method == 'GET':
            ontology = json.loads(get_or_set(name))
            title = {"label": ontology['rdf:label'],
                     "comment": ontology['rdf:comment'],
                     "name": host + name + "/"}
            context = ontology['@context']
            content = ontology['defines']
            classes, properties = classes_and_properties(content)

            return render_template('jsonld.html', title=title, name=name, context=context, 
                                    classes=classes, properties=properties, host=host)
    elif name == 'chronosapi':
        return redirect(url_for('chronosapi'))
    else:
        return wrong_uri()


@app.route('/', defaults={'name': 'documentation'})
@app.route("/<name>/", methods=['GET'])
def index(name):
    """
    Serves the ontology called by name
    :param name: the name of the ontology
    :return:
    """
    name = name.lower()
    if name and name in ONTOLOGIES.keys():
        #
        # serve name/ontology
        #
        data_format = request.args.get('format')
        if data_format and data_format == 'jsonld':
            ontology = get_or_set(name)
            res = Response(response=str(ontology), content_type="application/ld+json; charset=utf-8")
            print(res)
            return res
        else:
            # serve nt
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src', 'RDFvocab', 'ntriples', name + '.ntriples')
            with open(path, 'r') as content_file:
                content = content_file.read()
            return Response(response=str(content), content_type="application/n-triples; charset=utf-8")
    elif name == 'documentation':
        return redirect(url_for('documentation'))
    else:
        return wrong_uri()


@app.route("/<name>/<obj>/", methods=['GET'])
def chronos(name, obj):
    """
    Serves the single object from an ontology
    :param name: name of the ontology
    :param obj: label of the object
    :return:
    """
    name = name.lower()
    if name in ONTOLOGIES.keys():
        data_format = request.args.get('format')
        if data_format and data_format == 'jsonld':
            obj = get_or_set(name, obj)
            return Response(response=str(obj), content_type="application/ld+json; charset=utf-8")
        else:
            # use rdf-translator
            # return n-triples
            from src.libs.utils import rdf_translate
            obj = get_or_set(name, obj)
            print(obj)
            content = rdf_translate(obj)
            return Response(response=str(content), content_type="application/n-triples; charset=utf-8")
    return wrong_object()


@app.route("/chronosapi/", defaults={'url': None})
@app.route("/chronosapi/<url>", methods=['GET'])
def chronosapi(url):
    """
    Chronos APIs Explorer (a small client for an HATEOAS API)
    :param url: url or a Chronos API's endpoint
    :return:
    """
    from src.libs.json2html import get_html_table
    from src.libs.utils import decode_url, check_if_url

    if url is None:
        url = CHRONOS_APIS
    else:
        url = decode_url(str(url))

    #print(url)

    if not check_if_url(url):
        raise Exception('wrong url')
    jsonld = requests.get(url).text
    #print(jsonld)
    jsonld = json.loads(jsonld)
    table = ""
    if isinstance(jsonld, list):
        for j in jsonld:
            table += get_html_table(json.dumps(j))
    else:
        table = get_html_table(json.dumps(jsonld))
    return render_template("chronosapi.html", table=table)


@app.errorhandler(404)
def wrong_uri(e=None):
    message = {
            "status": 404,
            "message": "Not one of Project Chronos LOD URI: " + request.url,
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
    app.run()
