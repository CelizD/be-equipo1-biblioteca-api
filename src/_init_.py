# src/__init__.py
from flask import Flask
# 1. Importamos el diccionario de configuraciones desde config.py
from config import config_by_name

def create_app(config_name: str) -> Flask:
    """
    Crea y configura la aplicación Flask usando la configuración del entorno especificado.
    """
    # Usamos '../templates' para decirle a Flask que la carpeta de plantillas está un nivel arriba.
    app = Flask(__name__, template_folder='../templates')
    
    # 2. Cargamos la configuración desde el objeto correspondiente al nombre del entorno.
    #    Ej: si config_name es 'development', carga la clase DevelopmentConfig.
    app.config.from_object(config_by_name[config_name])
    
    # 3. Registramos los blueprints que contienen las rutas.
    _register_blueprints(app)
    
    return app

def _register_blueprints(app: Flask) -> None:
    """Importa y registra los blueprints de la aplicación."""
    from .api.libros import blueprint as libros_blueprint
    from .api.main import blueprint as main_blueprint
    
    app.register_blueprint(libros_blueprint, url_prefix="/libros")
    app.register_blueprint(main_blueprint)

# --- IGNORE --- 