from pionex_api.pionex.websocket.PionexWebsocketClient import PionexWebsocketClient
from pionex_api.pionex.signature.generate_signature import generate_WEBSOCKET_signature
from typing import Callable

import time

class PrivateStream:
    """
    Wrapper to subscribe to multiple pionex private websocket streams
    and assign individual callbacks for each (topic, symbol) pair
    """
    def __init__(self, api_key:str, api_secret:str):
        timestamp = str(int(time.time() * 1000))
        signature = generate_WEBSOCKET_signature(api_key, api_secret, timestamp)
        url = f"wss://ws.pionex.com/ws?key={api_key}&timestamp={timestamp}&signature={signature}"
        self.ws_client = PionexWebsocketClient(url, self._on_message)
        self.ws_client.start()
        self.topic_symbol_callbacks = {}

    def _on_message(self, message:str):
        topic, symbol = message['topic'], message['symbol']
        if (topic, symbol) in self.topic_symbol_callbacks:
            self.topic_symbol_callbacks[(topic, symbol)](message['data'])

    def subscribe(self, on_message:Callable, topic:str, symbol:str = None, ):
        message = {
            'op': "SUBSCRIBE",
            'topic': topic
        }
        if symbol != None:
            message['symbol'] = symbol
        self.ws.send_message(message)
        self.topic_symbol_callbacks[(topic, symbol)] = on_message

    def unsubscribe(self, topic:str, symbol:str=None):
        message = {
            'op': "UNSUBSCRIBE",
            'topic': topic
        }
        if symbol != None:
            message['symbol'] = symbol
        self.ws.send_message(message)
