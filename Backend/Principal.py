from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory, send_file, make_response
import tempfile
from flask_cors import CORS
from connection import connection_string
from collections import defaultdict
from StrategyMethod import *
from FactoryMethod import *
from ChainofResponsability import *
from AbstracFactory import *
from interprete import BuscadorPasteles
from io import BytesIO
from reportlab.pdfgen import canvas
from unidecode import unidecode
import pyodbc
# C:\Users\baril\Documents\8vo Semestre Sistemas\Desarrollo Web\Analisis\Frontend\templates
app = Flask(__name__, template_folder="C:/Users/baril/Documents/8vo Semestre Sistemas/Desarrollo Web/Analisis/Frontend/templates",
        static_folder="C:/Users/baril/Documents/8vo Semestre Sistemas/Desarrollo Web/Analisis/Frontend/static")
CORS(app)

folder="C:/Users/baril/Documents/8vo Semestre Sistemas/Desarrollo Web/Analisis/Frontend/templates"
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
    
    if user:    
        nombre_usuario = user [2]
        menus = []
        submenus = []
        if nombre_usuario == 'Administrador':
            menus = ['Adminsitracion']
            submenus = ['Crear pasteles']
        pasteles_query = "SELECT * FROM Esquema_analisis.Pastel"
        cursor.execute(pasteles_query)
        pasteles_data = cursor.fetchall()

        # Crear una lista de pasteles desde los datos recuperados
        pasteles = []
        for row in pasteles_data:
            pastel = {
                'Id': row[0],
                'Nombre': row[1],
                'Tipo': row[2],
                'Sabor': row[3],
                'Relleno': row[4],
                'Precio':row[5],
                'FechaIngreso': row[6],
                'imagenSabor': row[3]
            }
            if pastel['Sabor'] == 'Fresa' or pastel['Nombre'] == 'Pastel de Fresa':
                pastel['imagenSabor'] = "../static/images/fresa.jpg"
            elif pastel['Sabor'] == 'Chocolate' or pastel['Nombre'] == 'Pastel de Chocolate':
                pastel['imagenSabor'] = "../static/images/chocolate.jpg"
            else:
                pastel['imagenSabor'] = "../static/images/blanco.jpg"
            pasteles.append(pastel) 
            
        return jsonify({'message': 'Credenciales válidas', 'Usuario': nombre_usuario, 'Menus': menus, 'Submenus': submenus, 'Pasteles': pasteles})

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
            'Id': row[0],
            'Nombre': row[1],
            'Tipo': row[2],
            'Sabor': row[3],
            'Relleno': row[4],
            'Precio': row[5],
            'FechaIngreso': row[6],
            'imagenSabor': row[3]
        }
        
        if pastel['Sabor'] == 'Fresa' or pastel['Nombre'] == 'Pastel de Fresa':
            pastel['imagenSabor'] = "../static/images/fresa.jpg"
        elif pastel['Sabor'] == 'Chocolate' or pastel['Nombre'] == 'Pastel de Chocolate':
            pastel['imagenSabor'] = "../static/images/chocolate.jpg"
        else:
            pastel['imagenSabor'] = "../static/images/blanco.jpg"
            
        pasteles.append(pastel)
    if tipo_pastel != 'todos':
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
    elif tipo_pastel == 'todos':
        pasteles_filtrados = pasteles

    return jsonify({'message': 'Catálogo de pasteles', 'Pasteles': pasteles_filtrados})


@app.route('/api/pedido', methods=['POST'])
def crear_pedido_contado():
    data = request.json
    cliente = data['cliente']
    productos = data['productos']

    connection = pyodbc.connect(connection_string)
    # Realiza la consulta a la base de datos para buscar el tipo de cliente
    cursor = connection.cursor()
    cliente_query = """SELECT *
                    FROM Esquema_analisis.Usuarios U
                    INNER JOIN Esquema_analisis.Cliente C ON U.ID_Cliente = C.ID_Cliente
                    WHERE U.Usuario = ?;"""
    cursor.execute(cliente_query, (cliente,))
    resultado_cliente = cursor.fetchone()
    # tipo_cliente = str(resultado_cliente)
    tipo_cliente = resultado_cliente[8]

    if tipo_cliente == "Credito":
        factory_credito = PedidoCreditoFactory()
        pedido_credito = factory_credito.crear_pedido(cliente, productos)
        factura = pedido_credito.generar_factura()
        response = make_response(factura.read())
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=nota_credito.pdf'

        factura.close()
    elif tipo_cliente == "Contado":
        factory_contado = PedidoContadoFactory()
        pedido_contado = factory_contado.crear_pedido(cliente, productos)
        factura = pedido_contado.generar_factura()

        response = make_response(factura.read())
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=factura.pdf'

        factura.close()

    return response

@app.route('/api/buscar_pasteles', methods=['POST'])
def buscar_pasteles():
    data = request.get_json()
    descripcion = data.get('descripcion')
    buscador = BuscadorPasteles()
    pasteles_coincidentes = buscador.buscar_pasteles(descripcion)

    return jsonify({'resultados': pasteles_coincidentes})

@app.route('/api/descripcion', methods=['POST'])
def descripcion():
    data = request.get_json()
    id_pastel = data['idPastel']

    sabor_handler = SaborHandler()
    relleno_handler = RellenoHandler()
    descripcion_general_handler = DescripcionGeneralHandler()

    resultado = sabor_handler.handle_request(id_pastel)
    if resultado is None:
        resultado = relleno_handler.handle_request(id_pastel)
    if resultado is None:
        resultado = descripcion_general_handler.handle_request(id_pastel)

    return jsonify({'descripcion': resultado})


@app.route('/api/crearPasteles', methods=['POST'])
def crear_pasteles():
    data = request.get_json()
    # nombre = data.get('nombre')
    # sabor = data.get('sabor')
    # relleno = data.get('relleno')
    # tipoPastel = data.get('tipoPastel')
    # precio = data.get('precio')
    # tipoDescripcion = data.get('tipoDescripcion')
    # descripcion = data.get('descripcion')

    # Crear una instancia de DatabasePastelFactory
    pastel_factory = DatabasePastelFactory(connection_string)

    # Llamar al método create_pasteles para insertar datos en las tablas
    pastel_factory.create_pasteles(data)

    
    return jsonify({"message": "Operación exitosa"}), 200

if __name__ == "__main__":
    app.run(port=5000,debug=True)
