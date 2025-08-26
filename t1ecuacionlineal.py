class ecuacionlineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
            
    def TieneSolucion(self):
        determinante = (self.__a * self.__d) - (self.__b * self.__c)
        return determinante != 0 
        
    def getX(self):
        determinante = (self.__a * self.__d) - (self.__b * self.__c)
        if determinante == 0:
            return "No tiene solución única"
        numerador = (self.__e * self.__d) - (self.__b * self.__f)
        return numerador / determinante
    
    def getY(self):
        determinante = (self.__a * self.__d) - (self.__b * self.__c)
        if determinante == 0:
            return "No tiene solución "
        numerador = (self.__a * self.__f) - (self.__e * self.__c)
        return numerador / determinante
    
    def toString(self):
        return "EcuacionLineal {{{},{},{},{},{},{}}}".format(self.__a, self.__b, self.__c, self.__d, self.__e, self.__f)

x1 = ecuacionlineal(9, 4, 3, -5, -6, -21)
x2 = ecuacionlineal(1, 2, 2, 4, 4, 5)

print("¿x1 tiene solución?", x1.TieneSolucion())
print("x1 =", x1.getX())
print("y1 =", x1.getY())
print("/////////////////////////////////////////////////")
print("¿x2 tiene solución?", x2.TieneSolucion())
print("x2 =", x2.getX())
print("y2 =", x2.getY())