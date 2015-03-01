__author__ = 'lorenzo'


ONTOLOGIES = dict(
    {
        "chronos": ["a generic ontology for space activities", "ChronosOntology.json"],
        "sensors": ["an ontology for detectors, device that use some kind of sensor", "SpaceSensor_json-ld_v2.json"],
        "astronomy": ["an ontology for astronomical objects", "Astronomy.json"],
        "engineering": ["an ontology for engineering concepts", "Engineering.json"]
    }

)

CHRONOS_CONTEXT = dict(
    {
        "rdf"    : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "skos"   : "http://www.w3.org/2004/02/skos/core#",
        "schema" : "http://schema.org/",
        "dbpedia": "http://dbpedia.org/property/",
        "owl"    : "http://www.w3.org/2002/07/owl#",
        "chronos": "http://pramantha.eu/chronos/ontology/",
        "@base"  : "http://pramantha.eu/chronos/ontology"
    }
)

SENSORS_CONTEXT = dict(
    {
        "rdf"    : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "skos"   : "http://www.w3.org/2004/02/skos/core#",
        "schema" : "http://schema.org/",
        "dbpedia": "http://dbpedia.org/property/",
        "owl"    : "http://www.w3.org/2002/07/owl#",
        "sensor" : "http://pramantha.eu/sensors/ontology/",
        "@base"  : "http://pramantha.eu/sensors/ontology"
    }
)

ASTRONOMY_CONTEXT = dict(
    {
        "@base"    : "http://pramantha.eu/astronomy/ontology",
        "astronomy": "http://pramantha.eu/astronomy/ontology/",
        "schema"   : "https://schema.org/",
        "skos"     : "http://www.w3.org/2004/02/skos/core#",
        "rdf"      : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs"     : "http://www.w3.org/2000/01/rdf-schema#",
        "owl"      : "http://www.w3.org/2002/07/owl#",
        "dbpedia"  : "http://dbpedia.org/ontology/"
    }
)

ENGINEERING_CONTEXT = dict(
    {
        "@base"      : "http://pramantha.eu/engineering/ontology",
        "engineering": "http://pramantha.eu/engineering/ontology/",
        "schema"     : "https://schema.org/",
        "skos"       : "http://www.w3.org/2004/02/skos/core#",
        "rdf"        : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs"       : "http://www.w3.org/2000/01/rdf-schema#",
        "owl"        : "http://www.w3.org/2002/07/owl#",
        "dbpedia"    : "http://dbpedia.org/ontology/"
    }
)
