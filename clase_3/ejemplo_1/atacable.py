from abc import ABC, abstractmethod


class Atacable(ABC):
    @abstractmethod
    def recibir_ataque(self, potencia):
        pass

    @property
    @abstractmethod
    def resistencia(self):
        pass

    def _validar_resistencia(self):
        if self._resistencia == 0:
            raise ValueError("¡El objetivo ya no puede recibir ataques!")