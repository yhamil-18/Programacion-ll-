import math

class Estadisticas:
    def __init__(self):
        self.numeros = []
    
    def solicitar_numeros(self, n=10):
        for i in range(n):
            while True:
                try:
                    self.numeros.append(float(input(f"Número {i+1}: ")))
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")
    
    def promedio(self):
        return sum(self.numeros) / len(self.numeros) if self.numeros else 0
    
    def desviacion(self):
        if len(self.numeros) < 2:
            return 0
        prom = self.promedio()
        return math.sqrt(sum((x - prom)**2 for x in self.numeros) / (len(self.numeros) - 1))
    
    def __str__(self):  
        return f"Promedio: {self.promedio():.2f}\nDesviación: {self.desviacion():.2f}"

edad = Estadisticas()
edad.solicitar_numeros()
print(edad)  