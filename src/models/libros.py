# src/models/libros.py

# Importa la clase Autor para usarla en type hints y composición
from .autor import Autor

class Libro:
    """
    Representa un libro dentro de una colección o biblioteca.
    Contiene información como título, autor, género, número de páginas, año, idioma y disponibilidad.
    """
    def __init__(
        self, 
        titulo: str, 
        autor: Autor, 
        genero: str, 
        paginas: int, 
        año: int, 
        idioma: str = "Español", 
        disponible: bool = True
    ):
        # Título del libro
        self.titulo = titulo
        # Objeto Autor asociado al libro
        self.autor = autor
        # Género literario del libro
        self.genero = genero
        # Cantidad de páginas
        self.paginas = paginas
        # Año de publicación
        self.año = año
        # Idioma del libro (por defecto "Español")
        self.idioma = idioma
        # Disponibilidad para préstamo o venta
        self.disponible = disponible

    def to_dict(self):
        """
        Convierte la instancia del libro a un diccionario.
        Incluye la información del autor como diccionario mediante su método to_dict().
        Esto permite serializar el libro completo a JSON en la API.
        """
        return {
            "titulo": self.titulo,
            "autor": self.autor.to_dict(),  # Convierte el objeto Autor a diccionario
            "genero": self.genero,
            "paginas": self.paginas,
            "año": self.año,
            "idioma": self.idioma,
            "disponible": self.disponible
        }