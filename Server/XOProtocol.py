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
                print("Hello " + self.name)
            else:
                print("Please enter your name first")
        else:
            if msg == "bye":
                self.shouldTerminate=True
                return "-1"
            if msg.isdigit():
                self.board.set_pick(self.connectionId, int(msg))
        self.board.print()
        print("+++++++++++++++++++")
        winner = self.board.checkBoard()
        self.shouldTerminate = winner != 0
        if self.shouldTerminate:
            self.connections.disconnect(1)
            self.connections.disconnect(2)
            self.board.clear()
        return str(winner)

    
    def setName(self,name):
        self.name = name

    def shouldTerminate(self):
        return self.shouldTerminate

    def get(self):
        return XOProtocol()
