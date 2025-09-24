import random

class Juego:
    def __init__(self, vidas):
        self.numeroDeVidas = vidas
        self.record = 0
    
    def reiniciaPartida(self):
        pass
    
    def actualizaRecord(self):
        self.record += 1
        print(f"¡Nuevo record! Llevas {self.record} aciertos.")
    
    def quitaVida(self):
        self.numeroDeVidas -= 1
        if self.numeroDeVidas > 0:
            print(f"Te quedan {self.numeroDeVidas} vidas.")
            return True
        else:
            print("¡Game Over! Te has quedado sin vidas.")
            return False

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0
    
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        
        print("¡Bienvenido al juego de adivinar el número!")
        print(f"Tienes {self.numeroDeVidas} vidas para adivinar un número entre 0 y 10.")
        
        while True:
            try:
                numeroUsuario = int(input("Introduce tu número: "))
            except ValueError:
                print("Por favor, introduce un número válido.")
                continue
            
            if numeroUsuario == self.numeroAAdivinar:
                print("¡Acertaste!!")
                self.actualizaRecord()
                break
            else:
                if not self.quitaVida():
                    print(f"El número correcto era: {self.numeroAAdivinar}")
                    break
                else:
                    if self.numeroAAdivinar > numeroUsuario:
                        print("El número a adivinar es MAYOR.")
                    else:
                        print("El número a adivinar es MENOR.")
                    print("Inténtalo de nuevo.")

class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(5)
        juego.juega()

if __name__ == "__main__":
    Aplicacion.main()