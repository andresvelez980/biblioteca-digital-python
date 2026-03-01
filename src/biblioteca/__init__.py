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

class Biblioteca:
    def __init__(self):
        self.catalogo = {}
        self.usuarios = {}
        self.historial_prestamos = {}

    def registrar_libro(self, libro):
        if libro.id_libro in self.catalogo:
            print("El libro ya está registrado.")
        else:
            self.catalogo[libro.id_libro] = libro
            print("Libro registrado correctamente.")

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.id_usuario] = usuario

    def prestar(self, id_usuario, id_libro):
        if id_usuario not in self.usuarios or id_libro not in self.catalogo:
            print("Usuario o libro no existen.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.catalogo[id_libro]

        if libro.prestado:
            print("El libro ya está prestado.")
            return

        if not usuario.puede_prestar():
            print("El usuario alcanzó el límite de préstamos.")
            return

        libro.prestado = True
        usuario.prestamos.append(libro)

        evento = f"Usuario {usuario.nombre} prestó '{libro.titulo}'"
        self.historial_prestamos.setdefault88(id_usuario, []).append(evento)

        print("Préstamo realizado correctamente.")

    def devolver(self, id_usuario, id_libro):
        if id_usuario not in self.usuarios or id_libro not in self.catalogo:
            print("Usuario o libro no existen.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.catalogo[id_libro]

        if not libro.prestado:
            print("El libro no está prestado.")
            return

        if libro not in usuario.prestamos:
            print("Este usuario no tiene ese libro.")
            return

        libro.prestado = False
        usuario.prestamos.remove(libro)

        evento = f"Usuario {usuario.nombre} devolvió '{libro.titulo}'"
        self.historial_prestamos.setdefault(id_usuario, []).append(evento)

        print("Devolución realizada correctamente.")



