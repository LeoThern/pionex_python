from pionex_python.internal.generate_signature import ws_signature
from pionex_python.internal.WebsocketClient import WebsocketClient

from pionex_python.websocket.PublicStream import PublicStream

import time

class PrivateStream(PublicStream):
    """
    Extends PublicStream with authentication
    """
    def __init__(self, api_key:str, api_secret:str):
        self.key_secret = (api_key, api_secret)
        super().__init__()

    def initialize_client(self):
        key, secret = self.key_secret
        timestamp = str(int(time.time() * 1000))
        signature = ws_signature(key, secret, timestamp)
        url = f"wss://ws.pionex_python.com/ws?key={key}&timestamp={timestamp}&signature={signature}"
        return WebsocketClient(url, self._on_message)
