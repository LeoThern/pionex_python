import time
from typing import Callable

from pionex.signature.generate_signature import generate_WEBSOCKET_signature
from pionex.websocket.PublicStream import PublicStream
from pionex.websocket.PionexWebsocketClient import PionexWebsocketClient


class PrivateStream(PublicStream):
    def __init__(self, api_key:str, api_secret:str):
        self.key_secret = (api_key, api_secret)
        super().__init__()

    def initialize_client(self):
        key, secret = self.key_secret
        timestamp = str(int(time.time() * 1000))
        signature = generate_WEBSOCKET_signature(key, secret, timestamp)
        url = f"wss://ws.pionex.com/ws?key={key}&timestamp={timestamp}&signature={signature}"
        return PionexWebsocketClient(url, self._on_message)
