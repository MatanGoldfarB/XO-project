from abc import ABC, abstractmethod

class MessagingProtocol(ABC):
    @abstractmethod
    def process(self, msg):
        pass
    
    @abstractmethod
    def shouldTerminate(self):
        pass

    @abstractmethod
    def get(self):
        pass