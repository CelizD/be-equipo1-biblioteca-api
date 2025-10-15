# src/Api/libros.py
from flask import Blueprint, jsonify, request
from ..models.libros import Libro
from ..models.autor import Autor
from ..extensions import db

blueprint = Blueprint('libros', __name__)

@blueprint.route('/', methods=['GET'])
def get_libros():
    """Retorna la lista completa de libros desde la BD."""
    libros = Libro.query.all()
    return jsonify([libro.to_dict() for libro in libros])

@blueprint.route('/<int:libro_id>', methods=['GET'])
def get_libro(libro_id: int):
    """Busca un libro por su ID."""
    libro = Libro.query.get_or_404(libro_id, description=f"Libro con id {libro_id} no encontrado")
    return jsonify(libro.to_dict())

@blueprint.route('/', methods=['POST'])
def agregar_libro():
    """Agrega un nuevo libro a la base de datos."""
    data = request.get_json()
    required_fields = {"titulo", "autor", "genero", "paginas", "año"}
    if not data or not required_fields.issubset(data) or "nombre" not in data.get("autor", {}):
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    if Libro.query.filter_by(titulo=data["titulo"]).first():
        return jsonify({"error": "Ya existe un libro con ese título"}), 409

    # Manejo del autor
    nombre_autor = data["autor"]["nombre"]
    autor = Autor.query.filter_by(nombre=nombre_autor).first()
    if not autor:
        autor = Autor(
            nombre=nombre_autor,
            nacionalidad=data["autor"].get("nacionalidad", "N/A")
        )
        db.session.add(autor)
        db.session.commit() # Guardamos el autor para obtener su ID

    nuevo_libro = Libro(
        titulo=data["titulo"],
        autor_id=autor.id, # Usamos el ID del autor
        genero=data["genero"],
        paginas=data["paginas"],
        año=data["año"]
    )
    db.session.add(nuevo_libro)
    db.session.commit()
    
    return jsonify({"mensaje": "Libro agregado", "libro": nuevo_libro.to_dict()}), 201

@blueprint.route('/<int:libro_id>', methods=['PUT'])
def actualizar_libro(libro_id: int):
    """Actualiza los datos de un libro existente."""
    libro = Libro.query.get_or_404(libro_id)
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se proporcionaron datos"}), 400

    libro.genero = data.get("genero", libro.genero)
    libro.paginas = data.get("paginas", libro.paginas)
    libro.año = data.get("año", libro.año)
    libro.disponible = data.get("disponible", libro.disponible)

    db.session.commit()
    return jsonify({"mensaje": "Libro actualizado", "libro": libro.to_dict()})

@blueprint.route('/<int:libro_id>', methods=['DELETE'])
def eliminar_libro(libro_id: int):
    """Elimina un libro de la base de datos."""
    libro = Libro.query.get_or_404(libro_id)
    db.session.delete(libro)
    db.session.commit()
    return jsonify({"mensaje": f"Libro '{libro.titulo}' eliminado"})