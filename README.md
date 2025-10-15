# 📚 API para la Biblioteca Cesun

Bienvenido al repositorio oficial de la **API para la Biblioteca Cesun**. Este proyecto representa la columna vertebral tecnológica diseñada para modernizar y optimizar la gestión de los servicios bibliotecarios.

A través de una robusta **API RESTful construida con Python y Flask**, ofrecemos una solución centralizada y eficiente para manejar operaciones esenciales como el catálogo de libros y, en el futuro, el registro de usuarios y el sistema completo de préstamos y devoluciones.

Nuestro objetivo es proporcionar una **base sólida y escalable** para futuras aplicaciones web o móviles, garantizando una experiencia de usuario fluida y un control administrativo completo.

---

## 👥 Integrantes del Equipo

| Nombre Completo               | Matrícula  | Perfil de GitHub |
|-------------------------------|------------|------------------|
| CELIZ MARTINEZ DANIEL         | 23030536   | celizd           |
| RIVERA BARRERA PAUL           | 23030497   | ISMAELCervantes  |
| ISMAEL CERVANTES CARRANZA     | 23030705   | paulrivera123    |

---

## 🚀 Funcionalidades

### Funcionalidades Actuales
- 📚 **Gestión de Inventario (CRUD)** → Control completo del catálogo de libros (Crear, Leer, Actualizar, Borrar).
- 🔄 **Persistencia de Datos** → La información se almacena en una base de datos SQLite.
- 🌱 **Datos Semilla** → Carga inicial de datos para un arranque rápido.

### Funcionalidades Planeadas
- 🔍 **Búsqueda Avanzada** → Buscar libros por título, autor o ISBN.
- 👤 **Gestión de Usuarios** → Registrar, modificar o suspender cuentas de usuario.
- 📥 **Solicitud de Préstamos** → Solicitar formalmente un libro del catálogo.
- 📤 **Gestión de Devoluciones** → Registrar la devolución de un libro prestado.

---

## 🛠️ Guía de Instalación y Ejecución

### Requisitos Previos
- Python 3.8 o superior
- Git instalado

### Pasos de Instalación

1.  **Clonar el repositorio**
    ```bash
    git clone [https://github.com/celizd/be-equipo1-biblioteca-api.git](https://github.com/celizd/be-equipo1-biblioteca-api.git)
    cd be-equipo1-biblioteca-api
    ```

2.  **Crear y activar entorno virtual**
    ```bash
    # Crear entorno
    python -m venv venv
    
    # Activar en Windows
    .\venv\Scripts\activate
    
    # Activar en macOS/Linux
    source venv/bin/activate
    ```

3.  **Instalar dependencias**
    ```bash
    pip install -r requirements.txt
    ```

### Configuración de la Base de Datos

Para configurar la base de datos por primera vez o para reiniciarla, sigue estos pasos en la terminal:

1.  **Establecer la variable de entorno de Flask**
    ```bash
    # En Windows (cmd)
    set FLASK_APP=app.py

    # En macOS/Linux
    export FLASK_APP=app.py
    ```

2.  **Inicializar las migraciones** (solo se hace una vez por proyecto)
    ```bash
    flask db init
    ```

3.  **Crear y aplicar la migración inicial**
    ```bash
    flask db migrate -m "Creacion inicial de tablas"
    flask db upgrade
    ```

4.  **Poblar la base de datos con datos de ejemplo**
    ```bash
    flask seed
    ```

### Ejecución del Servidor

Una vez completada la instalación y configuración de la base de datos:

```bash

flask run

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
## 🏛️ Diagrama de la Arquitectura de Datos

```mermaid
classDiagram
    direction RL
    class Usuario {
        +int id
        +String nombre
        +String matricula
        +String rol
        --
        +solicitarPrestamo(libro)
        +devolverLibro(prestamo)
    }

    class Libro {
        +String titulo
        +String autor
        +String genero
        +int paginas
        +int anio
        +String idioma
        +bool disponible
        --
        +marcarComoPrestado()
        +marcarComoDevuelto()
    }

    class Prestamo {
        +int id
        +int idUsuario
        +int idLibro
        +Date fechaPrestamo
        +Date fechaDevolucion
        +bool devuelto
        --
        +registrarDevolucion()
        +calcularMulta()
    }

    Usuario "1" -- "0..*" Prestamo : "tiene"
    Libro "1" -- "0..*" Prestamo : "es parte de"
