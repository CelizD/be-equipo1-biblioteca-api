# Biblioteca Universitaria

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de una biblioteca universitaria diseñada para la gestión eficiente de la información que se maneje en esta. El objetivo principal es ofrecer dos interfaces claras: una para los usuarios regulares y otra para los administradores. La aplicación permite a los usuarios buscar en tiempo real el catálogo de libros, solicitar nuevos préstamos y registrar la devolución de material que tengan pendiente.

La parte fundamental de la aplicación es el panel de administrador, que proporciona herramientas para la gestión completa del inventario (agregar, modificar, eliminar libros) y la administración de los usuarios del sistema. El desarrollo se enfoca en la implementación de una arquitectura web y el manejo de flujos de datos complejos entre el frontend y el backend.

# Integrantes

Celiz Martinez Daniel 23030536
Cervantez Carranza Ismael 23030705
Rivera Barrera Paul 23030497


# Funcionalidades Clave

El sistema cuenta con las siguientes características principales:

# Para Usuarios Regulares
Búsqueda Avanzada: Permite buscar libros por título, autor o ISBN.
Solicitud de Préstamos: Interfaz para que el usuario solicite formalmente un libro del catálogo.
Gestión de Devoluciones: Proceso para registrar la devolución de un libro prestado.

# Para Administradores
Gestión de Inventario (CRUD): Control completo sobre el catálogo de libros.
Gestión de Usuarios: Capacidad para registrar, modificar o suspender cuentas de usuario.
Control de Préstamos: Visualización y manejo del estado actual de todos los préstamos activos.


# Instalación y Ejecución

Sigue estos pasos para instalar y poner en marcha el proyecto en tu entorno local.

# Requisitos

   Python 3.8+ instalado.
   Sistema con Windows 11. 

# 1. Instalación de Dependencias

Se recomienda crear y activar un entorno virtual para aislar las dependencias:

1.  **Crear el Entorno Virtual (`venv`):**
    ```bash
    python -m venv venv
    ```

2.  Activar el Entorno Virtual:
    Windows (CMD/PowerShell):
        ```bash
        .\venv\Scripts\activate
        ```
    

3.  **Instalar los Requisitos:**
    Asegúrate de que el archivo `requirements.txt` esté en la raíz del proyecto.
    ```bash
    pip install -r requirements.txt
    ```

### 2. Ejecución del Servidor

Con el entorno activado y las dependencias instaladas, inicia la aplicación:

```bash
python app.py