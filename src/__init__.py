# src/__init__.py
import os
from flask import Flask
from .extensions import db, migrate

def create_app(env_name: str | None = 'development'):
    """
    Función de fábrica para crear y configurar la aplicación Flask.
    """
    app = Flask(__name__, template_folder='../templates')

    _load_config(app, env_name)
    _register_extensions(app)
    _register_blueprints(app)
    # _register_cli(app) # Descomentaremos esto más adelante

    return app

def _load_config(app: Flask, env_name: str | None) -> None:
    """Carga la configuración desde el archivo config.py."""
    config_name = f"src.config.{env_name.capitalize()}Config"
    app.config.from_object(config_name)

def _register_extensions(app: Flask) -> None:
    """Registra las extensiones de Flask."""
    db.init_app(app)
    migrate.init_app(app, db)

def _register_blueprints(app: Flask) -> None:
    """Registra los blueprints de la aplicación."""
    from .api import main, libros
    
    app.register_blueprint(main.blueprint)
    app.register_blueprint(libros.blueprint, url_prefix='/api/libros')