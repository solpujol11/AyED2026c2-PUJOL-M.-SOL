import random


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado #cuadrado en particular al  que le asignas un lado
                        #variable __lado dentro de cuadado, crea un cuadrado de lado = lado
                        #los guiones bajos indican que es una variable privada, no se puede acceder desde fuera de la clase
        if isinstance(lado,(int,float)):
            self.__lado = lado 
        else:
            raise ValueError("El lado debe ser un número")

def prueba_cuadrado():
    cuadrado=Cuadrado("a")
    
#MODIFICACIONES
class Cuadrado:
    def __init__(self,lado):
        self.establecer_lado(lado)
    def establecer_lado(self , nuevo_lado):
        """
        Establece el lado en un nuevo valor
        Precondiciones:
            - nuevo_lado debe ser un valor numerico
            - nuevo_lado tiene que ser mayor a 0 
        Postcondiciones:
            - el lado cuadrado toma el valor nuevo_lado
        Raise:
            - ValueError si el lado no es numerico
        """
        if isinstance(nuevo_lado,(int,float)):
            if nuevo_lado>0:
                self.__lado = nuevo_lado 
            else:
                raise ValueError ("Lado debe ser mayor que 0")
        else:
            raise TypeError("El lado debe ser un número")
    def obtener_lado (self):
        return self.__lado

    def obtener_perimetro (self):
        return 4*self.__lado

    def obtener_area(self):
        return self.__lado*self.__lado

def prueba_cuadrado2():
    cuadrado=Cuadrado(1)
    print(cuadrado.obtener_lado()) #deberia dar 1
    print(cuadrado.obtener_perimetro()) #deberia dar 4
    cuadrado.establecer_lado(2)
    print(cuadrado.obtener_lado()) #deberia dar 2
    print(cuadrado.obtener_perimetro()) #deberia dar 8
    print(Cuadrado)
if __name__ == "__main__":  
    prueba_cuadrado2()

class Persona:
    def __init__(self,nombre,apellido):
        if isinstance(nombre,str):
            if isinstance(apellido,str):
                self.__nombre = nombre.capitalize()
                self.__apellido = apellido.capitalize()
            else:
                raise TypeError ("Apellido no es una cadena de caracteres)")
        else:
            raise TypeError ("Nombre no es una cadena de caracteres)")

@property
def nombre (self):
    return self.__nombre

@property
def apellido (self):
    return self.__apellido

import random
class PersonaAleatoria(Persona):
    NOMBRES=["amanda","feli","sol"]
    APELLIDOS=["epson","franco","cabada","pujol"]

    def __init__(self):
        nombre = random.choice(self.NOMBRES)
        apellido = random.choice(self.APELLIDOS)
        super().__init__(nombre,apellido) #llamar a su clase madre (persona) y llama al init de la clase madre

if __name__ == "__main__":
    persona_aleatoria = PersonaAleatoria()
    print(persona_aleatoria.nombre,persona_aleatoria.apellido)
    print(PersonaAleatoria.NOMBRES)