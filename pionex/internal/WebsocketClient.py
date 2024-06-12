import threading
import logging
import json
import time
from typing import Callable
from websocket import (
    ABNF,
    create_connection,
    WebSocketException,
    WebSocketConnectionClosedException,
    WebSocketTimeoutException,
)

class WebsocketClient(threading.Thread):
    """
    implements thread to run websocket send and recv
    - handles opening and closing
    - handles heartbeat ping/pong
    - callback on_message()
    - send individual message
    """
    def __init__(self, url, on_message:Callable[[dict], any]):
        threading.Thread.__init__(self)
        self.logger = logging.getLogger(__name__)
        self.on_message = on_message
        self.create_ws_connection(url)

    def create_ws_connection(self, url:str):
        self.ws = create_connection(url)
        self.logger.debug(f"WebSocket connection has been established to: {url}",)

    def run(self):
        self._read_data()

    def send_message(self, message: dict):
        message = json.dumps(message, separators=(', ', ': '))
        self.logger.debug(f"Sending message to Pionex: {message}")
        self.ws.send(message)

    def _read_data(self):
        while True:
            try:
                op_code, frame = self.ws.recv_data_frame(True)
                self.logger.debug(f"received message: {frame.data.decode('utf-8')}")
            except WebSocketException as e:
                if isinstance(e, WebSocketConnectionClosedException):
                    self.logger.error("Unexpected websocket close connection")
                elif isinstance(e, WebSocketTimeoutException):
                    self.logger.error("Websocket connection timeout")
                else:
                    self.logger.error(f"Websocket exception: {e}")
                raise e
            except Exception as e:
                self.logger.error(f"Exception in read_data: {e}")
                raise e

            if op_code == ABNF.OPCODE_PING:
                self.ws.pong("")

            if op_code == ABNF.OPCODE_BINARY:
                data = json.loads(frame.data)
                if 'op' in data:
                    if data['op'] == 'PING':
                        pass
                        self._pong()
                    elif data['op'] == 'CLOSE':
                        if 'note' in data:
                            if data['note'] == 'closed by yourself':
                                break
                        self.logger.warning("forced op:CLOSE by server")
                        break
                else:
                    self.on_message(data)

    def _pong(self):
        ms_timestamp = int(time.time() * 1000)
        message = {'op':'PONG','timestamp':ms_timestamp}
        self.send_message(message)

    def close(self):
        if not self.ws.connected:
            self.logger.warning("Websocket already closed")
        else:
            self.ws.send_close()
            self.logger.debug("Closing connection")
        return