from .trainer import Trainer
from .libros import libros 

class Tijuaball:
    def __init__(self, trainer: Trainer = None):
        self.owner = trainer
        self.captured_tijuamones: list[libros] = []