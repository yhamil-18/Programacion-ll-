class Persona:
    def __init__(self, nombre, edad, pesoPersona):
        self.nombre = nombre 
        self.edad = edad 
        self.pesoPersona = pesoPersona
        
    def __str__(self):
        return f"{self.nombre} ({self.edad} años, {self.pesoPersona} kg)"

class Cabina:
    def __init__(self, nroCabina):
        self.nroCabina = nroCabina
        self.PersonaAbordo = []  
        
    def agregarPersona(self, p):
        self.PersonaAbordo.append(p)
        
    def agregarPrimPersona(self, p):
        peso_total = sum(persona.pesoPersona for persona in self.PersonaAbordo)
        peso_total += p.pesoPersona  
        
        if len(self.PersonaAbordo) < 10 and peso_total <= 850:
            self.PersonaAbordo.append(p)
            print(f"Persona {p.nombre} agregada a cabina {self.nroCabina}")
            return True
        else:
            print(f"No se puede agregar a {p.nombre}. Capacidad: {len(self.PersonaAbordo)}/10 personas, Peso: {peso_total}/850 kg")
            return False
            
    def mostrar(self):
        peso_total = sum(persona.pesoPersona for persona in self.PersonaAbordo)
        print(f"Cabina nro {self.nroCabina} con {len(self.PersonaAbordo)} personas a bordo (Peso total: {peso_total} kg):")
        for persona in self.PersonaAbordo:
            print(f"  - {persona}")
        return f"Cabina nro {self.nroCabina} con {len(self.PersonaAbordo)} personas a bordo."
        
class Linea:
    def __init__(self, color, cantidadCabinas):
        self.color = color
        self.cabinas = []  
        self.filaPersona = []  
        self.cantidadCabinas = cantidadCabinas
        self.ingresos = 0  
        
    def agregarPersona(self, persona):
        self.filaPersona.append(persona)
        self.ingresos += 1  
        print(f"Persona {persona.nombre} agregada a la fila de línea {self.color}")
        
    def agregarCabina(self, cabina):
        if len(self.cabinas) < self.cantidadCabinas:
            self.cabinas.append(cabina)
            print(f"Cabina {cabina.nroCabina} agregada a línea {self.color}")
        else:
            print(f"No se pueden agregar más cabinas a la línea {self.color}")

    def mostrarInfo(self):
        total_personas = sum(len(cabina.PersonaAbordo) for cabina in self.cabinas)
        print(f"Línea de color {self.color} con {len(self.cabinas)}/{self.cantidadCabinas} cabinas. Personas: {total_personas}, Ingresos: {self.ingresos}")
        for cabina in self.cabinas:
            cabina.mostrar()
        return f"Línea de color {self.color} con {len(self.cabinas)}/{self.cantidadCabinas} cabinas."

class MiTeleferico: 
    def __init__(self, cantidadIngresos):
        self.cantidadIngresos = cantidadIngresos
        self.lineas = []  
        
    def agregarPersonaFila(self, persona, linea):
        linea.agregarPersona(persona)
        
    def agregarLinea(self, linea):
        self.lineas.append(linea)
        print(f"Línea {linea.color} agregada al teleférico")
        
    def tarifaPersona(self, persona):
        if persona.edad < 25 or persona.edad > 60:
            print(f"Tarifa reducida para {persona.nombre}: $1.50")   
            return 1.50
        else:
            print(f"Tarifa normal para {persona.nombre}: $3.00")
            return 3.00
        
    def lineaconmasIngresos(self):
        if not self.lineas:
            print("No hay líneas registradas")
            return None
            
        linea_mas_ingresos = max(self.lineas, key=lambda linea: linea.ingresos)
        print(f"La línea con más ingresos es la línea {linea_mas_ingresos.color} con {linea_mas_ingresos.ingresos} ingresos.")
        return linea_mas_ingresos


p = Persona("Ana", 28, 65)
p2 = Persona("Luis", 70, 80)
p3 = Persona("Marta", 15, 50)
p4 = Persona("Carlos", 30, 75)
p5 = Persona("Sofia", 22, 60)
p6 = Persona("Jorge", 68, 85)
p7 = Persona("Lucia", 19, 55)
p8 = Persona("Miguel", 45, 90)
p9 = Persona("Elena", 33, 70)
p10 = Persona("Diego", 72, 80)
p11 = Persona("Carmen", 27, 65)


cabina1 = Cabina(1)
cabina1.agregarPrimPersona(p)
cabina1.agregarPrimPersona(p2)
cabina1.agregarPrimPersona(p3)
cabina1.agregarPrimPersona(p4)
cabina1.agregarPrimPersona(p7)
cabina1.mostrar()

cabina2 = Cabina(2)
cabina2.agregarPrimPersona(p5)
cabina2.agregarPrimPersona(p6)
cabina2.mostrar()

cabina3 = Cabina(3)
cabina3.agregarPrimPersona(p8)
cabina3.agregarPrimPersona(p9)
cabina3.agregarPrimPersona(p10)
cabina3.agregarPrimPersona(p11)
cabina3.mostrar()


teleferico = MiTeleferico(1000)

linea1 = Linea("Rojo", 3)
linea2 = Linea("Amarilla", 2)
linea3 = Linea("Verde", 4)

teleferico.agregarLinea(linea1)
teleferico.agregarLinea(linea2)
teleferico.agregarLinea(linea3)

linea1.agregarCabina(cabina1)
linea2.agregarCabina(cabina2)
linea3.agregarCabina(cabina3)


teleferico.agregarPersonaFila(p, linea1)
teleferico.agregarPersonaFila(p2, linea1)
teleferico.agregarPersonaFila(p3, linea1)
teleferico.agregarPersonaFila(p4, linea2)
teleferico.agregarPersonaFila(p5, linea2)
teleferico.agregarPersonaFila(p6, linea3)

teleferico.tarifaPersona(p)   
teleferico.tarifaPersona(p2) 
teleferico.tarifaPersona(p3)  

linea1.mostrarInfo()
linea2.mostrarInfo()
linea3.mostrarInfo()

teleferico.lineaconmasIngresos()