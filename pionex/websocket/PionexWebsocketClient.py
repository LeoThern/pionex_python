import threading
import logging
from websocket import (
    ABNF,
    create_connection,
    WebSocketException,
    WebSocketConnectionClosedException,
    WebSocketTimeoutException,
)

class PionexWebsocketClient(threading.Thread):
    """
    implements thread to run
    while True: ws.recv_data_frame()
    - handles heardbeat ping/pong
    - callback on_message()
    - send individual message
    """
    def __init__(self, url, on_message, logger=None):
        threading.Thread.__init__(self)
        self.logger = logger
        if self.logger == None:
            self.logger = logging.getLogger(__name__)
        self.on_message = on_message
        self._is_closing_connection = False
        self.create_ws_connection(url)

    def create_ws_connection(self, url):
        self.logger.debug(f"Creating connection with WebSocket Server: {url}")
        self.ws = create_connection(url, timeout=5)
        self.logger.debug(f"WebSocket connection has been established: {url}",)

    def run(self):
        self._read_data()

    def send_message(self, message):
        self.logger.debug(f"Sending message to Pionex Server: {message}")
        self.ws.send(message)

    def _read_data(self):
        data = ""
        while True:
            try:
                op_code, frame = self.ws.recv_data_frame(True)
            except WebSocketException as e:
                if isinstance(e, WebSocketConnectionClosedException):
                    if self._is_closing_connection:
                        break
                    self.logger.error("Lost websocket connection")
                elif isinstance(e, WebSocketTimeoutException):
                    self.logger.error("Websocket connection timeout")
                else:
                    self.logger.error(f"Websocket exception: {e}")
                raise e
            except Exception as e:
                self.logger.error(f"Exception in read_data: {e}")
                raise e

            self._handle_data(op_code, frame, data)
            self._handle_heartbeat(op_code, frame)

            if op_code == ABNF.OPCODE_CLOSE:
                self.logger.warning("CLOSE frame received, closing websocket connection")
                break

    def _handle_heartbeat(self, op_code, frame):
        if op_code == ABNF.OPCODE_PING:
            self.ws.pong("")
            self.logger.debug("Received Ping; PONG frame sent back")
        elif op_code == ABNF.OPCODE_PONG:
            self.logger.debug("Received PONG frame ?")

    def _handle_data(self, op_code, frame, data):
        if op_code == ABNF.OPCODE_TEXT:
            data = frame.data.decode("utf-8")
            self.on_message(data)

    def close(self):
        if not self.ws.connected:
            self.logger.warning("Websocket already closed")
        else:
            self._is_closing_connection = True
            self.ws.send_close()
            self.logger.debug("Closing connection")
        return