from pionex.websocket.PionexWebsocketClient import PionexWebsocketClient

from typing import Callable
import time

class PublicStream:
    """
    Calls to subscribe to multiple pionex public websocket streams
    and assign individual callbacks for each (topic, symbol) pair
    """
    def __init__(self):
        self.ws_client = self.initialize_client()
        self.ws_client.start()
        self.topic_symbol_callbacks = {}

    def initialize_client(self):
        return PionexWebsocketClient("wss://ws.pionex.com/wsPub", self._on_message)

    def _on_message(self, message:dict):
        if 'code' in message:
            pass
            #handle / throw exceptions
        topic = None
        if 'topic' in message:
            topic = message['topic']
        symbol = None
        if 'symbol' in message:
            symbol = message['symbol']
        if (topic, symbol) in self.topic_symbol_callbacks:
            if 'data' in message:
                self.topic_symbol_callbacks[(topic, symbol)](message['data'])

    def subscribe(self, callback:Callable[[dict], any], topic:str, symbol:str = None, limit:int = None):
        message = {
            'op': "SUBSCRIBE",
            'topic': topic
        }
        if symbol != None:
            message['symbol'] = symbol
        if limit != None:
            message['limit'] = limit
        self.ws_client.send_message(message)
        self.topic_symbol_callbacks[(topic, symbol)] = callback

    def unsubscribe(self, topic:str, symbol:str=None):
        message = {
            'op': "UNSUBSCRIBE",
            'topic': topic
        }
        if symbol != None:
            message['symbol'] = symbol
        self.ws_client.send_message(message)

    def __del__(self):
        self.ws_client.close()
