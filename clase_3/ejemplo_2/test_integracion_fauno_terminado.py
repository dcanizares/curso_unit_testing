import unittest
from unittest.mock import Mock, patch

from fauno import Fauno

class IntegracionFaunoTestCase(unittest.TestCase):
    def setUp(self):
        self.fauno = Fauno()
        self.oponente = Fauno()

    def test_fauno_ataca_oponente_con_escudo_vencido_y_reduce_resistencia(self):
        for _ in range(5):
            self.fauno.atacar(self.oponente)

        self.fauno.atacar(self.oponente)

        self.assertEqual(90, self.oponente.resistencia)

    def test_fauno_ataca_oponente_con_escudo_y_no_reduce_resistencia(self):
        resistencia_inicial = self.oponente.resistencia 

        self.fauno.atacar(self.oponente)

        self.assertEqual(resistencia_inicial, self.oponente.resistencia)

    def test_fauno_ataca_oponente_sin_resistencia(self):
        for _ in range(15):
            self.fauno.atacar(self.oponente)

        with self.assertRaises(ValueError) as contexto:
            self.fauno.atacar(self.oponente)

        self.assertEqual("¡El objetivo ya no puede recibir ataques!", str(contexto.exception))
        self.assertEqual(0, self.oponente.resistencia)


if __name__ == '__main__':
    unittest.main(verbosity=2)
