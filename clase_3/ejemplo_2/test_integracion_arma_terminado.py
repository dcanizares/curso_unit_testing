import unittest
from unittest.mock import Mock

from arma import Arma
from escudo import Escudo
from fauno import Fauno

class IntegracionArmaTestCase(unittest.TestCase):
    def setUp(self):
        self.arma = Arma()
        self.escudo = Escudo()
        self.fauno = Fauno()

    def test_arma_ataca_escudo_y_reduce_resistencia(self):
        self.arma.atacar(self.escudo)

        self.assertEqual(4, self.escudo.resistencia)

    def test_arma_ataca_escudo_sin_resistencia(self):
        self.arma.atacar(self.escudo)
        self.arma.atacar(self.escudo)
        self.arma.atacar(self.escudo)
        self.arma.atacar(self.escudo)
        self.arma.atacar(self.escudo)

        with self.assertRaises(ValueError) as contexto:
            self.arma.atacar(self.escudo)

        self.assertEqual("¡El objetivo ya no puede recibir ataques!", str(contexto.exception))
        self.assertEqual(0, self.escudo.resistencia)

    def test_arma_ataca_fauno_con_escudo_y_no_reduce_resistencia(self):
        resistencia_inicial = self.fauno.resistencia
        self.arma.atacar(self.fauno)

        self.assertEqual(resistencia_inicial, self.fauno.resistencia)

    def test_arma_ataca_fauno_con_escudo_vencido_y_reduce_resistencia(self):
        for _ in range(5):
            self.arma.atacar(self.fauno)

        self.arma.atacar(self.fauno)

        self.assertEqual(90, self.fauno.resistencia)

    def test_arma_ataca_fauno_sin_resistencia(self):
        for _ in range(15):
            self.arma.atacar(self.fauno)

        with self.assertRaises(ValueError) as contexto:
            self.arma.atacar(self.fauno)

        self.assertEqual("¡El objetivo ya no puede recibir ataques!", str(contexto.exception))


if __name__ == '__main__':
    unittest.main(verbosity=2)
