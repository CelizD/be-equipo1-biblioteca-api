
import os

# Obtiene la ruta del directorio base del proyecto
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    """Configuración base de la que heredarán las demás."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "un_secreto_muy_seguro")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """Configuración para el entorno de desarrollo."""
    DEBUG = True
    # Define la ruta de la base de datos SQLite dentro del proyecto
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, '..', 'biblioteca-dev.db')