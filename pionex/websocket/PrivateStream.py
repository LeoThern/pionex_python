from pionex_api.pionex.websocket.PionexWebsocketClient import PionexWebsocketClient
from pionex_api.pionex.signature.pionex_signature import generate_WEBSOCKET_signature

import time

class PrivateStream:
    """
    Interface to subscribe to individual pionex private websocket streams
    and assign callbacks on messages
    """
    def __init__(self, api_key, api_secret):
        timestamp = str(int(time.time() * 1000))
        signature = generate_WEBSOCKET_signature(api_key, api_secret, timestamp)
        url = f"wss://ws.pionex.com/ws?key={api_key}&timestamp{timestamp}&signature{signature}"
        self.ws_client = PionexWebsocketClient(url, self._on_message)
        self.ws_client.start()

    def _on_message(self, message):
        pass

    def subscribe(self, topic, on_message):
        pass

    def unsubscribe(self, topic):
        pass
