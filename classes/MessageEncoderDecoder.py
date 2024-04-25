from abc import ABC, abstractmethod

class MessageEncoderDecoder(ABC):
    @abstractmethod
    def decode(self, message):
        pass
    
    @abstractmethod
    def encode(self, message):
        pass

    @abstractmethod
    def get(self):
        pass