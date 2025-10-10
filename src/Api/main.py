from flask import Blueprint, render_template
# Importamos la lista de libros desde el blueprint de la API
from .libros import libros

# --- Creación del Blueprint para la parte principal del sitio ---
blueprint = Blueprint('main', __name__)

@blueprint.route('/')
def index():
    """
    Endpoint GET /
    Renderiza la página de inicio (index.html).
    Pasa la lista completa de libros al template para que se puedan mostrar.
    """
    return render_template('index.html', libros=libros)

# Nota: Asegúrate de que la plantilla 'index.html' esté preparada
# para iterar sobre la lista 'libros' y mostrar sus datos correctamente.
