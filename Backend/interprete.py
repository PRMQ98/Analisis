from connection import connection_string
import pyodbc
from unidecode import unidecode

class BuscadorPasteles:
    def __init__(self):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        pasteles_query = "SELECT * FROM Esquema_analisis.Pastel"
        cursor.execute(pasteles_query)
        self.lista_pasteles = cursor.fetchall()

    def buscar_pasteles(self, descripcion):
        interpreter = BusquedaInterpreter(self.lista_pasteles)
        resultados = interpreter.interpret(descripcion)
        return resultados

class BusquedaInterpreter:
    def __init__(self, lista_pasteles):
        self.lista_pasteles = lista_pasteles

    def interpret(self, query):
        query = query.lower()

        palabras_clave = query.split()
        conectores = ["y", "de", "con"]

        # Eliminar los conectores de la consulta
        palabras_clave = [palabra for palabra in palabras_clave if palabra not in conectores]

        resultados = []

        if "pastel" in palabras_clave:
            palabras_clave.remove("pastel")
            for pastel in self.lista_pasteles:
                pastel_dict = {
                    'id': pastel[0],
                    'nombre': pastel[1],
                    'tipo': pastel[2],
                    'sabor': pastel[3],
                    'relleno': pastel[4],
                    'precio': float(pastel[5]),
                    'fecha': pastel[6]
                }

                descripcion_coincide = self.evaluar_descripcion(pastel_dict, palabras_clave)
                if descripcion_coincide:
                    self.asignar_imagen(pastel_dict)
                    resultados.append(pastel_dict)
        else:
            for pastel in self.lista_pasteles:
                pastel_dict = {
                    'id': pastel[0],
                    'nombre': pastel[1],
                    'tipo': pastel[2],
                    'sabor': pastel[3],
                    'relleno': pastel[4],
                    'precio': float(pastel[5]),
                    'fecha': pastel[6]
                }

                descripcion_coincide = self.evaluar_descripcion(pastel_dict, palabras_clave)
                if descripcion_coincide:
                    self.asignar_imagen(pastel_dict)
                    resultados.append(pastel_dict)

        return resultados



    def evaluar_descripcion(self, pastel, palabras_clave):
        for palabra in palabras_clave:
            if palabra in pastel['nombre'].lower() or palabra in pastel['sabor'].lower() \
               or palabra in pastel['tipo'].lower() or palabra in pastel['relleno'].lower():
                return True
        return False
    
    def asignar_imagen(self, pastel):
        if pastel['sabor'].lower() == 'fresa' or pastel['nombre'].lower() == 'pastel de fresa':
            pastel['imagenSabor'] = "../static/images/fresa.jpg"
        elif pastel['sabor'].lower() == 'chocolate' or pastel['nombre'].lower() == 'pastel de chocolate':
            pastel['imagenSabor'] = "../static/images/chocolate.jpg"
        else:
            pastel['imagenSabor'] = "../static/images/blanco.jpg"


