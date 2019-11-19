import unittest

from escudo import Escudo

class EscudoTestCase(unittest.TestCase):
    """
    ==========================================================================
    Casos de prueba detectados
    ==========================================================================

    Escenario: un escudo es atacable

    Dado que existe un escudo

    Cuando un escudo recibe ataque

    Entonces no hay error
    --------------------------------------------------------------------------
    Escenario: un escudo tiene una resistencia predeterminada de 5

    Dado que existe un escudo

    Cuando se crea un escudo

    Entonces el escudo tiene una resistencia de 5
    --------------------------------------------------------------------------
    Escenario: un escudo tiene una resistencia de 4 si es atacado solo una vez

    Dado que existe un escudo

    Cuando el escudo recibe un ataque

    Entonces el escudo pasa a tener una resistencia de 4
    --------------------------------------------------------------------------
    Escenario: un escudo se queda sin resistencia al recibir 5 ataques

    Dado que existe un escudo

    Cuando el escudo recibe 5 ataques

    Entonces el escudo pasa a tener una resistencia de 0
    --------------------------------------------------------------------------
    Escenario: un escudo sin resistencia no puede recibir ataques

    Dado que existe un escudo

    Cuando el escudo ya recibió 5 ataques
        Y se intenta un sexto ataque

    Entonces se recibe un ValueError con el mensaje '¡El objetivo ya no puede recibir ataques!'
    """
    def setUp(self):
        self.escudo = Escudo()

    def test_escudo_es_atacable(self):
        self.escudo.recibir_ataque()

    def test_escudo_inicia_con_resistencia_5(self):
        self.assertEqual(5, self.escudo.resistencia)

    def test_escudo_tiene_resistencia_4_al_recibir_ataque(self):
        self.escudo.recibir_ataque()

        self.assertEqual(4, self.escudo.resistencia)

    def test_escudo_tiene_0_al_recibir_5_ataques(self):
        for _ in range(5):
            self.escudo.recibir_ataque()

        self.assertEqual(0, self.escudo.resistencia)

    def test_escudo_en_0_arroja_value_error_al_recibir_ataque(self):
        for _ in range(5):
            self.escudo.recibir_ataque()

        with self.assertRaises(ValueError) as contexto:
            self.escudo.recibir_ataque()

        self.assertEqual("¡El objetivo ya no puede recibir ataques!", str(contexto.exception))


if __name__ == '__main__':
    unittest.main(verbosity=2)
