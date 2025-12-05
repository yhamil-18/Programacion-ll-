import json

class Transaccion:
    def __init__(self, id_trans="", monto=0.0, fecha=""):
        self.id = id_trans
        self.monto = monto
        self.fecha = fecha

class NFC:
    def __init__(self, archivo="nfc.json"):
        self.archivo = archivo
        self.transacciones = []
        self.cargar()
    
    def cargar(self):
        try:
            with open(self.archivo, 'r') as f:
                datos = json.load(f)
                self.transacciones = [Transaccion(**d) for d in datos]
        except:
            self.transacciones = []
    
    def guardar(self):
        datos = [t.__dict__ for t in self.transacciones]
        with open(self.archivo, 'w') as f:
            json.dump(datos, f, indent=2)
    
    def agregar_transaccion(self):
        id_trans = input("ID transacción: ")
        monto = float(input("Monto: "))
        fecha = input("Fecha (YYYY-MM-DD): ")
        
        transaccion = Transaccion(id_trans, monto, fecha)
        self.transacciones.append(transaccion)
        self.guardar()
        print("Transacción agregada")
    
    def mostrar_todas(self):
        for trans in self.transacciones:
            print(f"ID: {trans.id} - Monto: ${trans.monto} - Fecha: {trans.fecha}")
    
    def buscar_transaccion(self, id_trans):
        for trans in self.transacciones:
            if trans.id == id_trans:
                print(f"Encontrado: ID {trans.id} - ${trans.monto} el {trans.fecha}")
                return
        print("No encontrado")

nfc = NFC()

if not nfc.transacciones:
    nfc.transacciones = [
        Transaccion("TX001", 25.50, "2024-12-01"),
        Transaccion("TX002", 100.00, "2024-12-02"),
        Transaccion("TX003", 15.75, "2024-12-03")
    ]
    nfc.guardar()

print("\nMostrar todas")
nfc.mostrar_todas()

print("\nBuscar transacción 'TX002'")
nfc.buscar_transaccion("TX002")

print("\nAgregar nueva transacción")
nfc.agregar_transaccion()