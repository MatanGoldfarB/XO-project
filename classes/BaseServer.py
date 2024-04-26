from abc import ABC, abstractmethod
import socket
from classes.ConnectionHandler import ConnectionHandler
from classes.ConnectionImpl import ConnectionsImpl


class BaseServer(ABC):
    def __init__(self, port, protocolFactory, encdecFactory):
        self.port = port
        self.protocolFactory = protocolFactory
        self.encdecFactory = encdecFactory
        self.running = True
        self.connectios = ConnectionsImpl()

    @abstractmethod
    def execute(self, handler):
        pass

    def serve(self):
        serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', self.port)
        serverSock.bind(server_address)
        serverSock.listen(2)
        while(self.running):
            clientSock, clientAddress = serverSock.accept()
            encdec = self.encdecFactory.get()
            prot = self.protocolFactory.get()
            handler = ConnectionHandler(clientSock, encdec, prot)
            self.connectios.connect(handler)
            self.execute(handler)

    def terminate(self):
        self.running = False