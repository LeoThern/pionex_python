from pionex.internal.generate_signature import rest_signature
from pionex import __version__

import requests
import time

class RestClient:
    def __init__(self, key:str=None, secret:str=None):
        self.base_url = 'https://api.pionex.com/'
        self.key = key
        self.secret = secret
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': f'pionex-python/{__version__}',
            'Content-Type': 'application/json;charset=utf-8',
        })
        if key:
            self.session.headers.update({
                'PIONEX-KEY':key
            })

    def _send_request(self, http_method, url_path, **params):
        url = self.base_url + url_path
        params = {k: v for k, v in params.items() if v is not None}  # Remove None params

        timestamp = str(int(time.time() * 1000))
        params['timestamp'] = timestamp

        if 'data' in params:
            data = params['data']
            del params['data']
        else:
            data = None

        if self.key:
            signature = rest_signature(self.secret, http_method, url_path, timestamp, params, data)
            self.session.headers.update({
                'PIONEX-KEY': self.key,
                'PIONEX-SIGNATURE': signature
            })

        methods = {
            'GET': self.session.get,
            'DELETE': self.session.delete,
            'PUT': self.session.put,
            'POST': self.session.post,
        }

        response = methods[http_method](url, params=params, json=data)
        return response.text
