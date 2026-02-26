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

class Usuario:
    def __init__(self, id_usuario, nombre, limite_prestamos=2):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.limite_prestamos = limite_prestamos
        self.prestamos = []

    def puede_prestar(self):
        return len(self.prestamos) < self.limite_prestamos

    def __str__(self):
        return f"[{self.id_usuario}] {self.nombre} | Préstamos: {len(self.prestamos)}/{self.limite_prestamos}"