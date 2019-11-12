class Calculadora:
    def __init__(self, limite_inferior, limite_superior):
        self.__limite_inferior = limite_inferior
        self.__limite_superior = limite_superior

    @property
    def limite_inferior(self):
        return self.__limite_inferior

    @property
    def limite_superior(self):
        return self.__limite_superior

    def sumar(self, x, y):
        self.validar_argumentos(x, y)

        resultado = x + y

        if resultado > self.__limite_superior:
            raise ValueError("Se superó el límite superior")

        return resultado

    def restar(self, x, y):
        self.validar_argumentos(x, y)

        resultado = x - y

        if resultado < self.__limite_inferior:
            raise ValueError("Se superó el límite inferior")

        return resultado

    def dividir(self, x, y):
        if x % y != 0:
            raise ValueError("La división debe ser entera")
        else:
            return x / y

    def multiplicar(self, x, y):
        self.validar_argumentos(x, y)

        resultado = x * y

        if resultado < self.__limite_inferior:
            raise ValueError("Se superó el límite inferior")

        if resultado > self.__limite_superior:
            raise ValueError("Se superó el límite superior")

        return resultado

    def validar_argumentos(self, x, y):
        if x < self.__limite_inferior:
            raise ValueError("Primer parámetro supera el límite inferior")

        if y < self.__limite_inferior:
            raise ValueError("Segundo parámetro supera el límite inferior")

        if x > self.__limite_superior:
            raise ValueError("Primer parámetro supera el límite superior")

        if y > self.__limite_superior:
            raise ValueError("Segundo parámetro supera el límite superior")
