import json

class Consulta:
    def __init__(self,ci, nombrePaciente, apellidoPaciente, idMed, dia, mes, anio):
        self.ci = ci
        self.nombrePaciente = nombrePaciente
        self.apellidoPaciente = apellidoPaciente
        self.idMed = idMed
        self.dia = dia
        self.mes = mes
        self.anio = anio
        
    def cambiar_fecha(self, nuevo_dia, nuevo_mes, nuevo_anio):
        self.dia = nuevo_dia
        self.mes = nuevo_mes
        self.anio = nuevo_anio
        try:
            with open("consultas.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("No se encontraron consultas.")
            return
        for consulta in data:
            if consulta["ci"] == self.ci and consulta["idMed"] == self.idMed:
                consulta["dia"] = nuevo_dia
                consulta["mes"] = nuevo_mes
                consulta["anio"] = nuevo_anio
                break
        with open("consultas.json", "w") as file:
            json.dump(data, file, indent=4)
        

class Consultorio:
    def __init__(self, consulta, medico):
        self.consulta = consulta
        self.medico = medico
        
    def alta(self):
        try:
            with open("consultas.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        data.append({
            "ci": self.consulta.ci,
            "nombrePaciente": self.consulta.nombrePaciente,
            "apellidoPaciente": self.consulta.apellidoPaciente,
            "idMed": self.consulta.idMed,
            "dia": self.consulta.dia,
            "mes": self.consulta.mes,
            "anio": self.consulta.anio,
            "nombreMedico": self.medico.nombreMed,
            "apellidoMedico": self.medico.apellidoMed,
            "aniosExperiencia": self.medico.aniosExperiencia
        })
        with open("consultas.json", "w") as file:
            json.dump(data, file, indent=4)
            
        
class Medico:
    def __init__ (self, idMed, nombreMed, apellidoMed, aniosExperiencia):
        self.idMed = idMed
        self.nombreMed = nombreMed
        self.apellidoMed = apellidoMed
        self.aniosExperiencia = aniosExperiencia
        
    def bajaMedico(self, idMed):
        try:
            with open("consultas.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("No se encontraron consultas.")
            return
        data = [consulta for consulta in data if consulta["idMed"] != idMed]
        with open("consultas.json", "w") as file:
            json.dump(data, file, indent=4)
        
    
co1 = Consulta(1377382, "Juan", " Castilo", "1230", 8, 12, 2025)
co2 = Consulta(1233122, "Ana", " Gomez", "1231", 25, 12, 2025)
co3 = Consulta(1456789, "Pedro", " Martinez", "1230", 20, 10, 2025)
co4 = Consulta(1243122, "Luis", "Rodriguez", "1231", 1, 9, 2025)
co5 = Consulta(1248274, "Maria", "Quispe", "1230", 2, 8, 2025)
co6 = Consulta(1379204, "Marcos", "Quinteros", "1231", 12, 7, 2025)
co7 = Consulta(1333333, "Carlos", "Sanchez", "1233", 1, 1, 2025)
co8 = Consulta(1444444, "Sofia", "Ramirez", "1233", 15, 11, 2025)
co9 = Consulta(1555555, "Elena", "Torres", "1233", 30, 6, 2025)


med1 = Medico("1230", "Luis", "Perez", 10)
med2 = Medico("1231", "Ana", "Lopez", 8)
med3 = Medico("1233", "Fernando", "Vizcara", 20)

co2.cambiar_fecha(30, 12, 2025)
co7.cambiar_fecha(3, 1, 2025)  

con1 = Consultorio(co1, med1)
con2 = Consultorio(co2, med2)
con3 = Consultorio(co3, med1)
con4 = Consultorio(co4, med2)
con5 = Consultorio(co5, med1)
con6 = Consultorio(co6, med2)
con7 = Consultorio(co7, med3)
con8 = Consultorio(co8, med3)
con9 = Consultorio(co9, med3)
#alta
con1.alta()
con2.alta()
con3.alta()
con4.alta()
con5.alta()
con6.alta()
con7.alta()
con8.alta()
con9.alta()


#Baja
medico_baja = med1
medico_baja.bajaMedico("1230")

#mostrar atendidos en mi cumpleaños
dia_cumple = 1
mes_cumple = 9
try:
    with open("consultas.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print("No se encontraron consultas.")
    data = []
atendidos_cumple = [consulta for consulta in data if consulta["dia"] == dia_cumple and consulta["mes"] == mes_cumple]
print(f"Pacientes atendidos en mi cumpleaños ({dia_cumple}/{mes_cumple}):")
for consulta in atendidos_cumple:
    print(f"- {consulta['nombrePaciente']} {consulta['apellidoPaciente']} (CI: {consulta['ci']})")
    