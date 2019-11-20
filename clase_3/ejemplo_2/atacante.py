from abc import ABC, abstractmethod


class Atacante(ABC):
    @abstractmethod
    def atacar(self, objetivo):
        pass