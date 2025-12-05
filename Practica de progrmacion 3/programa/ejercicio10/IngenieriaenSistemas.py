import json

class Empresa:
    def __init__(self, nombre="", rubro="", empleados=0):
        self.nombre = nombre
        self.rubro = rubro
        self.empleados = empleados

class Sistema:
    def __init__(self, archivo="empresas.json"):
        self.archivo = archivo
        self.empresas = []
        self.cargar()
    
    def cargar(self):
        try:
            with open(self.archivo, 'r') as f:
                datos = json.load(f)
                self.empresas = [Empresa(**d) for d in datos]
        except:
            self.empresas = []
    
    def guardar(self):
        datos = [e.__dict__ for e in self.empresas]
        with open(self.archivo, 'w') as f:
            json.dump(datos, f, indent=2)
    
    def agregar_empresa(self):
        nombre = input("Nombre empresa: ")
        rubro = input("Rubro: ")
        empleados = int(input("Número empleados: "))
        
        empresa = Empresa(nombre, rubro, empleados)
        self.empresas.append(empresa)
        self.guardar()
        print("Empresa agregada")
    
    def mostrar_todas(self):
        for empresa in self.empresas:
            print(f"{empresa.nombre} - Rubro: {empresa.rubro}, Empleados: {empresa.empleados}")
    
    def buscar_empresa(self, nombre):
        for empresa in self.empresas:
            if empresa.nombre.lower() == nombre.lower():
                print(f"Encontrado: {empresa.nombre} - {empresa.empleados} empleados")
                return
        print("No encontrado")

sistema = Sistema()

if not sistema.empresas:
    sistema.empresas = [
        Empresa("TechCorp", "Tecnología", 500),
        Empresa("FoodExpress", "Alimentos", 150),
        Empresa("BuildRight", "Construcción", 300)
    ]
    sistema.guardar()

print("\nMostrar todas")
sistema.mostrar_todas()

print("\nBuscar empresa 'TechCorp'")
sistema.buscar_empresa("TechCorp")

print("\nAgregar nueva empresa")
sistema.agregar_empresa()