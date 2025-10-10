from flask import Blueprint, jsonify, request
from src import Libro

blueprint = Blueprint('libros', __name__)

# Datos en memoria
libros: list[Libro] = [
    Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 471, 1967),
    Libro("El principito", "Antoine de Saint-Exupéry", "Fábula", 96, 1943),
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", 863, 1605),
]

def libro_to_dict(libro: Libro) -> dict:
    # Si tu clase Libro ya tiene un método to_dict, usa ese.
    return {
        "titulo": libro.titulo,
        "autor": libro.autor,
        "genero": libro.genero,
        "paginas": libro.paginas,
        "anio": libro.anio,
        "disponible": getattr(libro, "disponible", True)
    }

@blueprint.route('/', methods=['GET'])
def get_libros():
    """Devuelve la lista completa de libros."""
    return jsonify([libro_to_dict(libro) for libro in libros])

@blueprint.route('/<string:titulo>', methods=['GET'])
def get_libro(titulo: str):
    """Devuelve un libro por título."""
    libro = next((l for l in libros if l.titulo.lower() == titulo.lower()), None)
    if libro:
        return jsonify(libro_to_dict(libro))
    return jsonify({"error": "Libro no encontrado"}), 404

@blueprint.route('/', methods=['POST'])
def agregar_libro():
    """Agrega un nuevo libro a la colección."""
    data = request.get_json()
    required_fields = {"titulo", "autor", "genero", "paginas", "anio"}
    if not data or not required_fields.issubset(data):
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    if any(l.titulo.lower() == data["titulo"].lower() for l in libros):
        return jsonify({"error": "Ya existe un libro con ese título"}), 409

    try:
        nuevo_libro = Libro(**data)
        libros.append(nuevo_libro)
        return jsonify({"mensaje": "Libro agregado exitosamente", "libro": libro_to_dict(nuevo_libro)}), 201
    except Exception as e:
        return jsonify({"error": f"Error al agregar libro: {str(e)}"}), 400

@blueprint.route('/<string:titulo>', methods=['DELETE'])
def eliminar_libro(titulo: str):
    """Elimina un libro por su título."""
    libro = next((l for l in libros if l.titulo.lower() == titulo.lower()), None)
    if not libro:
        return jsonify({"error": "Libro no encontrado"}), 404
    libros.remove(libro)
    return jsonify({"mensaje": f"Libro '{titulo}' eliminado correctamente"})

@blueprint.route('/<string:titulo>', methods=['PUT'])
def actualizar_disponibilidad(titulo: str):
    """Cambia la disponibilidad de un libro."""
    libro = next((l for l in libros if l.titulo.lower() == titulo.lower()), None)
    if not libro:
        return jsonify({"error": "Libro no encontrado"}), 404

    data = request.get_json()
    if not data or 'disponible' not in data:
        return jsonify({"error": "El campo 'disponible' es obligatorio"}), 400
    
    try:
        libro.disponible = bool(data['disponible'])
        return jsonify({"mensaje": "Disponibilidad actualizada", "libro": libro_to_dict(libro)})
    except ValueError:
        return jsonify({"error": "El valor de 'disponible' debe ser un booleano (true/false)"}), 400