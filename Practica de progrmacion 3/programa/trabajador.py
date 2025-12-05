import pickle

class Trabajador:
    def __init__(self, nombre, carnet, salario):
        self.nombre = nombre
        self.carnet = carnet
        self.salario = salario
    
    def __str__(self):
        return f"{self.nombre} (CI: {self.carnet}) - ${self.salario}"

class ArchivoTrabajador:
    def __init__(self):
        self.nombreArch = "trabajadores.dat"

    def crearArchivo(self):
        with open(self.nombreArch, "wb") as f:
            pickle.dump([], f)
        print("Archivo creado")

    def guardarTrabajador(self, t):
        try:
            with open(self.nombreArch, "rb") as f:
                trabajadores = pickle.load(f)
        except:
            trabajadores = []
        
        trabajadores.append(t)
        
        with open(self.nombreArch, "wb") as f:
            pickle.dump(trabajadores, f)

    def aumentaSalario(self, aumento, nombre_trabajador):
        with open(self.nombreArch, "rb") as f:
            trabajadores = pickle.load(f)
        
        for t in trabajadores:
            if t.nombre == nombre_trabajador:
                t.salario += aumento
        
        with open(self.nombreArch, "wb") as f:
            pickle.dump(trabajadores, f)

    def buscarMayorSalario(self):
        with open(self.nombreArch, "rb") as f:
            trabajadores = pickle.load(f)
        
        if not trabajadores:
            return None
        
        mayor = max(trabajadores, key=lambda x: x.salario)
        return mayor

    def ordenarPorSalario(self):
        with open(self.nombreArch, "rb") as f:
            trabajadores = pickle.load(f)
        
        trabajadores.sort(key=lambda x: x.salario)
        
        with open(self.nombreArch, "wb") as f:
            pickle.dump(trabajadores, f)

    def mostrarTodos(self):
        with open(self.nombreArch, "rb") as f:
            trabajadores = pickle.load(f)
        
        print("\n--- LISTA DE TRABAJADORES ---")
        for t in trabajadores:
            print(t)


archivo = ArchivoTrabajador()
archivo.crearArchivo()

t1 = Trabajador("Ana", 1001, 2500)
t2 = Trabajador("Luis", 1002, 3200)
t3 = Trabajador("Carlos", 1003, 1800)

archivo.guardarTrabajador(t1)
archivo.guardarTrabajador(t2)
archivo.guardarTrabajador(t3)
print("3 trabajadores guardados")

archivo.mostrarTodos()

print("\n--- Aumentar salario de Ana en 500 ---")
archivo.aumentaSalario(500, "Ana")
archivo.mostrarTodos()

print("\n--- Buscar mayor salario ---")
mayor = archivo.buscarMayorSalario()
print(f"Mayor salario: {mayor}")

print("\n--- Ordenar por salario ---")
archivo.ordenarPorSalario()
archivo.mostrarTodos()

print("\n--- Agregar más trabajadores ---")
t4 = Trabajador("María", 1004, 4000)
t5 = Trabajador("Pedro", 1005, 1500)
archivo.guardarTrabajador(t4)
archivo.guardarTrabajador(t5)
archivo.mostrarTodos()

print("\n--- Ordenar nuevamente ---")
archivo.ordenarPorSalario()
archivo.mostrarTodos()

