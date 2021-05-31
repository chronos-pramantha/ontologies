__author__ = 'lorenzo'

#
# Contexts for single objects and properties. Full ontology contexts are in the files
#


CHRONOS_CONTEXT = dict(
    {
        "rdf"    : "https://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "skos"   : "https://www.w3.org/2004/02/skos/core#",
        "schema" : "http://schema.org/",
        "dbpedia": "http://dbpedia.org/property/",
        "owl"    : "https://www.w3.org/2002/07/owl#",
        "chronos": "https://ontologies.pramantha.net/chronos/",
        "@base"  : "https://ontologies.pramantha.net/chronos",
        "defines": {
            "@reverse": "rdfs:isDefinedBy"
        }
    }
)

SENSORS_CONTEXT = dict(
    {
        "rdf"    : "https://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "skos"   : "https://www.w3.org/2004/02/skos/core#",
        "schema" : "http://schema.org/",
        "dbpedia": "http://dbpedia.org/property/",
        "owl"    : "https://www.w3.org/2002/07/owl#",
        "sensor" : "https://ontologies.pramantha.net/sensors/",
        "chronos": "https://ontologies.pramantha.net/chronos/",
        "@base"  : "https://ontologies.pramantha.net/sensors",
        "defines": {
            "@reverse": "https://www.w3.org/2000/01/rdf-schema#isDefinedBy"
        }
    }
)

ASTRONOMY_CONTEXT = dict(
    {
        "@base"    : "https://ontologies.pramantha.net/astronomy",
        "astronomy": "https://ontologies.pramantha.net/astronomy/",
        "schema"   : "https://schema.org/",
        "skos"     : "https://www.w3.org/2004/02/skos/core#",
        "rdf"      : "https://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs"     : "https://www.w3.org/2000/01/rdf-schema#",
        "owl"      : "https://www.w3.org/2002/07/owl#",
        "chronos": "https://ontologies.pramantha.net/chronos/",
        "dbpedia"  : "http://dbpedia.org/ontology/",
        "defines": {
            "@reverse": "https://www.w3.org/2000/01/rdf-schema#isDefinedBy"
        }
    }
)

ENGINEERING_CONTEXT = dict(
    {
        "@base"      : "https://ontologies.pramantha.net/engineering",
        "engineering": "https://ontologies.pramantha.net/engineering/",
        "schema"     : "https://schema.org/",
        "skos"       : "https://www.w3.org/2004/02/skos/core#",
        "rdf"        : "https://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs"       : "https://www.w3.org/2000/01/rdf-schema#",
        "owl"        : "https://www.w3.org/2002/07/owl#",
        "dbpedia"    : "http://dbpedia.org/ontology/",
        "defines": {
            "@reverse": "https://www.w3.org/2000/01/rdf-schema#isDefinedBy"
        }
    }
)

SPACECRAFT_CONTEXT = dict(
    {
        "engineering": "https://ontologies.pramantha.net/engineering/",
        "@base": "https://ontologies.pramantha.net/spacecraft",
        "spacecraft": "https://ontologies.pramantha.net/spacecraft/",
        "schema": "https://schema.org/",
        "skos": "https://www.w3.org/2004/02/skos/core#",
        "rdf": "https://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "https://www.w3.org/2000/01/rdf-schema#",
        "owl": "https://www.w3.org/2002/07/owl#",
        "chronos": "https://ontologies.pramantha.net/chronos/",
        "dbpedia": "http://dbpedia.org/ontology/",
        "defines": {
            "@reverse": "https://www.w3.org/2000/01/rdf-schema#isDefinedBy"
        }
    }
)

SUBSYSTEMS_CONTEXT = dict(
    {
        "@base": "https://ontologies.pramantha.net/subsystems",
        "spacecraft": "https://ontologies.pramantha.net/spacecraft/",
        "subsystems": "https://ontologies.pramantha.net/subsystems/",
        "skos": "https://www.w3.org/2004/02/skos/core#",
        "rdf": "https://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "https://www.w3.org/2000/01/rdf-schema#",
        "owl": "https://www.w3.org/2002/07/owl#",
        "dbpedia": "http://dbpedia.org/ontology/",
        "chronos": "https://ontologies.pramantha.net/chronos/",
        "xml": "https://www.w3.org/2001/XMLSchema#",
        "defines": {
            "@reverse": "https://www.w3.org/2000/01/rdf-schema#isDefinedBy"
        }
    }
)

SOLARSYSTEM_CONTEXT = dict(
    {
        "@base"    : "https://ontologies.pramantha.net/solarsystem",
        "astronomy": "https://ontologies.pramantha.net/astronomy/",
        "rdf"      : "https://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs"     : "https://www.w3.org/2000/01/rdf-schema#",
        "owl"      : "https://www.w3.org/2002/07/owl#",
        "chronos": "https://ontologies.pramantha.net/chronos/",
        "defines": {
            "@reverse": "https://www.w3.org/2000/01/rdf-schema#isDefinedBy"
        }
    }
)

EXPLORATION_CONTEXT = dict(
    {
        "@base": "https://ontologies.pramantha.net/exploration",
        "exploration": "https://ontologies.pramantha.net/exploration/",
        "schema": "https://schema.org/",
        "skos": "https://www.w3.org/2004/02/skos/core#",
        "rdf": "https://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "https://www.w3.org/2000/01/rdf-schema#",
        "chronos": "https://ontologies.pramantha.net/chronos/",
        "owl": "https://www.w3.org/2002/07/owl#",
        "dbpedia": "http://dbpedia.org/ontology/",
        "cyc": "http://sw.opencyc.org/2012/05/10/concept/en/",
        "defines": {
            "@reverse": "https://www.w3.org/2000/01/rdf-schema#isDefinedBy"
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