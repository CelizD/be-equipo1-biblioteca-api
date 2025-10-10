# src/models/libros.py

# Importa la clase Autor para usarla en el type hint del constructor.
from .autor import Autor

class Libro:
    """
    Clase que representa un Libro dentro de una colección o biblioteca.
    """
    def __init__(self, titulo: str, autor: Autor, genero: str, paginas: int, año: int, idioma: str = "Español", disponible: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.paginas = paginas
        self.año = año
        self.idioma = idioma
        self.disponible = disponible

    def to_dict(self):
        """
        Convierte la instancia del libro a un diccionario, incluyendo
        la representación del autor como diccionario.
        """
        return {
            "titulo": self.titulo,
            "autor": self.autor.to_dict(), # Se llama al método to_dict() del autor
            "genero": self.genero,
            "paginas": self.paginas,
            "año": self.año,
            "idioma": self.idioma,
            "disponible": self.disponible
        }