# Título del Proyecto:Biblioteca Universitaria

---

## Integrantes del Equipo

| Nombre Completo             | Matrícula |
| --------------------------- | --------- |
| CELIZ MARTINEZ DANIEL       | 23030536  |
| RIVERA BARRERA PAUL         | 23030497  |
| ISMAEL CERVANTES CARRANZA   | 23030705  |

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
