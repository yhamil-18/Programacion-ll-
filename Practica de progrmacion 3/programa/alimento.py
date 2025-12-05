import json

class Alimento:
    def __init__(self, nombre="", fecha="", cantidad=0):
        self.nombre = nombre
        self.fecha = fecha
        self.cantidad = cantidad

class Refri:
    def __init__(self, archivo="refri.json"):
        self.archivo = archivo
        self.alimentos = []
        self.cargar()
    
    def guardar(self):
        datos = [a.__dict__ for a in self.alimentos]
        with open(self.archivo, 'w') as f:
            json.dump(datos, f)
    
    def cargar(self):
        try:
            with open(self.archivo, 'r') as f:
                datos = json.load(f)
                self.alimentos = [Alimento(**d) for d in datos]
        except:
            self.alimentos = []
    
    def agregar(self):
        nombre = input("Nombre: ")
        fecha = input("Fecha: ")
        cantidad = int(input("Cantidad: "))
        self.alimentos.append(Alimento(nombre, fecha, cantidad))
        self.guardar()
    
    def modificar(self, nombre):
        for a in self.alimentos:
            if a.nombre == nombre:
                a.fecha = input("Nueva fecha: ")
                a.cantidad = int(input("Nueva cantidad: "))
                self.guardar()
                return
    
    def eliminar(self, nombre):
        self.alimentos = [a for a in self.alimentos if a.nombre != nombre]
        self.guardar()
    
    def caducados_antes(self, fecha):
        for a in self.alimentos:
            if a.fecha < fecha:
                print(a.nombre, a.fecha)
    
    def eliminar_cero(self):
        self.alimentos = [a for a in self.alimentos if a.cantidad > 0]
        self.guardar()
    
    def buscar_vencidos(self, hoy):
        for a in self.alimentos:
            if a.fecha < hoy:
                print(a.nombre, "vencido")
    
    def mas_cantidad(self):
        if self.alimentos:
            return max(self.alimentos, key=lambda x: x.cantidad)
        return None

refri = Refri()

if not refri.alimentos:
    refri.alimentos = [
        Alimento("Leche", "2024-12-10", 2),
        Alimento("Pan", "2024-11-01", 0),
        Alimento("Queso", "2024-12-25", 5)
    ]
    refri.guardar()

print("Alimentos:")
for a in refri.alimentos:
    print(f"{a.nombre} - {a.fecha} - {a.cantidad}")

refri.modificar("Leche")
refri.eliminar("Pan")

print("\nCaducados antes 2024-12-20:")
refri.caducados_antes("2024-12-20")

refri.eliminar_cero()

print("\nVencidos hoy 2024-12-04:")
refri.buscar_vencidos("2024-12-04")

mas = refri.mas_cantidad()
if mas:
    print(f"\nMás cantidad: {mas.nombre} ({mas.cantidad})")