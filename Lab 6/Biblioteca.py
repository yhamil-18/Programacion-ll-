from datetime import datetime, timedelta
import json

class Pagina:
    def __init__(self, numero_pagina, contenido_pagina):
        self.numero = numero_pagina
        self.contenido = contenido_pagina

class Libro:
    def __init__(self, titulo, isbn, contenido_paginas):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = []
        for i, contenido in enumerate(contenido_paginas, 1):
            self.paginas.append(Pagina(i, contenido))
        self.disponible = True
    
    def getTitulo(self):
        return self.titulo
    
    def getIsbn(self):
        return self.isbn
    
    def estaDisponible(self):
        return self.disponible
    
    def prestar(self):
        self.disponible = False
    
    def devolver(self):
        self.disponible = True

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    
    def getNombre(self):
        return self.nombre
    
    def getNacionalidad(self):
        return self.nacionalidad

class Estudiante:
    def __init__(self, codigo_estudiante, nombre):
        self.codigo = codigo_estudiante
        self.nombre = nombre
        self.libros_prestados = []
    
    def getCodigo(self):
        return self.codigo
    
    def getNombre(self):
        return self.nombre
    
    def getLibrosPrestados(self):
        return self.libros_prestados
    
    def agregarLibroPrestado(self, libro):
        self.libros_prestados.append(libro)
    
    def devolverLibro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

