from pionex_api.pionex.websocket.PionexWebsocketClient import PionexWebsocketClient

class PublicStream:
    """
    Interface to subscribe to individual pionex public websocket streams
    and assign callbacks on messages
    """
    def __init__(self, api_key, api_secret):
        self.ws_client = PionexWebsocketClient("wss://ws.pionex.com/wsPub", self._on_message)
        self.ws_client.start()

    def subscribe(self, topic, on_message, symbol=None):
        pass

    def unsubscribe(self, topic):
        pass