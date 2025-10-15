# src/models/autor.py
from ..extensions import db

class Autor(db.Model):
    __tablename__ = 'autores'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    nacionalidad = db.Column(db.String(80))

    # Relación con libros (un autor puede tener muchos libros)
    libros = db.relationship('Libro', backref='autor', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "nacionalidad": self.nacionalidad
        }