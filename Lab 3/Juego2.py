import random

class Juego:
    def __init__(self, vidas):
        self.numeroDeVidas = vidas
        self.record = 0
        self.vidas_iniciales = vidas  
    
    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidas_iniciales
    
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
    
    def validaNumero(self, numero):
        """Valida si el número está entre 0 y 10"""
        if 0 <= numero <= 10:
            return True
        else:
            print("Error: El número debe estar entre 0 y 10.")
            return False
    
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        
        print("\n=== NUEVA PARTIDA ===")
        print(f"Tienes {self.numeroDeVidas} vidas.")
        
        while True:
            try:
                numeroUsuario = int(input("Introduce tu número (0-10): "))
            except ValueError:
                print("Por favor, introduce un número válido.")
                continue
            
            if not self.validaNumero(numeroUsuario):
                print("Por favor, introduce un número válido.")
                continue
            
            if numeroUsuario == self.numeroAAdivinar:
                print("¡Acertaste!!")
                self.actualizaRecord()
                break
            else:
                if self.numeroAAdivinar > numeroUsuario:
                    print(f"Fallaste. El número a adivinar es MAYOR que {numeroUsuario}.")
                else:
                    print(f"Fallaste. El número a adivinar es MENOR que {numeroUsuario}.")
                
                if not self.quitaVida():
                    print(f"El número correcto era: {self.numeroAAdivinar}")
                    break

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
    
    def validaNumero(self, numero):
        """Valida si el número está entre 0 y 10 y es PAR"""
        if numero < 0 or numero > 10:
            print("Error: El número debe estar entre 0 y 10.")
            return False
        
        if numero % 2 == 0:
            return True
        else:
            print("Error: Debes introducir un número PAR.")
            return False
    
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.choice([0, 2, 4, 6, 8, 10])
        
        print("\n=== JUEGO ADIVINA NÚMERO PAR ===")
        print(f"Tienes {self.numeroDeVidas} vidas.")
        print("Debes adivinar un número PAR entre 0 y 10.")
        
        while True:
            try:
                numeroUsuario = int(input("Introduce un número PAR (0-10): "))
            except ValueError:
                print("Por favor, introduce un número válido.")
                continue
            
            if not self.validaNumero(numeroUsuario):
                continue
            
            if numeroUsuario == self.numeroAAdivinar:
                print("¡Acertaste!!")
                self.actualizaRecord()
                break
            else:
                if self.numeroAAdivinar > numeroUsuario:
                    print(f"Fallaste. El número a adivinar es MAYOR que {numeroUsuario}.")
                else:
                    print(f"Fallaste. El número a adivinar es MENOR que {numeroUsuario}.")
                
                if not self.quitaVida():
                    print(f"El número correcto era: {self.numeroAAdivinar}")
                    break

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
    
    def validaNumero(self, numero):
        """Valida si el número está entre 0 y 10 y es IMPAR"""
        if numero < 0 or numero > 10:
            print("Error: El número debe estar entre 0 y 10.")
            return False
        
        if numero % 2 != 0:
            return True
        else:
            print("Error: Debes introducir un número IMPAR.")
            return False
    
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.choice([1, 3, 5, 7, 9])
        
        print("\n=== JUEGO ADIVINA NÚMERO IMPAR ===")
        print(f"Tienes {self.numeroDeVidas} vidas.")
        print("Debes adivinar un número IMPAR entre 0 y 10.")
        
        while True:
            try:
                numeroUsuario = int(input("Introduce un número IMPAR (0-10): "))
            except ValueError:
                print("Por favor, introduce un número válido.")
                continue
            
            if not self.validaNumero(numeroUsuario):
                continue
            
            if numeroUsuario == self.numeroAAdivinar:
                print("¡Acertaste!!")
                self.actualizaRecord()
                break
            else:
                if self.numeroAAdivinar > numeroUsuario:
                    print(f"Fallaste. El número a adivinar es MAYOR que {numeroUsuario}.")
                else:
                    print(f"Fallaste. El número a adivinar es MENOR que {numeroUsuario}.")
                
                if not self.quitaVida():
                    print(f"El número correcto era: {self.numeroAAdivinar}")
                    break

class Aplicacion:
    @staticmethod
    def main():
        juegoNormal = JuegoAdivinaNumero(3)
        juegoPar = JuegoAdivinaPar(3)
        juegoImpar = JuegoAdivinaImpar(3)
        
        print("BIENVENIDO A LOS JUEGOS DE ADIVINANZA")
        print("=====================================")
        
        juegoNormal.juega()
        juegoPar.juega()
        juegoImpar.juega()
        
        print("\n=====================================")
        print("¡Gracias por jugar!")

if __name__ == "__main__":
    Aplicacion.main()