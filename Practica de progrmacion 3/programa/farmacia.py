import json

class Medicamento:
    def __init__(self, nombre="", cod=0, tipo="", precio=0.0):
        self.nombre = nombre
        self.cod = cod
        self.tipo = tipo
        self.precio = precio

class Farmacia:
    def __init__(self, nombre="", sucursal=0, direccion="", cant_meds=0):
        self.nombre = nombre
        self.sucursal = sucursal
        self.direccion = direccion
        self.cant_meds = cant_meds
        self.medicamentos = []

class ArchFarmacia:
    def __init__(self, archivo="farmacias.json"):
        self.archivo = archivo
        self.farmacias = []
        self.cargar()
    
    def cargar(self):
        try:
            with open(self.archivo, 'r') as f:
                datos = json.load(f)
                for farm_data in datos:
                    farmacia = Farmacia()
                    farmacia.nombre = farm_data['nombre']
                    farmacia.sucursal = farm_data['sucursal']
                    farmacia.direccion = farm_data['direccion']
                    farmacia.cant_meds = farm_data['cant_meds']
                    
                    for med_data in farm_data['medicamentos']:
                        med = Medicamento()
                        med.nombre = med_data['nombre']
                        med.cod = med_data['cod']
                        med.tipo = med_data['tipo']
                        med.precio = med_data['precio']
                        farmacia.medicamentos.append(med)
                    
                    self.farmacias.append(farmacia)
        except:
            self.farmacias = []
    
    def guardar(self):
        datos = []
        for farmacia in self.farmacias:
            meds = []
            for med in farmacia.medicamentos:
                meds.append({
                    'nombre': med.nombre,
                    'cod': med.cod,
                    'tipo': med.tipo,
                    'precio': med.precio
                })
            
            datos.append({
                'nombre': farmacia.nombre,
                'sucursal': farmacia.sucursal,
                'direccion': farmacia.direccion,
                'cant_meds': len(farmacia.medicamentos),
                'medicamentos': meds
            })
        
        with open(self.archivo, 'w') as f:
            json.dump(datos, f, indent=2)
    
    def mostrar_tos_sucursal_x(self, x):
        for farmacia in self.farmacias:
            if farmacia.sucursal == x:
                for med in farmacia.medicamentos:
                    if "tos" in med.tipo.lower():
                        print(f"{med.nombre} - ${med.precio}")
    
    def buscar_tapsin(self):
        for farmacia in self.farmacias:
            for med in farmacia.medicamentos:
                if med.nombre.lower() == "tapsin":
                    print(f"Sucursal: {farmacia.sucursal}, Dirección: {farmacia.direccion}")
    
    def buscar_por_tipo(self, tipo):
        for farmacia in self.farmacias:
            for med in farmacia.medicamentos:
                if med.tipo.lower() == tipo.lower():
                    print(f"{farmacia.nombre}: {med.nombre} - ${med.precio}")
    
    def ordenar_por_direccion(self):
        self.farmacias.sort(key=lambda f: f.direccion)
        self.guardar()
        for farmacia in self.farmacias:
            print(f"{farmacia.direccion}: {farmacia.nombre}")
    
    def mover_medicamentos(self, tipo, suc_origen, suc_destino):
        origen = None
        destino = None
        
        for farmacia in self.farmacias:
            if farmacia.sucursal == suc_origen:
                origen = farmacia
            if farmacia.sucursal == suc_destino:
                destino = farmacia
        
        if origen and destino:
            mover = []
            quedan = []
            
            for med in origen.medicamentos:
                if med.tipo.lower() == tipo.lower():
                    mover.append(med)
                else:
                    quedan.append(med)
            
            origen.medicamentos = quedan
            origen.cant_meds = len(quedan)
            
            destino.medicamentos.extend(mover)
            destino.cant_meds = len(destino.medicamentos)
            
            self.guardar()
            print(f"Movidos {len(mover)} medicamentos")

def crear_datos():
    m1 = Medicamento("Tapsin", 1, "resfrio", 25.0)
    m2 = Medicamento("Jarabe", 2, "tos", 18.0)
    m3 = Medicamento("Pastillas", 3, "dolor", 12.0)
    
    f1 = Farmacia("Farma1", 1, "Calle A", 3)
    f1.medicamentos = [m1, m2, m3]
    
    m4 = Medicamento("Gripex", 4, "resfrio", 30.0)
    m5 = Medicamento("Tosina", 5, "tos", 15.0)
    
    f2 = Farmacia("Farma2", 2, "Calle B", 2)
    f2.medicamentos = [m4, m5]
    
    arch = ArchFarmacia()
    arch.farmacias = [f1, f2]
    arch.guardar()
    return arch

arch = crear_datos()

print("Medicamentos para tos en sucursal 1:")
arch.mostrar_tos_sucursal_x(1)

print("\nSucursales con Tapsin:")
arch.buscar_tapsin()

print("\nMedicamentos tipo 'resfrio':")
arch.buscar_por_tipo("resfrio")

print("\nOrdenar por dirección:")
arch.ordenar_por_direccion()

print("\nMover medicamentos tipo 'tos' de sucursal 1 a 2:")
arch.mover_medicamentos("tos", 1, 2)