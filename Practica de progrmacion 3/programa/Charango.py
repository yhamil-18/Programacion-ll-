import pickle

class Charango:
    def __init__(self, material, nroCuerdas):
        self.material = material
        self.nroCuerdas = nroCuerdas
        self.cuerdas = [True] * nroCuerdas + [False] * (10 - nroCuerdas)
    
    def __str__(self):
        return f"Charango de {self.material} con {self.nroCuerdas} cuerdas activas"

def crear_archivo():
    charangos = [
        Charango("madera", 8),
        Charango("plastico", 5),
        Charango("madera", 10),
        Charango("metal", 3),
        Charango("plastico", 10),
        Charango("madera", 4),
        Charango("metal", 10)
    ]
    
    charangos[1].cuerdas = [False] * 7 + [True] * 3  
    charangos[3].cuerdas = [False] * 8 + [True] * 2  
    
    with open("charangos.dat", "wb") as f:
        pickle.dump(charangos, f)
    
    print("Archivo creado con 7 charangos de ejemplo")
    return charangos

def eliminar_mas_de_6_falsos(charangos):
    nuevos_charangos = []
    eliminados = []
    
    for c in charangos:
        falsas = c.cuerdas.count(False)
        if falsas > 6:
            eliminados.append(c)
        else:
            nuevos_charangos.append(c)
    
    print(f"Eliminados {len(eliminados)} charangos:")
    for c in eliminados:
        print(f"  - {c} (cuerdas falsas: {c.cuerdas.count(False)})")
    
    return nuevos_charangos

def listar_por_material(charangos, material):
    print(f"\nCharangos de {material}:")
    encontrados = False
    for c in charangos:
        if c.material.lower() == material.lower():
            print(f"  - {c}")
            encontrados = True
    
    if not encontrados:
        print(f"  No hay charangos de {material}")

def buscar_10_cuerdas(charangos):
    print("\nCharangos con 10 cuerdas:")
    for c in charangos:
        if c.nroCuerdas == 10:
            print(f"  - {c}")

def ordenar_por_material(charangos):
    return sorted(charangos, key=lambda x: x.material)


def mostrar_todos(charangos, titulo="Todos los charangos:"):
    print(f"\n{titulo}")
    for i, c in enumerate(charangos, 1):
        falsas = c.cuerdas.count(False)
        print(f"{i}. {c} (cuerdas falsas: {falsas})")


try:
    with open("charangos.dat", "rb") as f:
        charangos = pickle.load(f)
    print("Archivo cargado exitosamente")
except:
    print("Creando nuevo archivo")
    charangos = crear_archivo()

mostrar_todos(charangos, "Charangos iniciales:")

charangos = eliminar_mas_de_6_falsos(charangos)

with open("charangos.dat", "wb") as f:
    pickle.dump(charangos, f)

mostrar_todos(charangos, "\nDespués de eliminar:")

listar_por_material(charangos, "madera")
listar_por_material(charangos, "metal")

buscar_10_cuerdas(charangos)

charangos_ordenados = ordenar_por_material(charangos)
mostrar_todos(charangos_ordenados, "\nOrdenados por material:")

with open("charangos.dat", "wb") as f:
    pickle.dump(charangos_ordenados, f)
