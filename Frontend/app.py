from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

# Ruta para la página de inicio de sesión
@app.route("/")
def login():
    return render_template("login.html")

# Ruta para la página de inicio
@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

# Ruta para cerrar la sesión
@app.route("/logout")
def logout():
    # Aquí debes realizar acciones para cerrar la sesión, como limpiar cookies o
    # invalidar la sesión del usuario en el servidor, dependiendo de tu método de autenticación.
    
    # Redirigir al usuario a la página de inicio de sesión o a donde desees
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, port=1200)
