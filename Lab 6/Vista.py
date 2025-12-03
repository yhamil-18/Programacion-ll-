import tkinter as tk
from tkinter import ttk, simpledialog, scrolledtext
from Biblioteca import Biblioteca, Libro, Autor, Estudiante

class BibliotecaApp:
    def __init__(self, root):
        self.biblioteca = Biblioteca("Biblioteca Central")
        self.root = root
        self.root.title("Biblioteca")
        self.root.geometry("700x500")
        self.setup_ui()
    
    def setup_ui(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="BIBLIOTECA", font=('Arial', 14)).pack()
        
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0,10))
        
        buttons = [
            ("Libros", self.ver_libros),
            ("+Libro", self.agregar_libro),
            ("+Autor", self.agregar_autor),
            ("+Estudiante", self.agregar_estudiante),
            ("Estudiantes", self.ver_estudiantes),
            ("Prestar", self.prestar),
            ("Préstamos", self.ver_prestamos),
            ("Estado", self.ver_estado),
            ("Guardar", self.guardar),
            ("Cargar", self.cargar),
            ("Cerrar", self.cerrar)
        ]
        
        for text, cmd in buttons:
            ttk.Button(btn_frame, text=text, command=cmd, width=10).pack(pady=2)
        
        self.text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD)
        self.text_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.mostrar("Bienvenido")
    
    def mostrar(self, texto):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, texto)
    
    def agregar_libro(self):
        titulo = simpledialog.askstring("Libro", "Título:")
        isbn = simpledialog.askstring("Libro", "ISBN:")
        if titulo and isbn:
            libro = Libro(titulo, isbn, ["Página 1", "Página 2"])
            self.mostrar(self.biblioteca.agregarLibro(libro))
    
    def agregar_autor(self):
        nombre = simpledialog.askstring("Autor", "Nombre:")
        nacionalidad = simpledialog.askstring("Autor", "Nacionalidad:")
        if nombre and nacionalidad:
            autor = Autor(nombre, nacionalidad)
            self.mostrar(self.biblioteca.agregarAutor(autor))
    
    def agregar_estudiante(self):
        codigo = simpledialog.askstring("Estudiante", "Código:")
        nombre = simpledialog.askstring("Estudiante", "Nombre:")
        if codigo and nombre:
            estudiante = Estudiante(codigo, nombre)
            self.mostrar(self.biblioteca.agregarEstudiante(estudiante))
    
    def ver_libros(self):
        self.mostrar(self.biblioteca.listar_libros())
    
    def ver_estudiantes(self):
        self.mostrar(self.biblioteca.listar_estudiantes())
    
    def ver_prestamos(self):
        self.mostrar(self.biblioteca.listar_prestamos())
    
    def ver_estado(self):
        self.mostrar(self.biblioteca.mostrarEstado())
    
    def prestar(self):
        isbn = simpledialog.askstring("Préstamo", "ISBN:")
        codigo = simpledialog.askstring("Préstamo", "Código:")
        if isbn and codigo:
            libro = self.biblioteca.buscar_libro_por_isbn(isbn)
            estudiante = self.biblioteca.buscar_estudiante_por_codigo(codigo)
            if libro and estudiante:
                self.mostrar(self.biblioteca.prestarLibro(estudiante, libro))
            else:
                self.mostrar("No encontrado")
    
    def guardar(self):
        exito, msg = self.biblioteca.guardar_datos()
        self.mostrar(msg)
    
    def cargar(self):
        exito, msg = self.biblioteca.cargar_datos()
        self.mostrar(msg)
    
    def cerrar(self):
        self.mostrar(self.biblioteca.cerrarBiblioteca())

root = tk.Tk()
app = BibliotecaApp(root)
root.mainloop()