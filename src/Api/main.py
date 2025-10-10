from flask import Blueprint, render_template
# Importamos la lista de libros desde el blueprint de la API
from .libros import libros

blueprint = Blueprint('main', __name__)

@blueprint.route('/')
def index():
    """
    Renderiza la página de inicio y le pasa la lista completa de libros
    para que puedan ser mostrados en la plantilla HTML.
    """
    return render_template('index.html', libros=libros)

# Nota: Asegúrate de que la plantilla 'index.html' esté configurada para
# mostrar la lista de libros pasada en el contexto.