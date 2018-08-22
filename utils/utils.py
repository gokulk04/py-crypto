import json


class Utils(object):
    def __init__(self):
        pass

    @staticmethod
    def to_json(data):
        return json.loads(data.text)
