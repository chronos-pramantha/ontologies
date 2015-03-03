__author__ = 'lorenzo'

import os
import platform

import simplejson as json

from wsgi.contexts import ONTOLOGIES


CACHE = {}


def get_o_path():
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.abspath(os.path.join(path, os.pardir))
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        ''' linux path '''
        path += '/SensorOntology/'
    else:
        '''  windows path  '''
        path += '\\SensorOntology\\'

    return path

path = get_o_path()


def get_or_set(nm, obj=None):
    spath = path + ONTOLOGIES[nm][1]
    if not obj:
        if nm in CACHE.keys() and CACHE[nm]:
            ontology = CACHE[nm]
        else:
            with open(str(spath), "r", encoding="utf8") as jsonld:
                CACHE[nm] = json.loads(jsonld.read())
                ontology = CACHE[nm]
        return json.dumps(ontology)
    else:
        if obj in CACHE.keys() and CACHE[obj]:
            result = CACHE[obj]
        else:
            with open(str(spath), "r", encoding="utf8") as jsonld:
                defines = json.loads(jsonld.read())['defines']
                print('http://pramantha.eu/' + nm + '/ontology/' + obj)
            for d in defines:
                if '@id' in d:
                    if d['@id'] == 'http://pramantha.eu/' + nm + '/ontology/' + obj:
                        d["@context"] = ONTOLOGIES[nm][2]
                        CACHE[obj] = d
                        result = CACHE[obj]
                        break
        return json.dumps(result)




