from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
from flask_cors import CORS
from connection import connection_string
from collections import defaultdict
from StrategyMethod import *
# from PastelFactory import Pastel, PastelHorneado, PastelFrio, PastelDeYogurt
# from Observer import PedidoObservable, ObservadorPedido
import pyodbc

app = Flask(__name__, template_folder="C:/Users/baril/Documents/8vo Semestre Sistemas/Análisis de Sistemas II/Rama de pruebas/Analisis/Frontend/templates")
CORS(app)

folder="C:/Users/baril/Documents/8vo Semestre Sistemas/Análisis de Sistemas II/Rama de pruebas/Analisis/Frontend/templates"
@app.route('/templates/<path:filename>')
def serve_static(filename):
    return send_from_directory(folder, filename)

@app.route("/")
def index():
    return render_template("login.html")



@app.route('/api/login', methods=["POST"])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    
    connection = pyodbc.connect(connection_string)

    
    # Realiza la consulta a la base de datos para validar las credenciales
    cursor = connection.cursor()
    query = f"SELECT * FROM Esquema_analisis.Usuarios WHERE Usuario = '{username}' AND Contra = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    # user = str(user)
    if user:
        nombre_usuario = user [3]
        menus = []
        submenus = []
        if nombre_usuario == 'Administrador':
            menus = ['Adminsitracion']
            submenus = ['Crear pasteles', 'Descuentos', 'Clientes']

        # Consulta para obtener todos los pasteles desde la base de datos
        pasteles_query = "SELECT * FROM Esquema_analisis.Pastel"
        cursor.execute(pasteles_query)
        pasteles_data = cursor.fetchall()

        # Crear una lista de pasteles desde los datos recuperados
        pasteles = []
        for row in pasteles_data:
            pastel = {
                'Nombre': row[1],
                'Tipo': row[2],
                'Sabor': row[3],
                'Relleno': row[4],
                'Precio':row[5],
                'FechaIngreso': row[6]
            }
            pasteles.append(pastel) 
            
        return jsonify({'message': 'Credenciales válidas', 'Usuario': nombre_usuario, 'Menus': menus, 'Submenus': submenus, 'Pasteles': pasteles})
        
        # else:
        #     return jsonify({'message': 'Credenciales válidas', 'Usuario': user})
    else:
            return jsonify({'message': 'Credenciales inválidas'}), 401


@app.route('/api/catalogo/<tipo_pastel>', methods=["GET"])
def catalogo_por_tipo(tipo_pastel):
    if tipo_pastel == 'frio':
        tipo_pastel == 'frío'
    connection = pyodbc.connect(connection_string)
    
    # Realiza la consulta a la base de datos para obtener todos los pasteles
    cursor = connection.cursor()
    pasteles_query = "SELECT * FROM Esquema_analisis.Pastel"
    cursor.execute(pasteles_query)
    pasteles_data = cursor.fetchall()

    # Crear una lista de pasteles desde los datos recuperados
    pasteles = []
    for row in pasteles_data:
        pastel = {
            'Nombre': row[1],
            'Tipo': row[2],
            'Sabor': row[3],
            'Relleno': row[4],
            'Precio': row[5],
            'FechaIngreso': row[6]
        }
        pasteles.append(pastel)

    # Seleccionar la estrategia adecuada según el tipo de pastel
    if tipo_pastel == 'horneado':
        estrategia = EstrategiaHorneado()
    elif tipo_pastel == 'frío':
        estrategia = EstrategiaFrio()
    elif tipo_pastel == 'yogurt':
        estrategia = EstrategiaYogurt()
    elif tipo_pastel == 'queso':
        estrategia = EstrategiaQueso()
    else:
        return jsonify({'message': 'Tipo de pastel no válido'}), 400

    # Aplicar la estrategia para filtrar los pasteles
    pasteles_filtrados = estrategia.filtrar_pasteles(pasteles)

    return jsonify({'message': 'Catálogo de pasteles', 'Pasteles': pasteles_filtrados})


@app.route('/api/catalogo', methods=["GET"])
def catalogo():
    connection = pyodbc.connect(connection_string)
    
    # Realiza la consulta a la base de datos para obtener todos los pasteles
    cursor = connection.cursor()
    pasteles_query = "SELECT * FROM Esquema_analisis.Pastel"
    cursor.execute(pasteles_query)
    pasteles_data = cursor.fetchall()

    # Crear un diccionario para agrupar los pasteles por tipo
    pasteles_agrupados = defaultdict(list)
    for row in pasteles_data:
        pastel = {
            'Nombre': row[1],
            'Tipo': row[2],
            'Sabor': row[3],
            'Relleno': row[4],
            'Precio': row[5],
            'FechaIngreso': row[6]
        }
        tipo_pastel = row[2]
        pasteles_agrupados[tipo_pastel].append(pastel)

    # Convertir el diccionario en una lista de objetos JSON
    catalogo = [{'Tipo': tipo, 'Pasteles': pasteles} for tipo, pasteles in pasteles_agrupados.items()]

    return jsonify({'message': 'Catálogo de pasteles', 'Catalogo': catalogo})


if __name__ == "__main__":
    app.run(port=5000,debug=True)