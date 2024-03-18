import json
import hashlib
import hmac
from urllib.parse import urlencode

# Function to generate the PIONEX-SIGNATURE
def generate_REST_signature(api_secret, method, path, timestamp, params=None, data=None):
    # Set query parameters as key-value pairs: key=value
    if params is None:
        params = {}
    params['timestamp'] = timestamp
    query_string = urlencode(sorted(params.items()))

    message = f"{method.upper()}{path}?{query_string}"

    # Concatenate related entity body of POST and DELETE after step 5
    if method.upper() == 'POST' and data is not None:
        message += json.dumps(data, separators=(', ', ': '))

    # Use API Secret and the above result to generate HMAC SHA256 code, then convert it to hexadecimal
    signature = hmac.new(api_secret.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()

    return signature

# Function to generate the PIONEX-SIGNATURE
def generate_WEBSOCKET_signature(api_key, api_secret, timestamp):
    params = {
        'key':api_key,
        'timestamp':timestamp
    }
    query_string = urlencode(sorted(params.items()))
    message = f"/ws?{query_string}websocket_auth"

    # Use API Secret and the above result to generate HMAC SHA256 code, then convert it to hexadecimal
    signature = hmac.new(api_secret.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()

    return signature