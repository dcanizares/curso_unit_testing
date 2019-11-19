import unittest
from unittest.mock import Mock

from arma import Arma

class ArmaTestCase(unittest.TestCase):
    """
    ==========================================================================
    Casos de prueba detectados
    ==========================================================================

    Escenario: un arma es atacante

    Dado que existe un arma

    Cuando un arma ataca a un objetivo que puede recibir un ataque

    Entonces no hay error
    --------------------------------------------------------------------------
    Escenario: un arma tiene una potencia predeterminada de 10

    Dado que existe un arma

    Cuando se crea un arma

    Entonces el arma tiene una potencia de 10
    --------------------------------------------------------------------------
    Escenario: un arma tiene una potencia específica de 50

    Dado que existe un arma

    Cuando se crea un arma con potencia 50

    Entonces el arma tiene una potencia de 50
    --------------------------------------------------------------------------
    Escenario: un arma con potencia predeterminada ataca a un objetivo

    Dado que existe un arma

    Cuando el arma ataca a un objetivo puntual con una potencia de 10

    Entonces el objetivo recibe un ataque con potencia 10
    --------------------------------------------------------------------------
    Escenario: un arma con potencia específica ataca a un objetivo

    Dado que existe un arma

    Cuando el arma ataca a un objetivo puntual con una potencia específica de 50

    Entonces el objetivo recibe un ataque con potencia específica de 50
    --------------------------------------------------------------------------
    Escenario: un arma no puede atacar a aquel objetivo que no puede recibir ataques

    Dado que existe un arma

    Cuando el arma ataca a un objetivo que no puede recibir ataques

    Entonces se obtiene un NotImplementedError
    """
    def setUp(self):
        self.arma = Arma()

    def test_arma_es_atacante(self):
        objetivo = Mock()
        self.arma.atacar(objetivo)

    def test_arma_ataca_objetivo_que_puede_recibir_ataque(self):
        objetivo = Mock()

        self.arma.atacar(objetivo)

        objetivo.recibir_ataque.assert_called_once_with()

    def test_arma_potencia_custom_ataca_objetivo_que_puede_recibir_ataque(self):
        potencia_custom = 50
        self.arma = Arma(potencia_custom)
        objetivo = Mock()

        self.arma.atacar(objetivo)

        objetivo.recibir_ataque.assert_called_with()


if __name__ == '__main__':
    unittest.main(verbosity=2)
