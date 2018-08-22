import json
import hashlib
import urllib
import hmac


class Utils(object):
    def __init__(self):
        pass

    @staticmethod
    def to_json(data):
        return json.loads(data.text)

    @staticmethod
    def hash_request(secret, params):
        params_encoded = urllib.urlencode(params)

        return hmac.new(secret.encode('utf-8'),
                        params_encoded.encode('utf-8'),
                        hashlib.sha256).hexdigest()
