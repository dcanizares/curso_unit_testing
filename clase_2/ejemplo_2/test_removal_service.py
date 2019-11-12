from removal_service import RemovalService

import os.path
import tempfile
import unittest

class RemovalServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")
        # print(self.tmpfilepath)
        with open(self.tmpfilepath, "w") as f:
            f.write("Borrame!")
        
    def test_rm(self):
        # Arrange
        servicio = RemovalService()

        # Act: removemos el archivo
        servicio.rm(self.tmpfilepath)

        # Assert: chequeamos que haya sido efectivamente eliminado
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Error al eliminar el archivo")
