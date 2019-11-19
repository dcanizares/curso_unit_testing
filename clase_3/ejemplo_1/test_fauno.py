import unittest
from unittest.mock import Mock, patch

from escudo import Escudo
from fauno import Fauno

class FaunoTestCase(unittest.TestCase):
    """
    ==========================================================================
    Casos de prueba detectados
    ==========================================================================

    Escenario: un fauno es atacable

    Dado que existe un fauno

    Cuando un fauno recibe ataque

    Entonces no hay error
    --------------------------------------------------------------------------
    Escenario: un fauno es atacante

    Dado que existe un fauno con arma

    Cuando un fauno ataca

    Entonces ataca con su arma
    --------------------------------------------------------------------------
    Escenario: un fauno posee 100 como resistencia predeterminada.

    Dado que existe un fauno

    Cuando un fauno nace

    Entonces su resistencia es 100
    --------------------------------------------------------------------------
    Escenario: un fauno posee 50 como resistencia específica.

    Dado que existe un fauno

    Cuando un fauno nace
        Y se especifica que su resistencia es 50

    Entonces su resistencia es 50
    --------------------------------------------------------------------------
    Escenario: un fauno con escudo no reduce su resistencia ante un ataque

    Dado que existe un fauno con escudo

    Cuando el fauno es atacado
        Y su escudo recibió menos de 5 ataques

    Entonces su resistencia no se disminuye
    --------------------------------------------------------------------------
    Escenario: un fauno con escudo ya vencido, reduce a 90 su resistencia ante un ataque de 10

    Dado que existe un fauno con un escudo y una resistencia de 100

    Cuando el fauno recibe un ataque con potencia 10
        Y su escudo ya se encuentra vencido

    Entonces su resistencia valdrá 90
    --------------------------------------------------------------------------
    Escenario: un fauno con escudo ya vencido, reduce a 0 su resistencia ante un ataque de 100

    Dado que existe un fauno con un escudo y una resistencia de 100

    Cuando el fauno recibe un ataque con potencia 100
        Y su escudo ya se encuentra vencido

    Entonces su resistencia valdrá 0
    --------------------------------------------------------------------------
    Escenario: un fauno con escudo ya vencido, reduce a 0 su resistencia ante un ataque de más de 100

    Dado que existe un fauno con un escudo y una resistencia de 100

    Cuando el fauno recibe un ataque con potencia 10
        Y su escudo ya se encuentra vencido
        Y vuelve a recibir un ataque, pero de potencia 100

    Entonces su resistencia valdrá 0
    --------------------------------------------------------------------------
    Escenario: un fauno nacido con resistencia 0 no puede ser atacado

    Dado que existe un fauno nacido con resistencia 0

    Cuando el fauno recibe un ataque con cualquier potencia

    Entonces aparecerá un ValueError con mensaje '¡El objetivo ya no puede recibir ataques!'
    --------------------------------------------------------------------------
    Escenario: un fauno con resistencia 0 no puede ser atacado

    Dado que existe un fauno con resistencia 100

    Cuando el fauno recibe múltiples ataques cuyas potencias sumen más de 100
        Y sea atacado nuevamente

    Entonces aparecerá un ValueError con mensaje '¡El objetivo ya no puede recibir ataques!'
    """
    def setUp(self):
        self.fauno = Fauno()

    def test_fauno_es_atacante(self):
        objetivo = Mock()
        with patch('fauno.Arma.atacar') as m_atacar:
            self.fauno.atacar(objetivo)

        m_atacar.assert_called_once_with()

    def test_fauno_con_escudo_vencido_tiene_90_al_recibir_ataque_de_10(self):
        with patch('fauno.Escudo.recibir_ataque', side_effect=ValueError) as m_recibir_ataque:
            self.fauno.recibir_ataque(10)

        m_recibir_ataque.assert_called_once_with()

        self.assertEqual(90, self.fauno.resistencia)

    def test_fauno_tiene_0_al_recibir_ataque_de_100(self):
        with patch('fauno.Escudo', side_effect=ValueError):
            self.fauno.recibir_ataque(100)

        self.assertEqual(0, self.fauno.resistencia)

    def test_fauno_tiene_0_al_recibir_ataque_mayor_a_resistencia(self):
        with patch('fauno.Escudo.recibir_ataque'):
            self.fauno.recibir_ataque(10)
            self.fauno.recibir_ataque(100)

        self.assertEqual(0, self.fauno.resistencia)

    def test_fauno_en_0_arroja_value_error_al_recibir_ataque(self):
        with patch('fauno.Escudo.recibir_ataque', side_effect=ValueError):
            self.fauno.recibir_ataque(90)
            self.fauno.recibir_ataque(8)
            self.fauno.recibir_ataque(5)
            self.fauno.recibir_ataque(5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
