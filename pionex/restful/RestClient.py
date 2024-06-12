from pionex.internal.generate_signature import rest_signature

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
            self.session.headers.add({ ?
                'PIONEX-KEY':key
            })

    def _send_request(self, http_method, url_path, **params):
        #TODO
        #remove None params, possibly handle list[] params?
        url = self.base_url + url_path

        params = {'url': url}

        timestamp = str(int(time.time() * 1000))

        params['timestamp'] = timestamp

        signature = rest_signature(self.secret, http_method, url_path, timestamp, params, data)

        self.session.headers.addonlyonce / modify({
                'PIONEX-SIGNATURE':signature
            })

        #TODO optional timeout
            'timeout': self.timeout,
            
        methods = {
            'GET': self.session.get,
            'DELETE': self.session.delete,
            'PUT': self.session.put,
            'POST': self.session.post,
        }
        return methods[http_method](**params)