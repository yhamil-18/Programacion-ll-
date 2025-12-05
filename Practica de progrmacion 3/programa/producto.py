import json

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: ${self.precio}"

class ArchivoProducto:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def crearArchivo(self):
        with open(self.nombre, "w") as f:
            json.dump([], f)
    
    def guardaProducto(self, p):
        try:
            with open(self.nombre, "r") as f:
                data = json.load(f)
        except:
            data = []
        
        nuevo = {"codigo": p.codigo, "nombre": p.nombre, "precio": p.precio}
        data.append(nuevo)
        
        with open(self.nombre, "w") as f:
            json.dump(data, f, indent=2)
    
    def buscaProducto(self, codigo):
        with open(self.nombre, "r") as f:
            data = json.load(f)
        
        for item in data:
            if item["codigo"] == codigo:
                return Producto(item["codigo"], item["nombre"], item["precio"])
        return None
    
    def promedioPrecios(self):
        with open(self.nombre, "r") as f:
            data = json.load(f)
        
        if not data:
            return 0
        
        suma = sum(item["precio"] for item in data)
        return suma / len(data)
    
    def productoMasCaro(self):
        with open(self.nombre, "r") as f:
            data = json.load(f)
        
        if not data:
            return None
        
        caro = max(data, key=lambda x: x["precio"])
        return Producto(caro["codigo"], caro["nombre"], caro["precio"])
    
    def mostrarTodos(self):
        with open(self.nombre, "r") as f:
            data = json.load(f)
        
        for item in data:
            p = Producto(item["codigo"], item["nombre"], item["precio"])
            print(p)

archivo = ArchivoProducto("productos.json")
archivo.crearArchivo()

p1 = Producto(101, "Laptop", 1500)
p2 = Producto(102, "Mouse", 25)
p3 = Producto(103, "Teclado", 45)

archivo.guardaProducto(p1)
archivo.guardaProducto(p2)
archivo.guardaProducto(p3)

print("Todos los productos:")
archivo.mostrarTodos()

print("\nBuscar código 102:")
resultado = archivo.buscaProducto(102)
print(resultado)

print(f"\nPromedio: ${archivo.promedioPrecios():.2f}")

print("\nProducto más caro:")
print(archivo.productoMasCaro())