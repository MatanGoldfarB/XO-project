import sys
sys.path.insert(1, "/Users/matangoldfarb/Desktop/My_Projects/XO/classes")

from classes.MessagingProtocol import MessagingProtocol

class XOProtocol(MessagingProtocol):
    def __init__(self):
        self.shouldTerminate = False

    def process(self, msg):
        print(msg)
    
    def shouldTerminate(self):
        return self.shouldTerminate

    def get(self):
        return XOProtocol()
