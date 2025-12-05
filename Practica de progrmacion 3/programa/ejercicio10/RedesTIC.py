import json

class Dispositivo:
    def __init__(self, mac="", nombre="", velocidad=0):
        self.mac = mac
        self.nombre = nombre
        self.velocidad = velocidad

class WiFi:
    def __init__(self, archivo="wifi.json"):
        self.archivo = archivo
        self.dispositivos = []
        self.cargar()
    
    def cargar(self):
        try:
            with open(self.archivo, 'r') as f:
                datos = json.load(f)
                self.dispositivos = [Dispositivo(**d) for d in datos]
        except:
            self.dispositivos = []
    
    def guardar(self):
        datos = [d.__dict__ for d in self.dispositivos]
        with open(self.archivo, 'w') as f:
            json.dump(datos, f, indent=2)
    
    def agregar_dispositivo(self):
        mac = input("Dirección MAC: ")
        nombre = input("Nombre dispositivo: ")
        velocidad = int(input("Velocidad (Mbps): "))
        
        dispositivo = Dispositivo(mac, nombre, velocidad)
        self.dispositivos.append(dispositivo)
        self.guardar()
        print("Dispositivo agregado")
    
    def mostrar_todos(self):
        for disp in self.dispositivos:
            print(f"MAC: {disp.mac} - {disp.nombre} - {disp.velocidad} Mbps")
    
    def buscar_dispositivo(self, mac):
        for disp in self.dispositivos:
            if disp.mac.lower() == mac.lower():
                print(f"Encontrado: {disp.nombre} - {disp.velocidad} Mbps")
                return
        print("No encontrado")

wifi = WiFi()

if not wifi.dispositivos:
    wifi.dispositivos = [
        Dispositivo("00:1A:2B:3C:4D:5E", "Laptop Carlos", 1200),
        Dispositivo("AA:BB:CC:DD:EE:FF", "Celular Ana", 800),
        Dispositivo("11:22:33:44:55:66", "Tablet Oficina", 600)
    ]
    wifi.guardar()

print("\nMostrar todos")
wifi.mostrar_todos()

print("\nBuscar dispositivo '00:1A:2B:3C:4D:5E'")
wifi.buscar_dispositivo("00:1A:2B:3C:4D:5E")

print("\nAgregar nuevo dispositivo")
wifi.agregar_dispositivo()