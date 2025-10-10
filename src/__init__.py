# src/__init__.py

from flask import Flask

def create_app(env_name: str):
    """
    Función de fábrica para crear y configurar la aplicación Flask.
    Permite inicializar la app con configuraciones y blueprints según el entorno.
    """
    # Crear la app Flask y definir la carpeta de templates
    # '../templates' indica que la carpeta está en la raíz del proyecto
    app = Flask(__name__, template_folder='../templates')

    # --- Configuración opcional ---
    # Se podría cargar un archivo de configuración según el entorno
    # Por ejemplo:
    # app.config.from_object(f'config.{env_name.capitalize()}Config')

    # --- Importación de blueprints ---
    # main: rutas principales de la web
    # libros: rutas de la API de libros
    from .api import main, libros

    # Registrar blueprint principal (sin prefijo)
    app.register_blueprint(main.blueprint)
    # Registrar blueprint de libros con prefijo '/api/libros'
    # Todas las rutas definidas en libros se accederán como /api/libros/...
    app.register_blueprint(libros.blueprint, url_prefix='/api/libros')

    return app
