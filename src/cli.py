# src/cli.py
import click
from flask.cli import with_appcontext
from .extensions import db
from .models.autor import Autor
from .models.libros import Libro

@click.command(name='seed')
@with_appcontext
def seed():
    """
    Puebla la base de datos con datos iniciales.
    """
    # Evita duplicados: si ya hay un autor, asumimos que los datos ya existen.
    if Autor.query.first():
        click.echo('La base de datos ya contiene datos semilla.')
        return

    # --- Creación de Autores ---
    autor1 = Autor(nombre="Gabriel García Márquez", nacionalidad="Colombiano")
    autor2 = Autor(nombre="Antoine de Saint-Exupéry", nacionalidad="Francés")
    autor3 = Autor(nombre="Miguel de Cervantes", nacionalidad="Español")

    db.session.add_all([autor1, autor2, autor3])
    db.session.commit() # Guardamos para que los autores obtengan un ID

    # --- Creación de Libros ---
    libro1 = Libro(titulo="Cien años de soledad", autor_id=autor1.id, genero="Realismo mágico", paginas=471, año=1967)
    libro2 = Libro(titulo="El principito", autor_id=autor2.id, genero="Fábula", paginas=96, año=1943)
    libro3 = Libro(titulo="Don Quijote de la Mancha", autor_id=autor3.id, genero="Novela", paginas=863, año=1605)

    db.session.add_all([libro1, libro2, libro3])
    db.session.commit()

    click.echo('Base de datos poblada con datos semilla.')