# 📚 API para la Biblioteca Cesun

Bienvenido al repositorio oficial de la **API para la Biblioteca Cesun**. Este proyecto representa la columna vertebral tecnológica diseñada para modernizar y optimizar la gestión de los servicios bibliotecarios.  

A través de una robusta **API RESTful construida con Python y Flask**, ofrecemos una solución centralizada y eficiente para manejar operaciones esenciales como el catálogo de libros, el registro de usuarios y el sistema completo de préstamos y devoluciones.  

Nuestro objetivo es proporcionar una **base sólida y escalable** para futuras aplicaciones web o móviles, garantizando una experiencia de usuario fluida y un control administrativo completo.  

---

## 👥 Integrantes del Equipo

| Nombre Completo               | Matrícula  | Perfil de GitHub |
|-------------------------------|------------|------------------|
| CELIZ MARTINEZ DANIEL         | 23030536   | celizd           |
| RIVERA BARRERA PAUL           | 23030497   |                  |
| ISMAEL CERVANTES CARRANZA     | 23030705   |                  |

---

## 🚀 Funcionalidades Clave

### Para Usuarios Regulares
- 🔍 **Búsqueda Avanzada** → Buscar libros por título, autor o ISBN.  
- 📥 **Solicitud de Préstamos** → Solicitar formalmente un libro del catálogo.  
- 📤 **Gestión de Devoluciones** → Registrar la devolución de un libro prestado.  

### Para Administradores
- 📚 **Gestión de Inventario (CRUD)** → Control completo del catálogo de libros (Crear, Leer, Actualizar, Borrar).  
- 👤 **Gestión de Usuarios** → Registrar, modificar o suspender cuentas de usuario.  
- 🔄 **Control de Préstamos** → Visualizar y manejar el estado actual de los préstamos activos.  

---

## 🛠️ Guía de Instalación y Ejecución

### Requisitos Previos
- Python 3.8 o superior  
- Git instalado  

### Pasos de Instalación
'''bash
# Clonar el repositorio
git clone https://github.com/celizd/be-equipo1-biblioteca-api.git
cd be-equipo1-biblioteca-api

# Crear y activar entorno virtual
python -m venv venv
# En Windows:
.\venv\Scripts\activate

Ejecución del Servidor
python app.py


Luego abre en el navegador: http://127.0.0.1:5000/

# Instalar dependencias
pip install -r requirements.txt

### 📂 Estructura del Proyecto
be-equipo1-biblioteca-api/
│
|
├── .gitignore          # Archivos y carpetas ignorados por Git
├── app.py              # Archivo principal de la aplicación Flask
├── requirements.txt    # Dependencias de Python
├── README.md           # Documentación del proyecto
│
|
└── templates/
    └── index.html      # Plantilla HTML para la página de inicio

### 🤝 Contribuciones

Las contribuciones son bienvenidas.
Haz un Fork del repositorio.
Crea una nueva rama:
git checkout -b feature/nueva-funcionalidad
Realiza tus cambios y haz commit:
git commit -m "feat: agrega nueva funcionalidad"
Sube tus cambios:
git push origin feature/nueva-funcionalidad
Abre un Pull Request.

### 📄 Licencia

Este proyecto está bajo la Licencia MIT.
