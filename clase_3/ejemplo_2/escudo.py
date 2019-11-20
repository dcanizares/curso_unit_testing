from atacable import Atacable


class Escudo(Atacable):
    def __init__(self):
        self._resistencia = 5

    def recibir_ataque(self, potencia=0):
        self._validar_resistencia()

        self._resistencia -= 1