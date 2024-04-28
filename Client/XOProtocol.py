import sys
sys.path.insert(1, "/Users/matangoldfarb/Desktop/My_Projects/XO/classes")

from classes.MessagingProtocol import MessagingProtocol

class XOProtocol(MessagingProtocol):
    def __init__(self):
        self.shouldTerminate = False

    def process(self, msg):
        if msg == "name":
            print("please enter your name first")
            return False
        if msg == "terminate":
            return True
        if msg == "error":
            print("please enter a place for your token")
            return False
        if msg.isdigit():
            if msg == "0":
                return False
            print("the winner is: " + msg)
            return True
            

    
    def shouldTerminate(self):
        return self.shouldTerminate

    def get(self):
        return XOProtocol()
