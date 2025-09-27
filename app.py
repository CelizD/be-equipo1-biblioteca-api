from flask import Flask, render_template

# Inicializa la aplicación Flask
app = Flask(__name__)

@app.route("/")
def home():
    """
    Ruta principal que renderiza la página de inicio.
    Verifica que la app y las plantillas funcionan correctamente.
    """
    return render_template(
        "index.html",
        titulo="Biblioteca Universitaria API",
        mensaje="¡Bienvenido a la API de la Biblioteca Universitaria!"
    )

# Punto de entrada para ejecutar la aplicación
if __name__ == "__main__":
    # El modo debug se activa para ver los cambios en tiempo real
    app.run(debug=True)