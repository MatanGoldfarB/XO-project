import socket
import sys
sys.path.insert(1, "/Users/matangoldfarb/Desktop/My_Projects/XO")

from Client.XOEncDec import XOEncDec
from Client.XOProtocol import XOProtocol

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 9999)

clientSock.connect(server_address)
encdec = XOEncDec()

try:
    message = input("please enter a msg: ")
    clientSock.sendall(encdec.encode(message))
finally:
    clientSock.close()
