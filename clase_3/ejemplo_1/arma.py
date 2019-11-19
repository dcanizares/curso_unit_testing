from atacante import Atacante


class Arma(Atacante):
    def __init__(self, potencia=10):
        self.__potencia = potencia

    @property
    def potencia(self):
        return self.__potencia

    def atacar(self, objetivo):
        try:
            objetivo.recibir_ataque(self.__potencia)
        except AttributeError:
            raise NotImplementedError()