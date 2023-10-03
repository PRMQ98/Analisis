from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
from flask_cors import CORS
from connection import connection_string
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

if __name__ == "__main__":
    app.run(port=5000,debug=True)