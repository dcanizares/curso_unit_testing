from calculadora import Calculadora


class Programa:
    @classmethod
    def main(cls):
        cls.sumar_5_y_6_da_11()
        cls.sumar_5_y_6_no_da_23()

    @classmethod
    def sumar_5_y_6_da_11(cls):
        calculadora = Calculadora()
        resultado = calculadora.sumar(5, 6)

        if resultado != 16:
            raise ValueError()

    @classmethod
    def sumar_5_y_6_no_da_23(cls):
        calculadora = Calculadora()
        resultado = calculadora.sumar(5, 6)

        if resultado == 11:
            raise ValueError()


Programa.main()
