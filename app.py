# app.py

import os
import sys

# Agrega la carpeta raíz del proyecto al path de Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src import create_app

# Determinar el entorno de ejecución
env_name = os.getenv('FLASK_ENV', 'development')

# Creación de la aplicación
app = create_app(env_name)

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])