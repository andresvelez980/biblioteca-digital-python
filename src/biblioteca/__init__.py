from src.biblioteca.libro import Libro
from src.biblioteca.usuario import Usuario
from src.biblioteca.prestamo import Prestamo
from src.biblioteca.biblioteca import Biblioteca


class Libro:
    def __init__(self, id_libro, titulo, autor, anio, genero):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.prestado = False

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"[{self.id_libro}] {self.titulo} - {self.autor} ({self.anio}) | {estado}"