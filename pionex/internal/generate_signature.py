import json
import hashlib
import hmac
from urllib.parse import urlencode

# generate the PIONEX-SIGNATURE

# https://pionex-doc.gitbook.io/apidocs/restful/general/authentication
def rest_signature(api_secret, method, path, timestamp, params=None, data=None):
    params = params if params else {'timestamp':timestamp}

    query_string = urlencode(sorted(params.items()))
    
    message = f"{method.upper()}{path}?{query_string}"

    if data:
        message += json.dumps(data, separators=(', ', ': '))

    signature = hmac.new(api_secret.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()

    return signature

# https://pionex-doc.gitbook.io/apidocs/websocket/general-info
def ws_signature(api_key, api_secret, timestamp):
    params = {
        'key':api_key,
        'timestamp':timestamp
    }
    query_string = urlencode(sorted(params.items()))
    message = f"/ws?{query_string}websocket_auth"

    signature = hmac.new(api_secret.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()

    return signature