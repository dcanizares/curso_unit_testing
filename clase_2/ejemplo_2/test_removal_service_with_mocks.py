from removal_service import RemovalService

import unittest
from unittest import mock

class RemovalServiceWithMocksTestCase(unittest.TestCase):
    """
    =================================================================
    * MUY IMPORTANTE: ¡CUIDADO CON EL ORDEN DE LOS MOCKS EN PYTHON! * 
    =================================================================
    """
    
    @mock.patch('removal_service.os.path')
    @mock.patch('removal_service.os')
    def test_rm_cuando_no_existe_el_archivo(self, m_os, m_path):
        # Arrange
        servicio = RemovalService()
        
        # Configuramos el mock: el archivo "no existe"
        m_path.isfile.return_value = False
        
        # Act
        servicio.rm("cualquier path")
        
        # Assert: chequeamos que NO se haya realizado la llamada al método remove.
        self.assertFalse(m_os.remove.called, "Failed to not remove the file if not present.")

    @mock.patch('removal_service.os.path')
    @mock.patch('removal_service.os')
    def test_rm_cuando_existe_el_archivo(self, m_os, m_path):
        # Arrange
        servicio = RemovalService()

        # Configuramos el mock: el archivo "existe"
        m_path.isfile.return_value = True
        
        # Act
        servicio.rm("cualquier path")
        
        # Assert: chequeamos que NO se haya realizado la llamada al método remove.
        m_os.remove.assert_called_with("cualquier path")