import socket, time
import sys
sys.path.insert(1, "/Users/matangoldfarb/Desktop/My_Projects/XO")
from Client.XOEncDec import XOEncDec
from Client.XOProtocol import XOProtocol

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 9999)

clientSock.connect(server_address)
encdec = XOEncDec()
terminate = False

try:
        while not terminate:
            message = input("please enter a msg: ")
            clientSock.sendall(encdec.encode(message))
            data = clientSock.recv(1024)
            reply = encdec.decode(data)
            print("client recieved back "+reply)
            if reply == "0":
                terminate = True
finally:
    clientSock.close()
