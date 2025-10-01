from abc import ABC, abstractmethod
import math
import random

class Coloreado(ABC):
    @abstractmethod
    def comoColorear(self): pass

class Figura(ABC):
    def __init__(self, color): self.color = color
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimetro(self): pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color):
        super().__init__(color)
        self.lado = lado
    def area(self): return self.lado ** 2
    def perimetro(self): return 4 * self.lado
    def comoColorear(self): return "Colorear los cuatro lados"

class Circulo(Figura):
    def __init__(self, radio, color):
        super().__init__(color)
        self.radio = radio
    def area(self): return math.pi * self.radio ** 2
    def perimetro(self): return 2 * math.pi * self.radio


figuras = []
for i in range(5):
    if random.randint(1, 2) == 1:
        figuras.append(Cuadrado(random.uniform(1, 10), "azul"))
    else:
        figuras.append(Circulo(random.uniform(1, 10), "rojo"))

for f in figuras:
    print(f"{type(f).__name__} - Área: {f.area():.2f}, Perímetro: {f.perimetro():.2f}")
    if isinstance(f, Coloreado):
        print(f"  -> {f.comoColorear()}")