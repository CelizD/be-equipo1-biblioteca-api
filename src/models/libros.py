# src/models/libros.py
from ..extensions import db

class Libro(db.Model):
    __tablename__ = 'libros'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False, unique=True)
    genero = db.Column(db.String(100))
    paginas = db.Column(db.Integer)
    año = db.Column(db.Integer)
    idioma = db.Column(db.String(50), default="Español")
    disponible = db.Column(db.Boolean, default=True)

    # Llave foránea para la relación con Autor
    autor_id = db.Column(db.Integer, db.ForeignKey('autores.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor.to_dict(),  # Usa la relación `backref`
            "genero": self.genero,
            "paginas": self.paginas,
            "año": self.año,
            "idioma": self.idioma,
            "disponible": self.disponible
        }