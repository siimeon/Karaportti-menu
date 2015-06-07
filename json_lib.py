import json

def obj_to_json(obj):
    return json.dumps(obj, indent=4, sort_keys=True)

def json_to_obj(json_str):
    return json.loads(json_str)