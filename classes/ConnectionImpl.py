class ConnectionsImpl():
    def __init__(self):
        self.map = {}
        self.connections = 0
    
    def connect(self, handler):
        self.connections+=1
        self.map[self.connections] = handler

    def reset(self):
        for connectionId in range(1,self.connections):
            handler = self.map.get(connectionId)
            if handler is not None:
                handler.terminate()
                del self.map[connectionId]
        self.connections=0

    def getNumConnections(self):
        return self.connections
    
    def send(self, connectionId, msg):
        self.map[connectionId].send(msg)