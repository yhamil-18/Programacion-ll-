import json

class Animal:
    def __init__(self, especie="", nombre="", cantidad=0):
        self.especie = especie
        self.nombre = nombre
        self.cantidad = cantidad

class Zoo:
    def __init__(self, id_zoo=0, nombre=""):
        self.id = id_zoo
        self.nombre = nombre
        self.animales = []

class ArchZoo:
    def __init__(self, archivo="zoos.json"):
        self.archivo = archivo
        self.zoos = []
        self.cargar_datos()
    
    def cargar_datos(self):
        try:
            with open(self.archivo, 'r') as f:
                datos = json.load(f)
                for zoo_data in datos:
                    zoo = Zoo(zoo_data['id'], zoo_data['nombre'])
                    for animal_data in zoo_data['animales']:
                        animal = Animal(animal_data['especie'], animal_data['nombre'], animal_data['cantidad'])
                        zoo.animales.append(animal)
                    self.zoos.append(zoo)
        except:
            self.zoos = []
    
    def guardar_datos(self):
        datos = []
        for zoo in self.zoos:
            animales_data = []
            for animal in zoo.animales:
                animales_data.append({
                    'especie': animal.especie,
                    'nombre': animal.nombre,
                    'cantidad': animal.cantidad
                })
            datos.append({
                'id': zoo.id,
                'nombre': zoo.nombre,
                'animales': animales_data
            })
        with open(self.archivo, 'w') as f:
            json.dump(datos, f, indent=2)
    
    def crear_zoo(self):
        id_zoo = len(self.zoos) + 1
        nombre = f"Zoo {id_zoo}"
        zoo = Zoo(id_zoo, nombre)
        
        animal1 = Animal("Leon", f"Leon_{id_zoo}", 3)
        animal2 = Animal("Tigre", f"Tigre_{id_zoo}", 2)
        zoo.animales = [animal1, animal2]
        
        self.zoos.append(zoo)
        self.guardar_datos()
        print(f"Zoo {id_zoo} creado")
    
    def modificar_zoo(self, id_zoo):
        for zoo in self.zoos:
            if zoo.id == id_zoo:
                zoo.nombre = f"Zoo Modificado {id_zoo}"
                if zoo.animales:
                    zoo.animales[0].cantidad += 1
                self.guardar_datos()
                print(f"Zoo {id_zoo} modificado")
                return
        print(f"Zoo {id_zoo} no encontrado")
    
    def eliminar_zoo(self, id_zoo):
        self.zoos = [zoo for zoo in self.zoos if zoo.id != id_zoo]
        self.guardar_datos()
        print(f"Zoo {id_zoo} eliminado")
    
    def listar_mayor_variedad(self):
        if not self.zoos:
            return []
        
        max_variedad = max(len(zoo.animales) for zoo in self.zoos)
        return [zoo for zoo in self.zoos if len(zoo.animales) == max_variedad]
    
    def listar_y_eliminar_vacios(self):
        vacios = [zoo for zoo in self.zoos if len(zoo.animales) == 0]
        for zoo in vacios:
            print(f"Zoo {zoo.nombre} está vacío")
        
        self.zoos = [zoo for zoo in self.zoos if len(zoo.animales) > 0]
        if vacios:
            self.guardar_datos()
        return len(vacios)
    
    def mostrar_animales_especie(self, especie):
        print(f"Animales de especie '{especie}':")
        for zoo in self.zoos:
            for animal in zoo.animales:
                if animal.especie == especie:
                    print(f"  {zoo.nombre}: {animal.nombre} ({animal.cantidad})")
    
    def mover_animales(self, id_origen, id_destino):
        origen = None
        destino = None
        
        for zoo in self.zoos:
            if zoo.id == id_origen:
                origen = zoo
            if zoo.id == id_destino:
                destino = zoo
        
        if origen and destino:
            destino.animales.extend(origen.animales)
            origen.animales = []
            self.guardar_datos()
            print(f"Animales movidos de {origen.nombre} a {destino.nombre}")
    
    def mostrar_todos(self):
        for zoo in self.zoos:
            print(f"\n{zoo.nombre} (ID: {zoo.id}):")
            for animal in zoo.animales:
                print(f"  - {animal.nombre} ({animal.especie}): {animal.cantidad}")

archivo = ArchZoo()

if not archivo.zoos:
    zoo1 = Zoo(1, "Zoo Central")
    zoo1.animales.append(Animal("Leon", "Simba", 3))
    zoo1.animales.append(Animal("Tigre", "Rajah", 2))
    zoo1.animales.append(Animal("Elefante", "Dumbo", 1))
    
    zoo2 = Zoo(2, "Zoo Norte")
    zoo2.animales.append(Animal("Leon", "Mufasa", 2))
    
    zoo3 = Zoo(3, "Zoo Vacío")
    
    archivo.zoos = [zoo1, zoo2, zoo3]
    archivo.guardar_datos()

print("=== TODOS LOS ZOOS ===")
archivo.mostrar_todos()

print("\n=== CREAR ZOO ===")
archivo.crear_zoo()

print("\n=== MODIFICAR ZOO 1 ===")
archivo.modificar_zoo(1)

print("\n=== ELIMINAR ZOO 2 ===")
archivo.eliminar_zoo(2)

print("\n=== ZOOS CON MAYOR VARIEDAD ===")
mayor_variedad = archivo.listar_mayor_variedad()
for zoo in mayor_variedad:
    print(f"{zoo.nombre} con {len(zoo.animales)} especies")

print("\n=== ZOOS VACÍOS ===")
eliminados = archivo.listar_y_eliminar_vacios()
print(f"Eliminados {eliminados} zoológicos vacíos")

print("\n=== ANIMALES 'LEON' ===")
archivo.mostrar_animales_especie("Leon")

print("\n=== MOVER ANIMALES ===")
archivo.mover_animales(1, 4)

print("\n=== RESULTADO FINAL ===")
archivo.mostrar_todos()