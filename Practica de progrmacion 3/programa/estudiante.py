import json
from typing import List

class Estudiante:
    def __init__(self, ru: str, nombre: str, paterno: str, materno: str, edad: int):
        self.ru = ru
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
    
    def to_dict(self):
        return {
            'ru': self.ru,
            'nombre': self.nombre,
            'paterno': self.paterno,
            'materno': self.materno,
            'edad': self.edad
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['ru'], data['nombre'], data['paterno'], data['materno'], data['edad'])

class Nota:
    def __init__(self, materno: str, notaFinal: float, estudiante: Estudiante):
        self.materno = materno
        self.notaFinal = notaFinal
        self.estudiante = estudiante
    
    def to_dict(self):
        return {
            'materno': self.materno,
            'notaFinal': self.notaFinal,
            'estudiante': self.estudiante.to_dict()
        }
    
    @classmethod
    def from_dict(cls, data):
        estudiante = Estudiante.from_dict(data['estudiante'])
        return cls(data['materno'], data['notaFinal'], estudiante)

class ArchiNota:
    def __init__(self, nombreArchi: str = "notas.json"):
        self.nombreArchi = nombreArchi
        self.notas = []
        self.cargar_datos()
    
    def agregar_varios_estudiantes(self, estudiantes_data: List[dict]):
        for data in estudiantes_data:
            estudiante = Estudiante(
                data['ru'],
                data['nombre'],
                data['paterno'],
                data['materno'],
                data['edad']
            )
            nota = Nota(data['materia'], data['notaFinal'], estudiante)
            self.notas.append(nota)
        self.guardar_datos()
    
    def guardar_datos(self):
        datos = [nota.to_dict() for nota in self.notas]
        with open(self.nombreArchi, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
    
    def cargar_datos(self):
        try:
            with open(self.nombreArchi, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                self.notas = [Nota.from_dict(item) for item in datos]
        except FileNotFoundError:
            self.notas = []
    
    def obtener_promedio(self) -> float:
        if not self.notas:
            return 0.0
        total = sum(nota.notaFinal for nota in self.notas)
        return total / len(self.notas)
    
    def buscar_mejores_estudiantes(self) -> List[Nota]:
        if not self.notas:
            return []
        mejor_nota = max(nota.notaFinal for nota in self.notas)
        return [nota for nota in self.notas if nota.notaFinal == mejor_nota]
    
    def eliminar_por_materia(self, materia: str) -> int:
        cantidad_inicial = len(self.notas)
        self.notas = [nota for nota in self.notas if nota.materno != materia]
        eliminados = cantidad_inicial - len(self.notas)
        if eliminados > 0:
            self.guardar_datos()
        return eliminados
    
    def mostrar_todos(self):
        for nota in self.notas:
            est = nota.estudiante
            print(f"{est.ru}: {est.nombre} {est.paterno} - {nota.materno}: {nota.notaFinal}")

archivo = ArchiNota()

estudiantes_ejemplo = [
    {
        'ru': '1001',
        'nombre': 'Juan',
        'paterno': 'Perez',
        'materno': 'Gomez',
        'edad': 20,
        'materia': 'Matemáticas',
        'notaFinal': 85.5
    },
    {
        'ru': '1002',
        'nombre': 'Maria',
        'paterno': 'Lopez',
        'materno': 'Rodriguez',
        'edad': 21,
        'materia': 'Matemáticas',
        'notaFinal': 92.0
    },
    {
        'ru': '1003',
        'nombre': 'Carlos',
        'paterno': 'Garcia',
        'materno': 'Martinez',
        'edad': 19,
        'materia': 'Física',
        'notaFinal': 78.5
    }
]

archivo.agregar_varios_estudiantes(estudiantes_ejemplo)

print("Estudiantes:")
archivo.mostrar_todos()

print(f"\nPromedio: {archivo.obtener_promedio():.2f}")

mejores = archivo.buscar_mejores_estudiantes()
print("\nMejores estudiantes:")
for nota in mejores:
    est = nota.estudiante
    print(f"{est.nombre} {est.paterno}: {nota.notaFinal}")

eliminados = archivo.eliminar_por_materia("Matemáticas")
print(f"\nEliminados {eliminados} de Matemáticas")

print("\nDespués de eliminar:")
archivo.mostrar_todos()