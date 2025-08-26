class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getDiscriminante(self):
        return self.__b**2 - 4*self.__a*self.__c
    
    def getRaiz1(self):
        discriminante = self.getDiscriminante()
        if discriminante < 0:
            return "No tiene solución real"
        return (-self.__b + discriminante**0.5) / (2*self.__a)
    
    def getRaiz2(self):
        discriminante = self.getDiscriminante()
        if discriminante < 0:
            return "No tiene solución real"
        return (-self.__b - discriminante**0.5) / (2*self.__a)

    def toString(self):
        return "EcuacionCuadratica {{{},{},{}}}".format(self.__a, self.__b, self.__c)
    
ecuacion1 = EcuacionCuadratica(1, 3, 1)
ecuacion2 = EcuacionCuadratica(1, 2, 1)
ecuacion3 = EcuacionCuadratica(1, 2, 3)

print("Discriminante:", ecuacion1.getDiscriminante())
print("Raiz 1:", ecuacion1.getRaiz1())
print("Raiz 2:", ecuacion1.getRaiz2())
print("///////////////////////////////////////")
print("Discriminante:", ecuacion2.getDiscriminante())
print("Raiz 1:", ecuacion2.getRaiz1())
print("Raiz 2:", ecuacion2.getRaiz2())
print("///////////////////////////////////////")
print("Discriminante:", ecuacion3.getDiscriminante())
print("Raiz 1:", ecuacion3.getRaiz1())
print("Raiz 2:", ecuacion3.getRaiz2())