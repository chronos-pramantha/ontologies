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
        "chronos": "http://ontology.pramantha.net/chronos/",
        "@base"  : "http://ontology.pramantha.net/chronos",
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
        "sensor" : "http://ontology.pramantha.net/sensors/",
        "chronos": "http://ontology.pramantha.net/chronos/",
        "@base"  : "http://ontology.pramantha.net/sensors",
        "defines": {
            "@reverse": "http://www.w3.org/2000/01/rdf-schema#isDefinedBy"
        }
    }
)

ASTRONOMY_CONTEXT = dict(
    {
        "@base"    : "http://ontology.pramantha.net/astronomy",
        "astronomy": "http://ontology.pramantha.net/astronomy/",
        "schema"   : "https://schema.org/",
        "skos"     : "http://www.w3.org/2004/02/skos/core#",
        "rdf"      : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs"     : "http://www.w3.org/2000/01/rdf-schema#",
        "owl"      : "http://www.w3.org/2002/07/owl#",
        "chronos": "http://ontology.pramantha.net/chronos/",
        "dbpedia"  : "http://dbpedia.org/ontology/",
        "defines": {
            "@reverse": "http://www.w3.org/2000/01/rdf-schema#isDefinedBy"
        }
    }
)

ENGINEERING_CONTEXT = dict(
    {
        "@base"      : "http://ontology.pramantha.net/engineering",
        "engineering": "http://ontology.pramantha.net/engineering/",
        "schema"     : "https://schema.org/",
        "skos"       : "http://www.w3.org/2004/02/skos/core#",
        "rdf"        : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs"       : "http://www.w3.org/2000/01/rdf-schema#",
        "owl"        : "http://www.w3.org/2002/07/owl#",
        "dbpedia"    : "http://dbpedia.org/ontology/",
        "defines": {
            "@reverse": "http://www.w3.org/2000/01/rdf-schema#isDefinedBy"
        }
    }
)

SPACECRAFT_CONTEXT = dict(
    {
        "engineering": "http://ontology.pramantha.net/engineering/",
        "@base": "http://ontology.pramantha.net/spacecraft",
        "spacecraft": "http://ontology.pramantha.net/spacecraft/",
        "schema": "https://schema.org/",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "owl": "http://www.w3.org/2002/07/owl#",
        "chronos": "http://ontology.pramantha.net/chronos/",
        "dbpedia": "http://dbpedia.org/ontology/",
        "defines": {
            "@reverse": "http://www.w3.org/2000/01/rdf-schema#isDefinedBy"
        }
    }
)

SUBSYSTEMS_CONTEXT = dict(
    {
        "@base": "http://ontology.pramantha.net/subsystems",
        "spacecraft": "http://ontology.pramantha.net/spacecraft/",
        "subsystems": "http://ontology.pramantha.net/subsystems/",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "owl": "http://www.w3.org/2002/07/owl#",
        "dbpedia": "http://dbpedia.org/ontology/",
        "chronos": "http://ontology.pramantha.net/chronos/",
        "xml": "http://www.w3.org/2001/XMLSchema#",
        "defines": {
            "@reverse": "http://www.w3.org/2000/01/rdf-schema#isDefinedBy"
        }
    }
)

SOLARSYSTEM_CONTEXT = dict(
    {
        "@base"    : "http://ontology.pramantha.net/solarsystem",
        "astronomy": "http://ontology.pramantha.net/astronomy/",
        "rdf"      : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs"     : "http://www.w3.org/2000/01/rdf-schema#",
        "owl"      : "http://www.w3.org/2002/07/owl#",
        "chronos": "http://ontology.pramantha.net/chronos/",
        "defines": {
            "@reverse": "http://www.w3.org/2000/01/rdf-schema#isDefinedBy"
        }
    }
)

EXPLORATION_CONTEXT = dict(
    {
        "@base": "http://ontology.pramantha.net/exploration",
        "exploration": "http://ontology.pramantha.net/exploration/",
        "schema": "https://schema.org/",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "chronos": "http://ontology.pramantha.net/chronos/",
        "owl": "http://www.w3.org/2002/07/owl#",
        "dbpedia": "http://dbpedia.org/ontology/",
        "cyc": "http://sw.opencyc.org/2012/05/10/concept/en/",
        "defines": {
            "@reverse": "http://www.w3.org/2000/01/rdf-schema#isDefinedBy"
        }
    }
)

ONTOLOGIES = dict(
    {
        "chronos": ["a generic ontology for space activities", "Chronos.json", CHRONOS_CONTEXT],
        "sensors": ["an ontology for detectors, device that use some kind of sensor", "Sensors.json", SENSORS_CONTEXT],
        "astronomy": ["an ontology for astronomical objects", "Astronomy.json", ASTRONOMY_CONTEXT],
        "solarsystem" : ["an ontology for astronomical objects in the solar system", "SolarSystem.json", SOLARSYSTEM_CONTEXT],
        "engineering": ["an ontology for engineering concepts", "Engineering.json", ENGINEERING_CONTEXT],
        "spacecraft": ["an ontology for a spacecraft and its systems", "Spacecraft.json", SPACECRAFT_CONTEXT],
        "subsystems": ["an ontology for subsystems in a spacecraft", "SubSystems.json", SUBSYSTEMS_CONTEXT],
        "exploration": ["an ontology for space exploration and mission design", "Exploration.json", SUBSYSTEMS_CONTEXT]
    }

)