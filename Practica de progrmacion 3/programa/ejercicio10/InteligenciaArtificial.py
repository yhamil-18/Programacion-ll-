import json

class Dataset:
    def __init__(self, nombre="", instancias=0, algoritmo=""):
        self.nombre = nombre
        self.instancias = instancias
        self.algoritmo = algoritmo

class IA:
    def __init__(self, archivo="datasets.json"):
        self.archivo = archivo
        self.datasets = []
        self.cargar()
    
    def cargar(self):
        try:
            with open(self.archivo, 'r') as f:
                datos = json.load(f)
                self.datasets = [Dataset(**d) for d in datos]
        except:
            self.datasets = []
    
    def guardar(self):
        datos = [d.__dict__ for d in self.datasets]
        with open(self.archivo, 'w') as f:
            json.dump(datos, f, indent=2)
    
    def agregar_dataset(self):
        nombre = input("Nombre dataset: ")
        instancias = int(input("Número instancias: "))
        algoritmo = input("Algoritmo recomendado: ")
        
        dataset = Dataset(nombre, instancias, algoritmo)
        self.datasets.append(dataset)
        self.guardar()
        print("Dataset agregado")
    
    def mostrar_todos(self):
        for dataset in self.datasets:
            print(f"{dataset.nombre} - Instancias: {dataset.instancias}, Algoritmo: {dataset.algoritmo}")
    
    def buscar_dataset(self, nombre):
        for dataset in self.datasets:
            if dataset.nombre.lower() == nombre.lower():
                print(f"Encontrado: {dataset.nombre} - {dataset.instancias} instancias")
                return
        print("No encontrado")

ia = IA()

if not ia.datasets:
    ia.datasets = [
        Dataset("MNIST", 70000, "Red Neuronal"),
        Dataset("Iris", 150, "SVM"),
        Dataset("Titanic", 891, "Árbol de Decisión")
    ]
    ia.guardar()

print("\nMostrar todos")
ia.mostrar_todos()

print("\nBuscar dataset 'Iris'")
ia.buscar_dataset("Iris")

print("\nAgregar nuevo dataset")
ia.agregar_dataset()