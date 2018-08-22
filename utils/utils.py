import json
import hashlib
import hmac


class Utils(object):
    def __init__(self):
        pass

    @staticmethod
    def to_json(data):
        return json.loads(data.text)

    @staticmethod
    def hash_request(secret, message):
        return hmac.new(secret.encode('utf-8'),
                        message.encode('utf-8'),
                        hashlib.sha256).hexdigest()
