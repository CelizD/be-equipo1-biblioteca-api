from flask import Flask, jsonify

app = Flask(__name__)

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

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "genero": self.genero,
            "paginas": self.paginas,
            "año": self.año,
            "idioma": self.idioma,
            "disponible": self.disponible
        }

# Ejemplo de libros
libros = [
    Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", 417, 1967),
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", 863, 1605)
]

@app.route('/libros', methods=['GET'])
def get_libros():
    return jsonify([libro.to_dict() for libro in libros])

if __name__ == '__main__':
    app.run(debug=True)