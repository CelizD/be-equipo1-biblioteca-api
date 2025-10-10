import os
import sys

# --- Configuración del path de Python ---
# Agrega la carpeta raíz del proyecto al path de Python.
# Esto permite que se puedan importar módulos desde 'src' o 'config'.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# --- Importación de la aplicación ---
# Importa la función de fábrica desde el paquete src
from src import create_app

# --- Determinar el entorno de ejecución ---
# Busca la variable de entorno 'FLASK_ENV'. 
# Si no existe, usa 'development' como valor por defecto.
env_name = os.getenv('FLASK_ENV', 'development')

# --- Creación de la aplicación ---
# Llama a la función de fábrica pasando el nombre del entorno.
# Esto permite cargar configuraciones específicas para cada entorno.
app = create_app(env_name)

# --- Ejecución de la aplicación ---
# Si se ejecuta directamente este archivo, inicia el servidor Flask.
# La configuración de debug y otros parámetros se toman de la configuración cargada.
if __name__ == "__main__":
    app.run()
