import sys
sys.path.insert(1, "/Users/matangoldfarb/Desktop/My_Projects/XO/classes")

from classes.MessagingProtocol import MessagingProtocol

class XOProtocol(MessagingProtocol):
    def start(self, board, connections, connectionId):
        self.shouldTerminate = False
        self.name = ""
        self.board = board
        self.connections = connections
        self.connectionId = connectionId

    def process(self, msg):
        if self.name == "":
            if not msg.isdigit():
                self.setName(msg)
                if self.connections.getNumConnections() == 2:
                    if self.connectionId == 1:
                        self.connections.send(2, "0")
                    else:
                        self.connections.send(1, "0")
                return
            else:
                self.connections.send(self.connectionId, "name")
                return
        else:
            if msg == "bye":
                self.shouldTerminate=True
                self.connections.send(1, "terminate")
                self.connections.send(2, "terminate")
                return
            if self.connections.getNumConnections() != 2:
                return
            if msg.isdigit():
                self.board.set_pick(self.connectionId, int(msg))
                self.board.print()
                print("+++++++++++++++++++")
                winner = self.board.checkBoard()
                self.shouldTerminate = winner != 0
            else:
                self.connections.send(self.connectionId, "error")
                return
        if self.shouldTerminate:
            self.connections.send(1, str(winner))
            self.connections.send(2, str(winner))
            self.connections.reset()
            self.board.clear()
        else:
            if self.connectionId == 1:
                self.connections.send(2, "0")
            else:
                self.connections.send(1, "0")

    
    def setName(self,name):
        self.name = name

    def shouldTerminate(self):
        return self.shouldTerminate

    def get(self):
        return XOProtocol()
