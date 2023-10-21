from abc import ABC, abstractmethod
import pyodbc

class PastelFactory(ABC):
    @abstractmethod
    def create_pastel(self, data):
        pass

    @abstractmethod
    def create_descripcion(self, data, pastel_id):
        pass

class DatabasePastelFactory(PastelFactory):
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def create_pastel(self, data):
        connection = pyodbc.connect(self.connection_string)
        cursor = connection.cursor()

        cursor.execute("SELECT MAX(ID_Pastel) FROM Esquema_analisis.Pastel")
        ultimo_id_pastel = cursor.fetchone()[0]
        nuevo_id_pastel = ultimo_id_pastel + 1

        pastel_query = """INSERT INTO Esquema_analisis.Pastel 
                          (ID_Pastel, Nombre, Tipo, Sabor, Relleno, Precio, FechaIngreso)
                          VALUES (?, ?, ?, ?, ?, ?, GETDATE())"""
        cursor.execute(pastel_query, (nuevo_id_pastel, data['nombre'], data['tipoPastel'], data['sabor'], data['relleno'], data['precio']))
        connection.commit()
        connection.close()

        return nuevo_id_pastel

    def create_descripcion(self, data, pastel_id):
        connection = pyodbc.connect(self.connection_string)
        cursor = connection.cursor()

        cursor.execute("SELECT MAX(ID_Descripcion) FROM Esquema_analisis.Descripcion")
        ultimo_id_descripcion = cursor.fetchone()[0]
        nuevo_id_descripcion = ultimo_id_descripcion + 1

        descripcion_query = """INSERT INTO Esquema_analisis.Descripcion 
                              (ID_Descripcion, ID_Pastel, TipoDescripcion, TextoDescripcion)
                              VALUES (?, ?, ?, ?)"""
        cursor.execute(descripcion_query, (nuevo_id_descripcion, pastel_id, data['tipoDescripcion'], data['descripcion']))
        connection.commit()
        connection.close()

    def create_pasteles(self, data):
        pastel_id = self.create_pastel(data)
        self.create_descripcion(data, pastel_id)
