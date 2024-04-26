from classes.BaseServer import BaseServer
from Server.Board import Board
import threading

class ThreadPerClientServer(BaseServer):
    def __init__(self, prot, protocolFactory, encdecFactory):
        super().__init__(prot, protocolFactory, encdecFactory)
        self.board = Board()

    def execute(self, handler):
        handler.protocol.start(self.board, self.connectios, self.connectios.connections)
        threading.Thread(target=handler.run).start()