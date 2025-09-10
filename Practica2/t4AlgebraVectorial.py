import math

class AlgebraVectorial:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        if isinstance(x, AlgebraVectorial):
            vector = x
            self.x = float(vector.x)
            self.y = float(vector.y)
            self.z = float(vector.z)
        else:
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getZ(self):
        return self.z
    
    def setX(self, x):
        self.x = float(x)
    
    def setY(self, y):
        self.y = float(y)
    
    def setZ(self, z):
        self.z = float(z)
    
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def productoPunto(self, otro_vector):
        return (self.x * otro_vector.x + 
                self.y * otro_vector.y + 
                self.z * otro_vector.z)

    def productoVectorial(self, otro_vector):
        x = self.y * otro_vector.z - self.z * otro_vector.y
        y = self.z * otro_vector.x - self.x * otro_vector.z
        z = self.x * otro_vector.y - self.y * otro_vector.x
        return AlgebraVectorial(x, y, z)
    
    # a) |a + b| = |a - b|
    def esPerpendicular1(self, otro_vector):
        suma = AlgebraVectorial(self.x + otro_vector.x, 
                               self.y + otro_vector.y, 
                               self.z + otro_vector.z)
        resta = AlgebraVectorial(self.x - otro_vector.x, 
                                self.y - otro_vector.y, 
                                self.z - otro_vector.z)
        return abs(suma.magnitud() - resta.magnitud()) < 1e-10
    
    # b) |a - b| = |b - a| (siempre es verdadero, no es una prueba válida de perpendicularidad)
    def esPerpendicular2(self, otro_vector):
        ab = AlgebraVectorial(self.x - otro_vector.x, 
                             self.y - otro_vector.y, 
                             self.z - otro_vector.z)
        ba = AlgebraVectorial(otro_vector.x - self.x, 
                             otro_vector.y - self.y, 
                             otro_vector.z - self.z)
        return abs(ab.magnitud() - ba.magnitud()) < 1e-10
    
    # c) a · b = 0 (el método correcto para perpendicularidad)
    def esPerpendicular3(self, otro_vector):
        return abs(self.productoPunto(otro_vector)) < 1e-10
    
    # d) |a + b|² = |a|² + |b|² (teorema de Pitágoras para vectores)
    def esPerpendicular4(self, otro_vector):
        suma = AlgebraVectorial(self.x + otro_vector.x, 
                               self.y + otro_vector.y, 
                               self.z + otro_vector.z)
        magnitud_suma_cuad = suma.magnitud() ** 2
        magnitud_a_cuad = self.magnitud() ** 2
        magnitud_b_cuad = otro_vector.magnitud() ** 2
        return abs(magnitud_suma_cuad - (magnitud_a_cuad + magnitud_b_cuad)) < 1e-10
    
    # e) a = r*b (existe un escalar r tal que a = r*b)
    def esParalelo1(self, otro_vector):
        if otro_vector.magnitud() < 1e-10:
            # Si el otro vector es cero, solo somos paralelos si también somos cero
            return self.magnitud() < 1e-10
        
        # Verificamos si hay alguna componente no cero en el otro vector
        if abs(otro_vector.x) > 1e-10:
            r = self.x / otro_vector.x
        elif abs(otro_vector.y) > 1e-10:
            r = self.y / otro_vector.y
        elif abs(otro_vector.z) > 1e-10:
            r = self.z / otro_vector.z
        else:
            # El otro vector es cero (pero ya verificamos esto arriba)
            return False
        
        # Verificamos si todas las componentes son proporcionales
        return (abs(self.x - r * otro_vector.x) < 1e-10 and
                abs(self.y - r * otro_vector.y) < 1e-10 and
                abs(self.z - r * otro_vector.z) < 1e-10)
    
    # f) a × b = 0 (el método correcto para paralelismo)
    def esParalelo2(self, otro_vector):
        # Dos vectores son paralelos si su producto vectorial es el vector cero
        producto_cruz = self.productoVectorial(otro_vector)
        return producto_cruz.magnitud() < 1e-10
    
    # g) Proyección de a sobre b: (a·b/|b|²) * b
    def proyeccion(self, otro_vector):
        if abs(otro_vector.magnitud()) < 1e-10:
            return AlgebraVectorial(0, 0, 0)
        
        escalar = self.productoPunto(otro_vector) / (otro_vector.magnitud() ** 2)
        return AlgebraVectorial(escalar * otro_vector.x,
                               escalar * otro_vector.y,
                               escalar * otro_vector.z)
    
    # h) Componente de a en b: (a·b)/|b|
    def componente(self, otro_vector):
        if abs(otro_vector.magnitud()) < 1e-10:
            return 0.0
        
        return self.productoPunto(otro_vector) / otro_vector.magnitud()
    

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

v1 = AlgebraVectorial(1, 2, 3)
v2 = AlgebraVectorial(4, 5, 6)
v3 = AlgebraVectorial(0, 0, 1)
v4 = AlgebraVectorial(1, 0, 0)
v5 = AlgebraVectorial(2, 4, 6)

print("Vectores:")
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v3 = {v3}")
print(f"v4 = {v4}")
print(f"v5 = {v5}")
print()


print("Perpendicularidad v3 y v4:")
print(f"Método 1: {v3.esPerpendicular1(v4)}")
print(f"Método 2: {v3.esPerpendicular2(v4)} (siempre True, no es confiable)")
print(f"Método 3: {v3.esPerpendicular3(v4)} (método correcto)")
print(f"Método 4: {v3.esPerpendicular4(v4)}")
print()


print("Paralelismo v1 y v5:")
print(f"Método 1: {v1.esParalelo1(v5)}")
print(f"Método 2: {v1.esParalelo2(v5)} (método correcto)")
print()

print("Proyección de v1 sobre v2:")
proyeccion = v1.proyeccion(v2)
print(f"Proyección: {proyeccion}")

print("Componente de v1 en v2:")
componente = v1.componente(v2)
print(f"Componente: {componente}")