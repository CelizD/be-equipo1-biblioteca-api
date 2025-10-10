# src/__init__.py

from flask import Flask

def create_app(env_name: str):
    """
    Función de fábrica para crear y configurar la aplicación Flask.
    """
    # Se ajusta la ruta a la carpeta de plantillas para que la encuentre
    # desde la raíz del proyecto.
    app = Flask(__name__, template_folder='../templates')

    # Aquí podrías cargar configuraciones desde un archivo, por ejemplo:
    # app.config.from_object(f'config.{env_name.capitalize()}Config')

    # Importar y registrar los Blueprints
    from .api import main, libros

    app.register_blueprint(main.blueprint)
    # Prefija todas las rutas de la API de libros con /api/libros
    app.register_blueprint(libros.blueprint, url_prefix='/api/libros')

    return app