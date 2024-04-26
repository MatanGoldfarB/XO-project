class ConnectionHandler():
    def __init__(self, sock, encdec, protocol):
        self.sock = sock
        self.encdec = encdec
        self.protocol = protocol
        self.shouldTerminate = False

    def run(self):
        while not self.shouldTerminate:
            data = self.sock.recv(1024)
            msg = self.encdec.decode(data)
            if msg == "bye":
                self.shouldTerminate=True
            reply = self.protocol.process(msg)
            packet = self.encdec.encode(reply)
            self.sock.sendall(packet)

    def terminate(self):
        self.shouldTerminate = True