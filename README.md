Biblioteca Cesun API
<p align="center">
<img src="https://www.google.com/search?q=https://placehold.co/600x300/005A9C/FFFFFF%3Ftext%3DBiblioteca%2BCesun%2BAPI%26font%3Draleway" alt="Banner de la Biblioteca Cesun API">
</p>

API RESTful desarrollada en Flask para gestionar los servicios de la Biblioteca Cesun. Este proyecto sirve como el backend central para operaciones clave como la administración del catálogo de libros, el registro de usuarios y el sistema de préstamos y devoluciones.

👥 Integrantes del Equipo
Nombre Completo

Matrícula

GitHub Profile

CELIZ MARTINEZ DANIEL

23030536

celizd

RIVERA BARRERA PAUL

23030497

(Añadir perfil)

ISMAEL CERVANTES CARRANZA

23030705

(Añadir perfil)

🚀 Funcionalidades Clave
Para Usuarios Regulares
Búsqueda Avanzada: Permite buscar libros por título, autor o ISBN.

Solicitud de Préstamos: Interfaz para que el usuario solicite formalmente un libro del catálogo.

Gestión de Devoluciones: Proceso para registrar la devolución de un libro prestado.

Para Administradores
Gestión de Inventario (CRUD): Control completo sobre el catálogo de libros (Crear, Leer, Actualizar, Borrar).

Gestión de Usuarios: Capacidad para registrar, modificar o suspender cuentas de usuario.

Control de Préstamos: Visualización y manejo del estado actual de todos los préstamos activos.

💻 Stack Tecnológico
Backend: Python

Framework: Flask

Frontend Básico: HTML5, CSS3

Entorno: venv (Entorno Virtual de Python)

🛠️ Guía de Instalación y Ejecución
Sigue estos pasos para instalar y poner en marcha el proyecto en tu entorno local.

Requisitos Previos
Python 3.8 o superior.

Git para clonar el repositorio.

Pasos de Instalación
Clona el repositorio desde GitHub:

git clone [https://github.com/celizd/be-equipo1-biblioteca-api.git](https://github.com/celizd/be-equipo1-biblioteca-api.git)
cd be-equipo1-biblioteca-api

Crea y activa un entorno virtual:

# Crear el entorno virtual
python -m venv venv

# Activar en Windows (CMD / PowerShell)
.\venv\Scripts\activate

Instala las dependencias del proyecto:

pip install -r requirements.txt

Ejecución del Servidor
Con el entorno virtual activado, inicia la aplicación Flask:

python app.py

Abre tu navegador web y visita http://127.0.0.1:5000/ para ver la página de inicio.

📂 Estructura del Proyecto
be-equipo1-biblioteca-api/
│
├── .gitignore          # Archivos y carpetas ignorados por Git
├── app.py              # Archivo principal de la aplicación Flask
├── requirements.txt    # Lista de dependencias de Python
├── README.md           # Documentación del proyecto
│
└── templates/
    └── index.html      # Plantilla HTML para la página de inicio
