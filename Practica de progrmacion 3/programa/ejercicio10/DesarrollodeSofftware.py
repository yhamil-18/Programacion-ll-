import json

class Jugador:
    def __init__(self, nombre="", nivel=1, puntaje=0):
        self.nombre = nombre
        self.nivel = nivel
        self.puntaje = puntaje

class Videojuego:
    def __init__(self, archivo="jugadores.json"):
        self.archivo = archivo
        self.jugadores = []
        self.cargar()
    
    def cargar(self):
        try:
            with open(self.archivo, 'r') as f:
                datos = json.load(f)
                self.jugadores = [Jugador(**d) for d in datos]
        except:
            self.jugadores = []
    
    def guardar(self):
        datos = [j.__dict__ for j in self.jugadores]
        with open(self.archivo, 'w') as f:
            json.dump(datos, f, indent=2)
    
    def agregar_jugador(self):
        nombre = input("Nombre: ")
        nivel = int(input("Nivel: "))
        puntaje = int(input("Puntaje: "))
        
        jugador = Jugador(nombre, nivel, puntaje)
        self.jugadores.append(jugador)
        self.guardar()
        print("Jugador agregado")
    
    def mostrar_todos(self):
        for jugador in self.jugadores:
            print(f"{jugador.nombre} - Nivel: {jugador.nivel}, Puntaje: {jugador.puntaje}")
    
    def buscar_jugador(self, nombre):
        for jugador in self.jugadores:
            if jugador.nombre.lower() == nombre.lower():
                print(f"Encontrado: {jugador.nombre} - Nivel: {jugador.nivel}, Puntaje: {jugador.puntaje}")
                return
        print("No encontrado")

juego = Videojuego()

if not juego.jugadores:
    juego.jugadores = [
        Jugador("Carlos", 10, 1500),
        Jugador("Ana", 7, 950),
        Jugador("Luis", 12, 2100)
    ]
    juego.guardar()

print("\nMostrar todos")
juego.mostrar_todos()

print("\nBuscar jugador 'Ana'")
juego.buscar_jugador("Ana")

print("\nAgregar nuevo jugador")
juego.agregar_jugador()

print("\nTodos los jugadores después:")
juego.mostrar_todos()