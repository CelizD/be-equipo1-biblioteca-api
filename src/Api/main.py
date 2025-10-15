# src/api/main.py

from flask import Blueprint, render_template

# --- Creación del Blueprint ---
blueprint = Blueprint('main', __name__)

@blueprint.route('/')
def index():
    """
    Endpoint principal que renderiza la página de inicio.
    """
    return render_template('index.html')