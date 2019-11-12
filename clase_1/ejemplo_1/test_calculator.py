import unittest
from calculadora import Calculadora


class Test_Calculadora(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora(-100, 100)

    def test_sumar_2_mas_2_da_4(self):
        """
        Escenario: Sumar 2 más 2 da 4

        Dado que tengo una calculadora
            Y que el límite inferior es -100
            Y que el límite superior es 100

        Cuando sumo 2 más 2

        Entonces el resultado es 4
        """
        resultado = self.calculadora.sumar(2, 2)
        self.assertEqual(4, resultado)

    def test_sumar_5_mas_7_da_12(self):
        """
        Escenario: Sumar 5 más 7 da 12

        Dado que tengo una calculadora
            Y que el límite inferior es -100
            Y que el límite superior es 100

        Cuando sumo 5 más 7

        Entonces el resultado es 12
        """
        self.fail("Test no implementado")

    def test_sumar_es_conmutativa(self):
        """
        Escenario: La suma es conmutativa

        Dado que tengo una calculadora
            Y que el límite inferior es -100
            Y que el límite superior es 100

        Cuando sumo 3 más 5 
            Y  sumo 5 más 3

        Entonces ambos resultados son iguales
        """
        self.fail("Test no implementado")

    def test_sumar_numeros_negativos(self):
        """
        Escenario: La suma de números negativos da por resultado otro número negativo

        Dado que tengo una calculadora
            Y que el límite inferior es -100
            Y que el límite superior es 100

        Cuando sumo -3 y -5

        Entonces el resultado es -8
        """
        self.fail("Test no implementado")

    def test_restar_5_menos_3_da_2(self):
        """
        Escenario: Se realiza una resta en la que el primer valor es mayor que el segundo

        Dado que tengo una calculadora
            Y que el límite inferior es -100
            Y que el límite superior es 100

        Cuando le resto 3 a 5

        Entonces el resultado es 2
        """
        resultado = self.calculadora.restar(5, 3)
        self.assertEqual(2, resultado)

    def test_restar_2_menos_3_da_menos_1(self):
        """
        Escenario: Se realiza una resta en la que el segundo valor es mayor que el primero

        Dado que tengo una calculadora
            Y que el límite inferior es -100
            Y que el límite superior es 100

        Cuando le resto 3 a 2

        Entonces el resultado es -1
        """
        self.fail("Test no implementado")

    def test_restar_no_es_conmutativa(self):
        """
        Escenario: La resta no es conmutativa

        Dado que tengo una calculadora
            Y que el límite inferior es -100
            Y que el límite superior es 100

        Cuando resto 4 menos 2
            Y  resto 2 menos 4

        Entonces los resultados son diferentes
        """
        self.fail("Test no implementado")

    def test_restar_menos_2_y_menos_4_da_2(self):
        """
        Escenario: Se realiza una resta de dos valores negativos

        Dado que tengo una calculadora
            Y que el límite inferior es -100
            Y que el límite superior es 100

        Cuando resto -4 a -2

        Entonces el resultado es 2
        """
        self.fail("Test no implementado")

    def test_dividir_2_por_2_da_1(self):
        """
        Escenario: Se realiza una división entera de dos valores positivos

        Dado que tengo una calculadora
            Y que el límite inferior es -100
            Y que el límite superior es 100

        Cuando divido 2 por 2

        Entonces el resultado es 1
        """
        self.fail("Test no implementado")

    def test_dividir_10_por_5_da_2(self):
        """
        Escenario: Se realiza una división entera de dos valores positivos

        Dado que tengo una calculadora
            Y que el límite inferior es -100
            Y que el límite superior es 100

        Cuando divido 10 por 5

        Entonces el resultado es 2
        """
        self.fail("Test no implementado")

    def test_dividir_10_por_menos_5_da_menos_2(self):
        """
        Escenario: Se realiza una división entera de un positivo por un negativo

        Dado que tengo una calculadora
            Y que el límite inferior es -100
            Y que el límite superior es 100

        Cuando divido 10 por -5

        Entonces el resultado es -2
        """
        self.fail("Test no implementado")

    def test_dividir_3_por_2_arroja_value_error(self):
        """
        Escenario: Se realiza una división no entera

        Dado que tengo una calculadora
            Y que el límite inferior es -100
            Y que el límite superior es 100

        Cuando divido 3 por 2

        Entonces la calculadora arroja un ValueError con el mensaje "La división debe ser entera"
        """
        with self.assertRaises(ValueError) as contexto:
            self.calculadora.dividir(3, 2)
        
        self.assertEqual("La división debe ser entera", str(contexto.exception))

    def test_dividir_3_por_0_arroja_zero_division_error(self):
        """
        Escenario: Se realiza una división por cero

        Dado que tengo una calculadora
            Y que el límite inferior es -100
            Y que el límite superior es 100

        Cuando divido 3 por 0

        Entonces la calculadora arroja un ZeroDivisionError
            Y no importa el mensaje
        """
        self.fail("Test no implementado")

    def test_restar_pasa_limite_inferior_arroja_value_error(self):
        """
        Escenario: La resta arroja por resultado un número más bajo que el límite inferior

        Dado que tengo una calculadora
            Y que el límite inferior es -5
            Y que el límite superior es 5

        Cuando resto 4 a -5

        Entonces la calculadora arroja un ValueError con el mensaje "Se superó el límite inferior"
        """
        self.calculadora = Calculadora(-5, 5)

        with self.assertRaises(ValueError) as contexto:
            self.calculadora.restar(-5, 4)
        
        self.assertEqual("Se superó el límite inferior", str(contexto.exception))

    def test_sumar_pasa_limite_superior_arroja_value_error(self):
        """
        Escenario: La suma arroja por resultado un número más alto que el límite superior

        Dado que tengo una calculadora
            Y que el límite inferior es -5
            Y que el límite superior es 5

        Cuando sumo 5 más 4

        Entonces la calculadora arroja un ValueError con el mensaje "Se superó el límite superior"
        """
        self.fail("Test no implementado")

    def test_multiplicar_2_por_2_da_4(self):
        """
        Escenario: Se realiza una multiplicación de dos valores

        Dado que tengo una calculadora
            Y que el límite inferior es -100
            Y que el límite superior es 100

        Cuando se multiplica 2 por 2

        Entonces el resultado es 4
        """
        resultado = self.calculadora.multiplicar(2, 2)
        self.assertEqual(4, resultado)

    def test_multiplicar_4_por_3_da_12(self):
        """
        Escenario: Se realiza una multiplicación de dos valores

        Dado que tengo una calculadora
            Y que el límite inferior es -100
            Y que el límite superior es 100

        Cuando se multiplica 4 por 3

        Entonces el resultado es 12
        """
        self.fail("Test no implementado")

    def test_multiplicar_es_conmutativa(self):
        """
        Escenario: La multiplicación es conmutativa

        Dado que tengo una calculadora
            Y que el límite inferior es -100
            Y que el límite superior es 100

        Cuando multiplico 3 por 5
            Y  multiplico 5 por 3

        Entonces los resultados son iguales
        """
        self.fail("Test no implementado")

    def test_multiplicar_numeros_negativos(self):
        """
        Escenario: Se realiza una multiplicación de dos valores negativos

        Dado que tengo una calculadora
            Y que el límite inferior es -100
            Y que el límite superior es 100

        Cuando multiplico -3 por -5

        Entonces el resultado es 15
        """
        self.fail("Test no implementado")

    def test_multiplicar_pasa_limite_inferior_arroja_value_error(self):
        """
        Escenario: La multiplicación arroja por resultado un número más bajo que el límite inferior

        Dado que tengo una calculadora
            Y que el límite inferior es -5
            Y que el límite superior es 5

        Cuando multiplico 2 por -3

        Entonces la calculadora arroja un ValueError con el mensaje "Se superó el límite inferior"
        """
        self.fail("Test no implementado")

    def test_multiplicar_pasa_limite_superior_arroja_value_error(self):
        """
        Escenario: La multiplicación arroja por resultado un número más alto que el límite superior

        Dado que tengo una calculadora
            Y que el límite inferior es -5
            Y que el límite superior es 5

        Cuando multiplico 2 por 3

        Entonces la calculadora arroja un ValueError con el mensaje "Se superó el límite superior"
        """
        self.fail("Test no implementado")

    def test_primer_parametro_supera_limite_inferior_arroja_value_error(self):
        """
        Escenario: El primer parámetro es menor que el límite inferior

        Dado que tengo una calculadora
            Y que el límite inferior es -5
            Y que el límite superior es 5

        Cuando el primer parámetro es menor al límite inferior

        Entonces la calculadora arroja un ValueError con el mensaje "Primer parámetro supera el límite inferior"
        """
        self.calculadora = Calculadora(-5, 5)

        with self.assertRaises(ValueError) as contexto:
            self.calculadora.validar_argumentos(-10, 2)
        
        self.assertEqual("Primer parámetro supera el límite inferior", str(contexto.exception))

    def test_segundo_parametro_supera_limite_inferior_arroja_value_error(self):
        """
        Escenario: El segundo parámetro es menor que el límite inferior

        Dado que tengo una calculadora
            Y que el límite inferior es -5
            Y que el límite superior es 5

        Cuando el segundo parámetro es menor al límite inferior

        Entonces la calculadora arroja un ValueError con el mensaje "Segundo parámetro supera el límite inferior"
        """
        self.fail("Test no implementado")

    def test_primer_parametro_supera_limite_superior_arroja_value_error(self):
        """
        Escenario: El primer parámetro es mayor que el límite superior

        Dado que tengo una calculadora
            Y que el límite inferior es -5
            Y que el límite superior es 5

        Cuando el primer parámetro es mayor al límite superior

        Entonces la calculadora arroja un ValueError con el mensaje "Primer parámetro supera el límite superior"
        """
        self.fail("Test no implementado")

    def test_segundo_parametro_supera_limite_superior_arroja_value_error(self):
        """
        Escenario: El segundo parámetro es mayor que el límite superior

        Dado que tengo una calculadora
            Y que el límite inferior es -5
            Y que el límite superior es 5

        Cuando el segundo parámetro es mayor al límite superior

        Entonces la calculadora arroja un ValueError con el mensaje "Segundo parámetro supera el límite superior"
        """
        self.fail("Test no implementado")


if __name__ == '__main__':
    unittest.main()
