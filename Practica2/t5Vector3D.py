import math

class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    # Sobrecarga de operadores
    def __add__(self, other):
        """Sobrecarga del operador + para suma de vectores"""
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        """Sobrecarga del operador - para resta de vectores"""
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        """Sobrecarga del operador * para producto escalar y multiplicación por escalar"""
        if isinstance(other, (int, float)):
            # Multiplicación por escalar
            return Vector3D(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector3D):
            # Producto escalar
            return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __rmul__(self, scalar):
        """Multiplicación por escalar (desde la derecha)"""
        return self * scalar
    
    def __xor__(self, other):
        """Sobrecarga del operador ^ para producto vectorial"""
        if isinstance(other, Vector3D):
            x = self.y * other.z - self.z * other.y
            y = self.z * other.x - self.x * other.z
            z = self.x * other.y - self.y * other.x
            return Vector3D(x, y, z)
    
    def __str__(self):
        """Representación string del vector"""
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"
    
    def __repr__(self):
        """Representación para debugging"""
        return f"Vector3D({self.x}, {self.y}, {self.z})"
    
    # Métodos de operaciones vectoriales
    def magnitud(self):
        """Calcula la magnitud del vector"""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalizar(self):
        """Normaliza el vector (vector unitario)"""
        mag = self.magnitud()
        if mag < 1e-10:
            return Vector3D(0, 0, 0)
        return Vector3D(self.x/mag, self.y/mag, self.z/mag)
    
    # Métodos de análisis
    def es_perpendicular(self, other):
        """Verifica si es perpendicular usando producto escalar"""
        return abs(self * other) < 1e-10
    
    def es_paralelo(self, other):
        """Verifica si es paralelo usando producto vectorial"""
        producto_cruz = self ^ other
        return producto_cruz.magnitud() < 1e-10
    
    def proyeccion(self, other):
        """Calcula la proyección de este vector sobre otro"""
        mag_cuad = other.magnitud() ** 2
        if mag_cuad < 1e-10:
            return Vector3D(0, 0, 0)
        escalar = (self * other) / mag_cuad
        return other * escalar
    
    def componente(self, other):
        """Calcula el componente de este vector en la dirección de otro"""
        mag = other.magnitud()
        if mag < 1e-10:
            return 0.0
        return (self * other) / mag

a = Vector3D(1, 2, 3)
b = Vector3D(4, 5, 6)
c = Vector3D(0, 0, 1)
d = Vector3D(1, 0, 0)
e = Vector3D(2, 4, 6)


suma = a + b
resta = a - b
multiplicacion = a * 2
producto_escalar = a * b
producto_vectorial = a ^ b
magnitud = a.magnitud()
normalizado = a.normalizar()


perpendiculares = c.es_perpendicular(d)
paralelos = a.es_paralelo(e)
proyeccion = a.proyeccion(b)
componente = a.componente(b)


print("=== PROGRAMA DE ÁLGEBRA VECTORIAL EN PYTHON ===")
print()
print("Vectores:")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"d = {d}")
print(f"e = {e}")
print()
print("Operaciones básicas:")
print(f"a + b = {suma}")
print(f"a - b = {resta}")
print(f"a * 2 = {multiplicacion}")
print(f"a · b (producto escalar) = {producto_escalar:.2f}")
print(f"a × b (producto vectorial) = {producto_vectorial}")
print(f"|a| (magnitud) = {magnitud:.2f}")
print(f"a_normalizado = {normalizado}")
print()
print("Análisis de vectores:")
print(f"c ⟂ d (perpendiculares): {perpendiculares}")
print(f"a ∥ e (paralelos): {paralelos}")
print(f"Proyección de a sobre b: {proyeccion}")
print(f"Componente de a en b: {componente:.2f}")
print()
print("Verificación de propiedades:")
print(f"a · c = {a * c:.2f}")
print(f"|a × e| = {(a ^ e).magnitud():.2f} (debe ser ≈ 0 para paralelos)")