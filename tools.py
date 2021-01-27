import json

JSON_PARSE_ERROR = "This is not a validate JSON"

def transformJsonToObject(value):

    value = sanitize_json(value)

    try:
        data = json.loads(value)
    except:
        raise ValueError(JSON_PARSE_ERROR)

    if not data:
        return []

    if isinstance(data, list):
        return [elt["registrant"] for elt in data]
    else:
        return [data["registrant"]]


def sanitize_json(value):
    """Clean json format, to prevent error."""

    # https://stackoverflow.com/questions/39491420/python-jsonexpecting-property-name-enclosed-in-double-quotes
    value = value.replace('\t', '')
    value = value.replace('\n', '')
    value = value.replace(',}', '}')
    value = value.replace(',]', ']')

    return value
