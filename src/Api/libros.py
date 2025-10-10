# src/Api/libros.py

from flask import Blueprint, jsonify, request

# Importaciones relativas de los modelos Libro y Autor
from ..models.libros import Libro
from ..models.autor import Autor

# --- Creación del Blueprint para los endpoints de libros ---
blueprint = Blueprint('libros', __name__)

# --- Base de Datos en Memoria ---
# Diccionario de autores existentes
autores = {
    "Gabriel García Márquez": Autor(nombre="Gabriel García Márquez", nacionalidad="Colombiano"),
    "Antoine de Saint-Exupéry": Autor(nombre="Antoine de Saint-Exupéry", nacionalidad="Francés"),
    "Miguel de Cervantes": Autor(nombre="Miguel de Cervantes", nacionalidad="Español")
}

# Lista de libros existentes con referencia al autor correspondiente
libros: list[Libro] = [
    Libro("Cien años de soledad", autores["Gabriel García Márquez"], "Realismo mágico", 471, 1967),
    Libro("El principito", autores["Antoine de Saint-Exupéry"], "Fábula", 96, 1943),
    Libro("Don Quijote de la Mancha", autores["Miguel de Cervantes"], "Novela", 863, 1605),
]

# --- Endpoints de la API ---

@blueprint.route('/', methods=['GET'])
def get_libros():
    """
    Endpoint GET / 
    Retorna la lista completa de libros en formato JSON.
    Se usa el método to_dict() de cada libro para convertirlo a diccionario.
    """
    return jsonify([libro.to_dict() for libro in libros])

@blueprint.route('/<string:titulo>', methods=['GET'])
def get_libro(titulo: str):
    """
    Endpoint GET /<titulo>
    Busca un libro por su título (insensible a mayúsculas/minúsculas)
    Retorna el libro en formato JSON si se encuentra, o un error 404 si no existe.
    """
    libro = next((l for l in libros if l.titulo.lower() == titulo.lower()), None)
    if libro:
        return jsonify(libro.to_dict())
    return jsonify({"error": "Libro no encontrado"}), 404

@blueprint.route('/', methods=['POST'])
def agregar_libro():
    """
    Endpoint POST /
    Agrega un nuevo libro a la base de datos en memoria.
    Valida que existan todos los campos requeridos.
    Si el autor no existe, lo crea.
    Retorna el libro agregado con código 201 o errores 400/409 según el caso.
    """
    data = request.get_json()
    required_fields = {"titulo", "autor", "genero", "paginas", "año"}
    if not data or not required_fields.issubset(data) or "nombre" not in data.get("autor", {}):
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    # Verificar si ya existe un libro con el mismo título
    if any(l.titulo.lower() == data["titulo"].lower() for l in libros):
        return jsonify({"error": "Ya existe un libro con ese título"}), 409

    # Manejo del autor
    nombre_autor = data["autor"]["nombre"]
    if nombre_autor in autores:
        autor_obj = autores[nombre_autor]
    else:
        autor_obj = Autor(nombre=nombre_autor, nacionalidad=data["autor"].get("nacionalidad", "N/A"))
        autores[nombre_autor] = autor_obj

    # Creación del nuevo libro y agregado a la lista
    nuevo_libro = Libro(
        titulo=data["titulo"], autor=autor_obj, genero=data["genero"],
        paginas=data["paginas"], año=data["año"]
    )
    libros.append(nuevo_libro)
    return jsonify({"mensaje": "Libro agregado", "libro": nuevo_libro.to_dict()}), 201

@blueprint.route('/<string:titulo>', methods=['PUT'])
def actualizar_libro(titulo: str):
    """
    Endpoint PUT /<titulo>
    Actualiza los datos de un libro existente.
    Permite modificar género, páginas, año y disponibilidad.
    Retorna el libro actualizado o error 404 si no se encuentra.
    """
    libro = next((l for l in libros if l.titulo.lower() == titulo.lower()), None)
    if not libro:
        return jsonify({"error": "Libro no encontrado"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No se proporcionaron datos"}), 400

    # Actualización de campos opcionales
    libro.genero = data.get("genero", libro.genero)
    libro.paginas = data.get("paginas", libro.paginas)
    libro.año = data.get("año", libro.año)
    libro.disponible = data.get("disponible", libro.disponible)

    return jsonify({"mensaje": "Libro actualizado", "libro": libro.to_dict()})

@blueprint.route('/<string:titulo>', methods=['DELETE'])
def eliminar_libro(titulo: str):
    """
    Endpoint DELETE /<titulo>
    Elimina un libro de la lista por su título.
    Retorna mensaje de éxito o error 404 si el libro no existe.
    """
    libro_a_eliminar = next((l for l in libros if l.titulo.lower() == titulo.lower()), None)
    if not libro_a_eliminar:
        return jsonify({"error": "Libro no encontrado"}), 404
    
    libros.remove(libro_a_eliminar)
    return jsonify({"mensaje": f"Libro '{titulo}' eliminado"})
