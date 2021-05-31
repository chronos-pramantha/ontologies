__author__ = 'lorenzo'

import os
import platform

import simplejson as json

from src.contexts import ONTOLOGIES


CACHE = {}


def get_o_path(fs):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'RDFvocab', 'ld+json', fs)


def get_or_set(nm, obj=None):
    spath = get_o_path(ONTOLOGIES[nm][1])
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
            result = None
            with open(str(spath), "r", encoding="utf8") as jsonld:
                defines = json.loads(jsonld.read())["defines"]
                print("http://ontologies.pramantha.net/" + nm + "/" + obj)
            for d in defines:
                if "@id" in d:
                    if d["@id"] == "http://ontologies.pramantha.net/" + nm + "/" + obj:
                        d["@context"] = ONTOLOGIES[nm][2]
                        CACHE[obj] = d
                        result = CACHE[obj]
                        break
        return json.dumps(result)




