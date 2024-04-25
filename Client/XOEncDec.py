import sys
sys.path.insert(1, "/Users/matangoldfarb/Desktop/My_Projects/XO/classes")

from classes.MessageEncoderDecoder import MessageEncoderDecoder


class XOEncDec(MessageEncoderDecoder):
    def decode(self, message):
        return message.decode()
    
    def encode(self, message):
        return message.encode()

    def get(self):
        return XOEncDec()
