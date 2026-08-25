import random
#ejercicio 1
class Cuadrado:
    def __init__(self,lado):
        self.establecer_lado(lado)
    def establecer_lado(self,nuevo_lado):
        """
        Establece el lado en un nuevo valor
        Precondiciones:
            - nuevo_lado debe ser un valor numerico
            - nuevo_lado tiene que ser mayor a 0 
        Postcondiciones:
            - el lado cuadrado toma el valor nuevo_lado
        Raise:
            - ValueError si el lado no es numerico
            - TypeError si el lado es menor o igual a 0
        """
        if isinstance(nuevo_lado,(int,float)):
            if nuevo_lado>0:
                self.__lado = nuevo_lado
            else:
                raise ValueError ("El lado debe ser un numero mayor que 0")
        else:
            raise TypeError ("El lado debe ser un numero")

    def obtener_lado (self):
        return self.__lado

    def obtener_perimetro(self):
        return 4*self.__lado

    def obtener_area(self):
        return self.__lado*self.__lado

def prueba_cuadrado():
    cuadrado=Cuadrado(1)
    print(cuadrado.obtener_lado()) #deberia dar 1
    print(cuadrado.obtener_perimetro()) #deberia dar 4
    cuadrado.establecer_lado(2)
    print(cuadrado.obtener_lado()) #deberia dar 2
    print(cuadrado.obtener_perimetro()) #deberia dar 8
    print(Cuadrado)

if __name__ == "__main__":  
    prueba_cuadrado()

#ejercicio 2
class Punto:
    def __init__(self,x,y):
        self.establecer_x(x)
        self.establecer_y(y)
    def establecer_x(self,punto_x):
        if isinstance(punto_x,(int,float)):
            self.__x = punto_x
        else:
            raise TypeError ("x no es un numero")
    def establecer_y(self,punto_y):
        if isinstance(punto_y,(int,float)):
            self.__y = punto_y
        else:
            raise TypeError ("y no es un numero")
    def obtener_x(self):
        return self.__x
    def obtener_y(self):
        return self.__y
    def obtener_coordenadas(self):
        return self.__x,self.__y

def prueba_punto():
    p = Punto(3, 4.5)
    print("Coordenada X:", p.obtener_x())  # Muestra 3
    print("Coordenada Y:", p.obtener_y())  # Muestra 4.5
    print("Ambas coordenadas:", p.obtener_coordenadas())  # Muestra (3, 4.5)

    p.establecer_x(-10)
    print("Nueva X:", p.obtener_x())  # Muestra -10

    try:
        p.establecer_y("cuatro")
    except TypeError as e:
        print("Error capturado con éxito:", e)

if __name__ == "__main__":
    prueba_punto()

#ejercicio 3
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

class personaAleatoria(Persona):
    NOMBRES=["amanda","feli","sol"]
    APELLIDOS=["epson","franco","cabada","pujol"]

    def __init__(self):
        nombre = random.choice(self.NOMBRES)
        apellido = random.choice(self.APELLIDOS)
        super().__init__(nombre,apellido)

class CalculadoraIMC:
    def __init__(self, peso, altura):
        self.establecer_altura(altura)
        self.establecer_peso(peso)

    def establecer_altura(self, altura):
        if isinstance(altura,(int,float)):
            if altura > 0:
                self.altura = float(altura)
            else:
                raise ValueError ("Altura debe ser mayor que 0")
        else:
            raise TypeError ("Altura no es un float")

    def establecer_peso(self, peso):
        if isinstance(peso,(int,float)):
            if peso > 0:
                self.peso = float(peso)
            else:
                raise ValueError ("Peso debe ser mayor que 0")
        else:
            raise TypeError ("Peso no es un float")

    @property
    def imc (self):
        return self.peso / (self.altura ** 2)
    @property
    def info(self):
        imc = self.imc
        if imc < 18.5:
            return f"Tu IMC {imc:.2f} está debajo de lo normal"
        elif imc < 25:
            return f"Tu IMC {imc:.2f} está en el rango normal"
        elif imc < 30:
            return f"Tu IMC {imc:.2f} indica Sobrepeso"
        else:
            return f"Tu IMC {imc:.2f} indica Obesidad"

    
