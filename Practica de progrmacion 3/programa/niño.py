import json

class Persona:
    def __init__(self, nombre="", paterno="", materno="", ci=""):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.ci = ci

class Nino:
    def __init__(self):
        self.persona = Persona()
        self.edad = 0
        self.peso = 0
        self.talla = 0

class ArchNino:
    def __init__(self, archivo="ninos.json"):
        self.archivo = archivo
        self.ninos = []
        self.cargar()
    
    def guardar(self):
        datos = []
        for n in self.ninos:
            datos.append({
                'nombre': n.persona.nombre,
                'paterno': n.persona.paterno,
                'materno': n.persona.materno,
                'ci': n.persona.ci,
                'edad': n.edad,
                'peso': n.peso,
                'talla': n.talla
            })
        with open(self.archivo, 'w') as f:
            json.dump(datos, f, indent=2)
    
    def cargar(self):
        try:
            with open(self.archivo, 'r') as f:
                datos = json.load(f)
                for d in datos:
                    nino = Nino()
                    nino.persona = Persona(d['nombre'], d['paterno'], d['materno'], d['ci'])
                    nino.edad = d['edad']
                    nino.peso = d['peso']
                    nino.talla = d['talla']
                    self.ninos.append(nino)
        except:
            self.ninos = []
    
    def agregar(self):
        nino = Nino()
        nino.persona.nombre = input("Nombre: ")
        nino.persona.paterno = input("Paterno: ")
        nino.persona.materno = input("Materno: ")
        nino.persona.ci = input("CI: ")
        nino.edad = int(input("Edad: "))
        nino.peso = float(input("Peso: "))
        nino.talla = float(input("Talla: "))
        self.ninos.append(nino)
        self.guardar()
    
    def listar(self):
        for n in self.ninos:
            print(f"{n.persona.nombre} {n.persona.paterno} - Edad: {n.edad}, Peso: {n.peso}, Talla: {n.talla}")
    
    def mostrar(self, ci):
        for n in self.ninos:
            if n.persona.ci == ci:
                print(f"CI: {n.persona.ci}")
                print(f"Nombre: {n.persona.nombre} {n.persona.paterno} {n.persona.materno}")
                print(f"Edad: {n.edad}")
                print(f"Peso: {n.peso}")
                print(f"Talla: {n.talla}")
                return
        print("No encontrado")
    
    def peso_adecuado(self):
        count = 0
        for n in self.ninos:
            peso_min = n.edad * 2
            peso_max = n.edad * 3
            if peso_min <= n.peso <= peso_max:
                count += 1
        return count
    
    def inadecuados(self):
        for n in self.ninos:
            peso_min = n.edad * 2
            peso_max = n.edad * 3
            talla_min = 70 + n.edad * 6
            if n.peso < peso_min or n.peso > peso_max or n.talla < talla_min:
                print(f"{n.persona.nombre}: Edad {n.edad}, Peso {n.peso}, Talla {n.talla}")
    
    def promedio_edad(self):
        if not self.ninos:
            return 0
        total = sum(n.edad for n in self.ninos)
        return total / len(self.ninos)
    
    def buscar(self, ci):
        for n in self.ninos:
            if n.persona.ci == ci:
                return n
        return None
    
    def talla_alta(self):
        if not self.ninos:
            return []
        max_talla = max(n.talla for n in self.ninos)
        return [n for n in self.ninos if n.talla == max_talla]

arch = ArchNino()

if not arch.ninos:
    n1 = Nino()
    n1.persona = Persona("Juan", "Perez", "Gomez", "111")
    n1.edad = 5
    n1.peso = 18
    n1.talla = 110
    arch.ninos.append(n1)
    
    n2 = Nino()
    n2.persona = Persona("Maria", "Lopez", "Rod", "222")
    n2.edad = 7
    n2.peso = 25
    n2.talla = 125
    arch.ninos.append(n2)
    
    arch.guardar()

print("Listar:")
arch.listar()

print(f"\nPeso adecuado: {arch.peso_adecuado()}")

print("\nInadecuados:")
arch.inadecuados()

print(f"\nPromedio edad: {arch.promedio_edad()}")

print("\nBuscar CI 111:")
arch.mostrar("111")

print("\nTalla más alta:")
for n in arch.talla_alta():
    print(f"{n.persona.nombre}: {n.talla} cm")