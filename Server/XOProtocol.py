import sys
sys.path.insert(1, "/Users/matangoldfarb/Desktop/My_Projects/XO/classes")

from classes.MessagingProtocol import MessagingProtocol

class XOProtocol(MessagingProtocol):
    def start(self, board, playerNum):
        self.shouldTerminate = False
        self.name = ""
        self.board = board
        self.playerNum = playerNum

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
            if msg.isdigit():
                self.board.set_pick(self.playerNum, int(msg))
        self.board.print()
        if self.shouldTerminate:
            return "0"
        return "1"

    
    def setName(self,name):
        self.name = name

    def shouldTerminate(self):
        return self.shouldTerminate

    def get(self):
        return XOProtocol()
