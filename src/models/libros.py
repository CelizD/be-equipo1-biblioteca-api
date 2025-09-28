class Libro:
    """
    Clase que representa un Libro dentro de una colección o biblioteca.
    """
    def __init__(self, titulo: str, autor: str, genero: str, paginas: int, año: int, idioma: str = "Español", disponible: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.paginas = paginas
        self.año = año
        self.idioma = idioma
        self.disponible = disponible