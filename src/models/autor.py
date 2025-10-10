from .trainer import Trainer
from .libros import libros 

# src/models/autor.py

class Autor:
    """
    Clase que representa a un Autor de un libro.
    """
    def __init__(self, nombre: str, nacionalidad: str):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def to_dict(self):
        """Convierte la instancia del autor a un diccionario."""
        return {
            "nombre": self.nombre,
            "nacionalidad": self.nacionalidad
        }