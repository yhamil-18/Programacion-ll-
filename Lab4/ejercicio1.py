from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
    
    @abstractmethod
    def calcular_salario_mensual(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_anual):
        super().__init__(nombre)
        self.salario_anual = salario_anual
    
    def calcular_salario_mensual(self):
        return self.salario_anual / 12

class EmpleadoTiempoHorario(Empleado):
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora
    
    def calcular_salario_mensual(self):
        return self.horas_trabajadas * self.tarifa_por_hora
    

empleados = [
    EmpleadoTiempoCompleto("Ana", 60000),
    EmpleadoTiempoCompleto("Carlos", 72000),
    EmpleadoTiempoCompleto("María", 48000),
    EmpleadoTiempoHorario("Pedro", 160, 25),
    EmpleadoTiempoHorario("Laura", 120, 30)
]

for emp in empleados:
    print(f"{emp.nombre}: ${emp.calcular_salario_mensual():,.2f}")