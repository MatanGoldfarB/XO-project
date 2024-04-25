import sys
sys.path.insert(1, "/Users/matangoldfarb/Desktop/My_Projects/XO")

from classes.ThreadPerClientServer import ThreadPerClientServer
from Server.XOEncDec import XOEncDec
from Server.XOProtocol import XOProtocol

prot = XOProtocol()
encdec = XOEncDec()
server = ThreadPerClientServer(9999, prot, encdec)
server.serve()