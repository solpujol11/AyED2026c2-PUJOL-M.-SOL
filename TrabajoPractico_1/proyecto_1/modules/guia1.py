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
        self.establecer_nombre(nombre)
        self.establecer_apellido(apellido)
    def establecer_nombre(self,nuevo_nombre):
        if isinstance (nuevo_nombre,str):
            self.__nombre = nuevo_nombre.capitalize()
        else:
            raise TypeError ("Nombre no es un str")
    def establecer_apellido(self,nuevo_apellido):
        if isinstance (nuevo_apellido,str):
            self.__apellido = nuevo_apellido.capitalize()
        else:
            raise TypeError ("Nombre no es un str")
    #GETTERS
    def obtener_nombre(self):
        return self.__nombre
    def obtener_apellido(self):
        return self.__apellido

def prueba_persona():
    p=Persona("sol","pujol")
    print ("Nombre:", p.obtener_nombre())
    print ("Apellido:", p.obtener_apellido())
    try:
        p_error=Persona(123,"Pujol")
    except TypeError as e:
        print("Error detectado:",e)

if __name__ == "__main__":
    prueba_persona()

#otraforma
    def __init__(self,nombre,apellido):
        if isinstance(nombre,str):
            if isinstance(apellido,str):
                self.__nombre=nombre.capitalize()
                self.__apellido=apellido.capitalize()
            else:
                raise TypeError ("Nombre no es un string")
        else:
            raise TypeError ("Apellido no es un string")


# ejercicio 4
class Estudiante:
    def __init__(self,legajo,apellido,nombre,documento,promedio):
        self.establecer_legajo(legajo)
        self.establecer_apellido(apellido)
        self.establecer_nombre(nombre)
        self.establecer_documento(documento)
        self.establecer_promedio(promedio)
#SETTERS (MÉTODOS PARA ESTABLECER Y VALIDAR)
    def establecer_legajo(self,nuevo_legajo):
        try:
            legajo_int=int(nuevo_legajo)
            if legajo_int <=0:
                raise ValueError ("Legajo debe ser mayor que 0")
            self._legajo=legajo_int
        except (ValueError,TypeError):
            raise ValueError ("legajo debe ser un numero valido")
    def establecer_apellido_nombre(self,nuevo_apellido_nombre):
        if isinstance(nuevo_apellido_nombre,str):
            self._apellido_nombre = nuevo_apellido_nombre
        else:
            raise TypeError ("Apellido y nombre han de ser str")
    def establecer_documento(self,nuevo_documento):
        try:
            documento_int=int(nuevo_documento)
            if documento_int<=0:
                raise ValueError ("Documento ha de ser un numero mayor a 0")
            self._documento = documento_int
        except (ValueError,TypeError):
            raise TypeError("El documento debe ser un número entero válido.")
    def establecer_promedio(self,nuevo_promedio):
        try:
            promedio_float=float(nuevo_promedio)
            if 0.00<=promedio_float<=10.00:
                self._promedio=promedio_float
            else:
                raise ValueError("Promedio debe ser un numero entre 0 y 10")
        except(ValueError,TypeError):
            raise TypeError("Promedio debe ser un flotante valido")

    #GETTERS PARA OBTENER
    def obtener_legajo(self):
        return self._legajo
    def obtener_apellido_nombre(self):
        return self._apellido_nombre
    def obtener_documento(self):
            return self._documento
    def obtener_promedio(self):
            return self._promedio

    #LECTURA Y PROCESAMIENTO DEL ARCHIVO
def cargar_y_ordenar_estudiantes(ruta_archivo):
    estudiantes = []

    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.strip()
                
                # Si la línea no está vacía, la procesamos
                if linea:
                    partes = linea.split(',')
                    
                    # Verificamos que tenga los 4 datos
                    if len(partes) == 4:
                        try:
                            # Creamos el estudiante con sus datos
                            est = Estudiante(partes[0], partes[1], partes[2], partes[3])
                            estudiantes.append(est)
                        except (TypeError, ValueError) as error:
                            print("Dato inválido ignorado:", error)

    except FileNotFoundError:
        print("No se encontró el archivo")
        return []

    estudiantes.sort(key=lambda est: est.obtener_legajo())
    return estudiantes


def prueba_estudiantes():
    lista = cargar_y_ordenar_estudiantes("estudiantes.txt")

    for est in lista:
        print("Legajo:", est.obtener_legajo(), 
              "| Nombre:", est.obtener_apellido_y_nombre(), 
              "| DNI:", est.obtener_documento(), 
              "| Promedio:", est.obtener_promedio())


if __name__ == "__main__":
    prueba_estudiantes()

#ejercicio 5
import random
class Persona_Aleatoria(Persona):
    NOMBRE=["sol","juli","maxi","pri","anita","maga"]
    APELLIDO=["pujol","fumero","forni","beltramino","bosco","diaz"]
    def __init__(self):
        nombre=random.choice(self.NOMBRE)
        apellido=random.choice(self.APELLIDO)
        super().__init__(nombre,apellido) #llamar a su clase madre (persona) y llama al init de la clase madre
if __name__ == "__main__":
    personaaleatoria=Persona_Aleatoria()
    print(personaaleatoria.obtener_nombre(),personaaleatoria.obtener_apellido())

#ejercicio 6
    
