from abc import ABC, abstractmethod


class Atacable(ABC):
    _resistencia = None

    @abstractmethod
    def recibir_ataque(self, potencia):
        pass

    @property
    def resistencia(self):
        return self._resistencia

    def _validar_resistencia(self):
        if self._resistencia == 0:
            raise ValueError("¡El objetivo ya no puede recibir ataques!")