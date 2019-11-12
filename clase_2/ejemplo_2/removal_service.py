import os
import os.path

class RemovalService:
    """Un servicio eliminar archivos del filesystem."""

    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)
