import json

class Libro:
    def __init__(self, codLibro="", titulo="", precio=0.0):
        self.codLibro = codLibro
        self.titulo = titulo
        self.precio = precio

class Cliente:
    def __init__(self, codCliente="", nombre="", apellido=""):
        self.codCliente = codCliente
        self.nombre = nombre
        self.apellido = apellido

class Prestamo:
    def __init__(self, codCliente="", codLibro="", fecha="", cantidad=0):
        self.codCliente = codCliente
        self.codLibro = codLibro
        self.fecha = fecha
        self.cantidad = cantidad

class Sistema:
    def __init__(self):
        self.libros = []
        self.clientes = []
        self.prestamos = []
    
    def guardar(self):
        libros_data = [l.__dict__ for l in self.libros]
        clientes_data = [c.__dict__ for c in self.clientes]
        prestamos_data = [p.__dict__ for p in self.prestamos]
        
        with open('libros.json', 'w') as f:
            json.dump(libros_data, f, indent=2)
        with open('clientes.json', 'w') as f:
            json.dump(clientes_data, f, indent=2)
        with open('prestamos.json', 'w') as f:
            json.dump(prestamos_data, f, indent=2)
    
    def cargar(self):
        try:
            with open('libros.json', 'r') as f:
                datos = json.load(f)
                self.libros = [Libro(**d) for d in datos]
        except:
            pass
        
        try:
            with open('clientes.json', 'r') as f:
                datos = json.load(f)
                self.clientes = [Cliente(**d) for d in datos]
        except:
            pass
        
        try:
            with open('prestamos.json', 'r') as f:
                datos = json.load(f)
                self.prestamos = [Prestamo(**d) for d in datos]
        except:
            pass
    
    def listar_precios(self, min_p, max_p):
        for libro in self.libros:
            if min_p <= libro.precio <= max_p:
                print(f"{libro.titulo}: ${libro.precio}")
    
    def ingreso_libro(self, cod_libro):
        total = 0
        libro_precio = 0
        
        for libro in self.libros:
            if libro.codLibro == cod_libro:
                libro_precio = libro.precio
                break
        
        for prestamo in self.prestamos:
            if prestamo.codLibro == cod_libro:
                total += prestamo.cantidad * libro_precio
        
        return total
    
    def libros_no_vendidos(self):
        vendidos = set()
        for prestamo in self.prestamos:
            vendidos.add(prestamo.codLibro)
        
        for libro in self.libros:
            if libro.codLibro not in vendidos:
                print(libro.titulo)
    
    def clientes_libro(self, cod_libro):
        clientes_ids = set()
        for prestamo in self.prestamos:
            if prestamo.codLibro == cod_libro:
                clientes_ids.add(prestamo.codCliente)
        
        for cliente in self.clientes:
            if cliente.codCliente in clientes_ids:
                print(cliente.nombre, cliente.apellido)
    
    def libro_mas_prestado(self):
        contador = {}
        for prestamo in self.prestamos:
            if prestamo.codLibro in contador:
                contador[prestamo.codLibro] += prestamo.cantidad
            else:
                contador[prestamo.codLibro] = prestamo.cantidad
        
        if contador:
            mas_prestado = max(contador, key=contador.get)
            return mas_prestado
        return ""
    
    def cliente_mas_prestamos(self):
        contador = {}
        for prestamo in self.prestamos:
            if prestamo.codCliente in contador:
                contador[prestamo.codCliente] += prestamo.cantidad
            else:
                contador[prestamo.codCliente] = prestamo.cantidad
        
        if contador:
            mas_prestamos = max(contador, key=contador.get)
            return mas_prestamos
        return ""

sistema = Sistema()

sistema.libros = [
    Libro("L1", "Python", 50),
    Libro("L2", "Java", 80),
    Libro("L3", "C++", 40)
]

sistema.clientes = [
    Cliente("C1", "Juan", "Perez"),
    Cliente("C2", "Maria", "Lopez")
]

sistema.prestamos = [
    Prestamo("C1", "L1", "2024-01-01", 2),
    Prestamo("C2", "L1", "2024-01-02", 1),
    Prestamo("C1", "L2", "2024-01-03", 3)
]

sistema.guardar()

print("Libros $40-$70:")
sistema.listar_precios(40, 70)

print(f"\nIngreso L1: {sistema.ingreso_libro('L1')}")

print("\nLibros no vendidos:")
sistema.libros_no_vendidos()

print("\nClientes libro L1:")
sistema.clientes_libro('L1')

print(f"\nLibro más prestado: {sistema.libro_mas_prestado()}")

print(f"\nCliente más préstamos: {sistema.cliente_mas_prestamos()}")