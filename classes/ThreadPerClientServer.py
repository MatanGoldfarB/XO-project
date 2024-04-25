import sys
sys.path.insert(1, "/Users/matangoldfarb/Desktop/My_Projects/XO/classes")

from BaseServer import BaseServer
import threading

class ThreadPerClientServer(BaseServer):
    def __init__(self, port, protocolFactory, encdecFactory):
        super().__init__(port, protocolFactory, encdecFactory)

    def execute(self, handler):
        threading.Thread(target=handler.run).start()