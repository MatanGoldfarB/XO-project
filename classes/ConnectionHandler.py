from abc import ABC

class ConnectionHandler(ABC):
    def __init__(self, sock, encdec, protocol):
        self.sock = sock
        self.encdec = encdec
        self.protocol = protocol

    def run(self):
        data = b''
        while True:
            chunk = self.sock.recv(1024)
            if not chunk:
                break
            data += chunk
        msg = self.encdec.decode(data)
        self.protocol.process(msg)