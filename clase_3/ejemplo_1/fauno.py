from atacable import Atacable
from atacante import Atacante

from arma import Arma
from escudo import Escudo


class Fauno(Atacable, Atacante):
    def __init__(self, resistencia=100):
        self._resistencia = resistencia
        self.__escudo = Escudo()
        self.__arma = Arma()

    def atacar(self, objetivo):
        self.__arma.atacar(objetivo)

    def recibir_ataque(self, potencia):
        self._validar_resistencia()

        try:
            self.__escudo.recibir_ataque()
        except ValueError:
            if self._resistencia - potencia > 0:
                self._resistencia -= potencia
            else:
                self._resistencia = 0
