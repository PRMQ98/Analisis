import pyodbc
from connection import connection_string
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

class DescripcionHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle_request(self, id_pastel):
        pass

class SaborHandler(DescripcionHandler):
    def handle_request(self, id_pastel):
        cursor.execute("SELECT TextoDescripcion FROM Esquema_analisis.Descripcion WHERE ID_Pastel = ? AND TipoDescripcion = 'Sabor'", id_pastel)
        result = cursor.fetchone()
        if result:
            return result[0]
        elif self.next_handler:
            return self.next_handler.handle_request(id_pastel)
        return None

class RellenoHandler(DescripcionHandler):
    def handle_request(self, id_pastel):
        cursor.execute("SELECT TextoDescripcion FROM Esquema_analisis.Descripcion WHERE ID_Pastel = ? AND TipoDescripcion = 'Relleno'", id_pastel)
        result = cursor.fetchone()
        if result:
            return result[0]
        elif self.next_handler:
            return self.next_handler.handle_request(id_pastel)
        return None

class DescripcionGeneralHandler(DescripcionHandler):
    def handle_request(self, id_pastel):
        # Para la descripción general, verifica si el ID_Pastel es NULL
        cursor.execute("SELECT TextoDescripcion FROM Esquema_analisis.Descripcion WHERE ID_Pastel IS NULL AND TipoDescripcion = 'Descripción General'")
        result = cursor.fetchone()
        if result:
            return result[0]
        elif self.next_handler:
            return self.next_handler.handle_request(id_pastel)
        return None
