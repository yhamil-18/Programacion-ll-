import json
import hashlib

class Usuario:
    def __init__(self, username="", password=""):
        self.username = username
        self.password = password

class Seguridad:
    def __init__(self, archivo="usuarios.json"):
        self.archivo = archivo
        self.usuarios = []
        self.cargar()
    
    def cargar(self):
        try:
            with open(self.archivo, 'r') as f:
                datos = json.load(f)
                self.usuarios = [Usuario(**d) for d in datos]
        except:
            self.usuarios = []
    
    def guardar(self):
        datos = [u.__dict__ for u in self.usuarios]
        with open(self.archivo, 'w') as f:
            json.dump(datos, f, indent=2)
    
    def encriptar(self, texto):
        return hashlib.sha256(texto.encode()).hexdigest()
    
    def agregar_usuario(self):
        username = input("Usuario: ")
        password = input("Contraseña: ")
        
        usuario = Usuario(username, self.encriptar(password))
        self.usuarios.append(usuario)
        self.guardar()
        print("Usuario agregado (contraseña encriptada)")
    
    def mostrar_todos(self):
        for usuario in self.usuarios:
            print(f"Usuario: {usuario.username}, Contraseña (hash): {usuario.password[:20]}...")
    
    def buscar_usuario(self, username):
        for usuario in self.usuarios:
            if usuario.username.lower() == username.lower():
                print(f"Encontrado: {usuario.username}")
                return
        print("No encontrado")

seg = Seguridad()

if not seg.usuarios:
    seg.usuarios = [
        Usuario("admin", seg.encriptar("admin123")),
        Usuario("usuario1", seg.encriptar("clave456")),
        Usuario("invitado", seg.encriptar("guest789"))
    ]
    seg.guardar()

print("=== SISTEMA DE SEGURIDAD ===")
print("\nMostrar todos")
seg.mostrar_todos()

print("\nBuscar usuario 'admin'")
seg.buscar_usuario("admin")

print("\nAgregar nuevo usuario")
seg.agregar_usuario()