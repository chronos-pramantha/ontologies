__author__ = 'lorenzo'

#
# Contexts for single objects and properties. Full ontology contexts are in the files
#


CHRONOS_CONTEXT = dict(
    {
        "rdf"    : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "skos"   : "http://www.w3.org/2004/02/skos/core#",
        "schema" : "http://schema.org/",
        "dbpedia": "http://dbpedia.org/property/",
        "owl"    : "http://www.w3.org/2002/07/owl#",
        "chronos": "http://ontology.projectchronos.eu/chronos/",
        "@base"  : "http://ontology.projectchronos.eu/chronos",
        "defines": {
            "@reverse": "rdfs:isDefinedBy"
        }
    }
)

SENSORS_CONTEXT = dict(
    {
        "rdf"    : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "skos"   : "http://www.w3.org/2004/02/skos/core#",
        "schema" : "http://schema.org/",
        "dbpedia": "http://dbpedia.org/property/",
        "owl"    : "http://www.w3.org/2002/07/owl#",
        "sensor" : "http://ontology.projectchronos.eu/sensors/",
        "@base"  : "http://ontology.projectchronos.eu/sensors"
    }
)

ASTRONOMY_CONTEXT = dict(
    {
        "@base"    : "http://ontology.projectchronos.eu/astronomy",
        "astronomy": "http://ontology.projectchronos.eu/astronomy/",
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
        "@base"      : "http://ontology.projectchronos.eu/engineering",
        "engineering": "http://ontology.projectchronos.eu/engineering/",
        "schema"     : "https://schema.org/",
        "skos"       : "http://www.w3.org/2004/02/skos/core#",
        "rdf"        : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs"       : "http://www.w3.org/2000/01/rdf-schema#",
        "owl"        : "http://www.w3.org/2002/07/owl#",
        "dbpedia"    : "http://dbpedia.org/ontology/"
    }
)

SPACECRAFT_CONTEXT = dict(
    {
        "engineering": "http://ontology.projectchronos.eu/engineering/",
        "@base": "http://ontology.projectchronos.eu/spacecraft",
        "spacecraft": "http://ontology.projectchronos.eu/spacecraft/",
        "schema": "https://schema.org/",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "owl": "http://www.w3.org/2002/07/owl#",
        "dbpedia": "http://dbpedia.org/ontology/"
    }
)

SUBSYSTEMS_CONTEXT = dict(
    {
        "@base": "http://ontology.projectchronos.eu/subsystems",
        "spacecraft": "http://ontology.projectchronos.eu/spacecraft/",
        "subsystems": "http://ontology.projectchronos.eu/subsystems/",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "owl": "http://www.w3.org/2002/07/owl#",
        "dbpedia": "http://dbpedia.org/ontology/",
        "xml": "http://www.w3.org/2001/XMLSchema#"
    }
)

SOLARSYSTEM_CONTEXT = dict(
    {
        "@base"    : "http://ontology.projectchronos.eu/solarsystem",
        "astronomy": "http://ontology.projectchronos.eu/astronomy/",
        "rdf"      : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs"     : "http://www.w3.org/2000/01/rdf-schema#",
        "owl"      : "http://www.w3.org/2002/07/owl#"
    }
)

ONTOLOGIES = dict(
    {
        "chronos": ["a generic ontology for space activities", "ChronosOntology.json", CHRONOS_CONTEXT],
        "sensors": ["an ontology for detectors, device that use some kind of sensor", "SpaceSensor_json-ld_v2.json", SENSORS_CONTEXT],
        "astronomy": ["an ontology for astronomical objects", "Astronomy.json", ASTRONOMY_CONTEXT],
        "solarsystem" : ["an ontology for astronomical objects in the solar system", "SolarSystem.jsonld", SOLARSYSTEM_CONTEXT],
        "engineering": ["an ontology for engineering concepts", "Engineering.json", ENGINEERING_CONTEXT],
        "spacecraft": ["an ontology for a spacecraft and its systems", "Spacecraft.json", SPACECRAFT_CONTEXT],
        "subsystems": ["an ontology for subsystems in a spacecraft", "SubSystems.json", SUBSYSTEMS_CONTEXT]
    }

)