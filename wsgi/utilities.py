import simplejson as json


def check_type_in_list(listed_types, looking_for):
    """ checks if the object is type class or property """
    if looking_for == 'property':
        look_for = "http://www.w3.org/2002/07/owl#ObjectProperty"
    elif looking_for == 'class':
        look_for = "http://www.w3.org/2002/07/owl#Class"
    else:
        raise BadAttribute('Wrong looking_for parameter')
    
    for lst in listed_types:
        if isinstance(lst, dict):
            if lst['@id'] == look_for:
                return True
        else:
            if look_for in lst:
                return True

def classes_and_properties(defines):
    """ create two arrays for properties and classes """
    classes, properties = [], []
    for c in defines:
        # check @type
        label = None
        if 'rdfs:label' in c.keys():
            label = c['rdfs:label']
        else:
            if 'skos:prefLabel' in c.keys():
                label = c['skos:prefLabel']
            elif 'skos:altLabel' in c.keys():
                label = c['skos:altLabel']

        if label is None:
            raise ValueError(str(c))

        if isinstance(c['@type'], list):
            if check_type_in_list(c['@type'], 'property'):
                properties.append({ "label": label, "dump": json.dumps(c, indent=2) })
                continue
            elif check_type_in_list(c['@type'], 'class'):
                classes.append({ "label": label, "dump": json.dumps(c, indent=2) })
                continue
            else:
                classes.append({ "label": label, "dump": json.dumps(c, indent=2) })
                continue
        else:
            if "http://www.w3.org/2002/07/owl#ObjectProperty" in c['@type']:
                properties.append({ "label": label, "dump": json.dumps(c, indent=2) })
                continue
            elif "http://www.w3.org/2002/07/owl#Class" in c['@type']:
                classes.append({ "label": label, "dump": json.dumps(c, indent=2) })
                continue
            else:
                classes.append({ "label": label, "dump": json.dumps(c, indent=2) })
                continue
    return classes, properties


