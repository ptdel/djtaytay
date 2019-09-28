import os
import json

def error(message):
    return json.dumps({"error": message}), 400

def get_parent_path(path):
    return os.path.dirname(path)

def get_complete_path(path, root):
    r = root
    r += "/"
    r += path.lstrip('/')
    return r
