# src/models/autor.py

class Autor:
    """
    Representa a un autor de libro.
    Contiene información básica: nombre y nacionalidad.
    """
    def __init__(self, nombre: str, nacionalidad: str):
        # Nombre completo del autor
        self.nombre = nombre
        # Nacionalidad del autor
        self.nacionalidad = nacionalidad

    def to_dict(self):
        """
        Convierte la instancia del autor a un diccionario.
        Útil para serializar a JSON en la API.
        """
        return {
            "nombre": self.nombre,
            "nacionalidad": self.nacionalidad
        }
