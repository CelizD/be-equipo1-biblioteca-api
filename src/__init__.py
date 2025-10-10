# src/__init__.py
from flask import Flask

def create_app(config_object: dict | None = None) -> Flask:
    """
    Crea y configura una instancia de la aplicación Flask.
    Este es el corazón del patrón de 'fábrica de aplicaciones'.
    """
    app = Flask(__name__)
    
    # Carga la configuración
    _load_config(app, config_object)
    
    # Registra los blueprints (las rutas de la API)
    _register_blueprints(app)
    
    return app

def _load_config(app: Flask, config_object: dict | None) -> None:
    """Carga la configuración de la aplicación desde un objeto."""
    app.config.from_mapping(
        # Valores por defecto que pueden ser sobrescritos
        SECRET_KEY="dev",
        JSON_SORT_KEYS=False,
    )
    if config_object:
        app.config.update(config_object)

def _register_blueprints(app: Flask) -> None:
    """
    Importa y registra los blueprints en la aplicación.
    Aquí es donde se conectan las rutas de la API.
    """
    # Importamos el blueprint de libros desde el módulo de la API
    from src.Api.libros import blueprint as libros_blueprint 
    
    # Registramos el blueprint con un prefijo de URL
    # Todas las rutas en este blueprint comenzarán con /libros
    app.register_blueprint(libros_blueprint, url_prefix="/libros")
    