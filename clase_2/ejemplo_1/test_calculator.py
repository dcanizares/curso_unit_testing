import unittest
from calculadora import Calculadora


class Test_Calculadora(unittest.TestCase):
    def test_sumar_5_mas_6_da_11(self):
        calculadora = Calculadora()
        resultado = calculadora.sumar(5, 6)
        self.assertEqual(resultado, 11)

    def test_sumar_7_mas_5_no_da_23(self):
        calculadora = Calculadora()
        resultado = calculadora.sumar(7, 5)
        self.assertNotEqual(resultado, 23)

    def test_restar_3_menos_1_da_2(self):
        calculadora = Calculadora()
        resultado = calculadora.restar(3, 1)
        self.assertEqual(resultado, 2)

    def test_restar_8_menos_5_no_da_88(self):
        calculadora = Calculadora()
        resultado = calculadora.restar(8, 5)
        self.assertNotEqual(resultado, 88)


if __name__ == '__main__':
    unittest.main()
