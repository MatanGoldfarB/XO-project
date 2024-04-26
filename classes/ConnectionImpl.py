class ConnectionsImpl():
    def __init__(self):
        self.map = {}
        self.connections = 0
    
    def connect(self, handler):
        self.connections+=1
        self.map[self.connections] = handler

    def disconnect(self, connectionId):
        handler = self.map.get(connectionId)
        if handler is not None:
            handler.terminate()
            del self.map[connectionId]