class Prestamo:
    def __init__(self, estudiante, libro):
        self.id = f"P{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.fecha_prestamo = datetime.now()
        self.estudiante = estudiante
        self.libro = libro
    
    def getId(self):
        return self.id
    
    def getLibro(self):
        return self.libro
    
    def getEstudiante(self):
        return self.estudiante
    
    def getFechaPrestamo(self):
        return self.fecha_prestamo.strftime('%d/%m/%Y %H:%M:%S')

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.autores = []
        self.estudiantes = []
        self.prestamos = []
    
    def agregarLibro(self, libro):
        self.libros.append(libro)
        return f"Libro '{libro.titulo}' agregado exitosamente a la biblioteca"
    
    def agregarAutor(self, autor):
        self.autores.append(autor)
        return f"Autor '{autor.nombre}' registrado exitosamente en la biblioteca"
    
    def agregarEstudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        return f"Estudiante '{estudiante.nombre}' registrado exitosamente"
    
    def prestarLibro(self, estudiante, libro):
        if libro in self.libros and libro.estaDisponible():
            libro.prestar()
            estudiante.agregarLibroPrestado(libro)
            prestamo = Prestamo(estudiante, libro)
            self.prestamos.append(prestamo)
            return f"Libro '{libro.getTitulo()}' prestado a {estudiante.getNombre()}"
        else:
            return f"El libro '{libro.getTitulo()}' no está disponible"
    
    def buscar_libro_por_isbn(self, isbn):
        for libro in self.libros:
            if libro.getIsbn() == isbn:
                return libro
        return None
    
    def buscar_estudiante_por_codigo(self, codigo):
        for estudiante in self.estudiantes:
            if estudiante.getCodigo() == codigo:
                return estudiante
        return None
    
    def listar_libros(self):
        if not self.libros:
            return "No hay libros registrados.\n"
        
        resultado = "LIBROS DISPONIBLES\n" + "="*50 + "\n\n"
        for libro in self.libros:
            disponible = "DISPONIBLE" if libro.estaDisponible() else "PRESTADO"
            resultado += f"• {libro.getTitulo()} (ISBN: {libro.getIsbn()}) - {disponible}\n"
        return resultado
    
    def listar_autores(self):
        if not self.autores:
            return "No hay autores registrados.\n"
        
        resultado = "AUTORES REGISTRADOS\n" + "="*50 + "\n\n"
        for autor in self.autores:
            resultado += f"• {autor.getNombre()} - {autor.getNacionalidad()}\n"
        return resultado
    
    def listar_estudiantes(self):
        if not self.estudiantes:
            return "No hay estudiantes registrados.\n"
        
        resultado = "ESTUDIANTES REGISTRADOS\n" + "="*50 + "\n\n"
        for estudiante in self.estudiantes:
            resultado += f"• {estudiante.getNombre()} - Código: {estudiante.getCodigo()}\n"
        return resultado
    
    def listar_prestamos(self):
        if not self.prestamos:
            return "No hay préstamos activos.\n"
        
        resultado = "PRÉSTAMOS ACTIVOS\n" + "="*50 + "\n\n"
        for prestamo in self.prestamos:
            resultado += f"• {prestamo.getLibro().getTitulo()} prestado a {prestamo.getEstudiante().getNombre()}\n"
        return resultado
    
    def mostrarEstado(self):
        resultado = f"=== ESTADO DE LA BIBLIOTECA: {self.nombre} ===\n\n"
        resultado += f"Autores: {len(self.autores)}\n"
        resultado += f"Libros: {len(self.libros)}\n"
        resultado += f"Estudiantes: {len(self.estudiantes)}\n"
        resultado += f"Préstamos: {len(self.prestamos)}\n"
        return resultado
    
    def cerrarBiblioteca(self):
        for prestamo in self.prestamos:
            libro = prestamo.getLibro()
            libro.devolver()
            estudiante = prestamo.getEstudiante()
            estudiante.devolverLibro(libro)
        
        self.prestamos.clear()
        return "Biblioteca cerrada. Préstamos eliminados."
    
    def guardar_datos(self):
        try:
            datos = {
                'libros': [
                    {'titulo': l.getTitulo(), 'isbn': l.getIsbn(), 'disponible': l.estaDisponible()}
                    for l in self.libros
                ],
                'autores': [
                    {'nombre': a.getNombre(), 'nacionalidad': a.getNacionalidad()}
                    for a in self.autores
                ],
                'estudiantes': [
                    {'codigo': e.getCodigo(), 'nombre': e.getNombre()}
                    for e in self.estudiantes
                ]
            }
            
            with open('biblioteca.json', 'w', encoding='utf-8') as f:
                json.dump(datos, f, ensure_ascii=False, indent=2)
            
            return True, "Datos guardados exitosamente"
            
        except Exception as e:
            return False, f"Error al guardar datos: {e}"
    
    def cargar_datos(self):
        try:
            with open('biblioteca.json', 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            for libro_data in datos.get('libros', []):
                paginas = [f"Contenido página {i+1}" for i in range(3)]
                libro = Libro(libro_data['titulo'], libro_data['isbn'], paginas)
                if not libro_data['disponible']:
                    libro.prestar()
                self.libros.append(libro)

            for autor_data in datos.get('autores', []):
                autor = Autor(autor_data['nombre'], autor_data['nacionalidad'])
                self.autores.append(autor)
            
            for estudiante_data in datos.get('estudiantes', []):
                estudiante = Estudiante(estudiante_data['codigo'], estudiante_data['nombre'])
                self.estudiantes.append(estudiante)
            
            return True, "Datos cargados exitosamente"
            
        except FileNotFoundError:
            return True, "No se encontró archivo de datos previo"
        except Exception as e:
            return False, f"Error al cargar datos: {e}"


print("PRUEBA DEL SISTEMA DE BIBLIOTECA")
print("=" * 40)

biblioteca = Biblioteca("Biblioteca Central UMSA")

autor1 = Autor("Gabriel García Márquez", "Colombiana")
autor2 = Autor("Isabel Allende", "Chilena")

libro1 = Libro("Cien Años de Soledad", "978-8437604947", 
              ["Página 1: Muchos años después...", "Página 2: Continuación..."])
libro2 = Libro("La Casa de los Espíritus", "978-8401332081", 
              ["Página 1: Capítulo 1", "Página 2: Capítulo 2"])

estudiante1 = Estudiante("2024001", "Ana María Torres")
estudiante2 = Estudiante("2024002", "Carlos López")

print("\nAGREGANDO ELEMENTOS:")
print(biblioteca.agregarAutor(autor1))
print(biblioteca.agregarAutor(autor2))
print(biblioteca.agregarLibro(libro1))
print(biblioteca.agregarLibro(libro2))
print(biblioteca.agregarEstudiante(estudiante1))
print(biblioteca.agregarEstudiante(estudiante2))

print("\nREALIZANDO PRÉSTAMOS:")
print(biblioteca.prestarLibro(estudiante1, libro1))
print(biblioteca.prestarLibro(estudiante2, libro2))

print("\n ESTADO DE LA BIBLIOTECA:")
print(biblioteca.mostrarEstado())

print("\nLISTADO DE LIBROS:")
print(biblioteca.listar_libros())

print("\n LISTADO DE AUTORES:")
print(biblioteca.listar_autores())

print("\nLISTADO DE ESTUDIANTES:")
print(biblioteca.listar_estudiantes())

print("\n LISTADO DE PRÉSTAMOS:")
print(biblioteca.listar_prestamos())

print("\n GUARDAR DATOS:")
exito, mensaje = biblioteca.guardar_datos()
print(mensaje)

print("\n CERRAR BIBLIOTECA:")
print(biblioteca.cerrarBiblioteca())

print("\n CARGAR DATOS:")
exito, mensaje = biblioteca.cargar_datos()
print(mensaje)

print("\nPRUEBA FINALIZADA")