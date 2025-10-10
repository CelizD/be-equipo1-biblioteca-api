import os
import sys

# Agrega la carpeta raíz del proyecto al path de Python.
# Esto es crucial para que Python pueda encontrar los módulos 'src' y 'config'.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importa la función de fábrica desde el paquete src
from src import create_app

# 1. Determina el entorno actual.
#    Busca una variable de entorno llamada 'FLASK_ENV'. Si no la encuentra,
#    usará 'development' como valor por defecto.
env_name = os.getenv('FLASK_ENV', 'development')

# 2. Crea la aplicación Flask.
#    Pasa el nombre del entorno a la función de fábrica para que cargue
#    la configuración correcta (DevelopmentConfig, ProductionConfig, etc.).
app = create_app(env_name)

# 3. Ejecuta la aplicación.
#    Ya no se necesita 'debug=True', porque la configuración del entorno
#    (cargada en el paso anterior) ahora controla ese y otros parámetros.
if __name__ == "__main__":
    app.run()

