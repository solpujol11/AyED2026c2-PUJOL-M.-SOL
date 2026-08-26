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
class Producto:
    def __init__(self,nombre,precio,unidades):
        self.establecer_nombre(nombre)
        self.establecer_precio(precio)
        self.establecer_unidades(unidades)
        self.__descuento = 0

    def establecer_nombre(self,nombre_final):
        if isinstance(nombre_final,str):
            self.__nombre = nombre_final
        else:
            raise TypeError ("Nombre debe ser un string")
    def establecer_precio(self,precio_final):
        if isinstance(precio_final,(int,float)):
            if precio_final>=0:
                self.__precio = precio_final
            else:
                raise ValueError ("Precio debe ser un numero mayor a 0")
        else:
            raise TypeError ("Precio debe ser un numero")
    def establecer_unidades(self,unidades_final):
        if isinstance(unidades_final,int):
            if unidades_final>=0:
                self.__unidades = unidades_final
            else:
                raise ValueError("Unidades debe ser mayor a 0")
        else:
            raise TypeError("Unidades debe ser un numero entero")
    def establecer_descuento(self,porcentaje):
        if isinstance(porcentaje,(int,float)) and 0<=porcentaje<=100:
            self.__descuento = porcentaje
        else:
            raise ValueError ("El porcentaje debe ser un numero entre 0 y 100")

    def obtener_nombres(self):
        return self.__nombre
    def obtener_precio(self):
        return self.__precio
    def obtener_unidades(self):
        return self.__unidades
    def descuento_final(self):
        monto_descuento = self.__precio * (self.__descuento / 100)
        return self.__precio - monto_descuento
    def mostrar_todo(self):
        print(f"Producto: {self.obtener_nombres()}, "
              f"Precio: {self.obtener_precio()}, "
              f"Precio con Desc: {self.descuento_final()}, "
              f"Unidades: {self.obtener_unidades()}")

def Prueba_Producto():
    p=Producto("tijera",300,15)
    p.mostrar_todo()
    print("PRECIO CON DESCUENTO")
    p.establecer_descuento(15)
    p.mostrar_todo()
    print("MODIFICANDO")
    p.establecer_precio(400)
    p.establecer_unidades(500)
    p.mostrar_todo()
    print("ERRORES")
    try:
        p_error=Producto(123,"Pujol",-10)
    except TypeError as e:
        print("Error detectado:",e)

if __name__ == "__main__":
    Prueba_Producto()

#ejercicio 7
class CalculadoraIMC:
    def __init__(self,peso,altura):
        self.establecer_peso(peso)
        self.establecer_altura(altura)

    def establecer_peso(self,peso_final):
        if isinstance(peso_final,(int,float)):
            if peso_final >0:
                self.peso=peso_final
            else:
                raise ValueError("Peso debe ser mayor a 0Kg")
        else:
            raise TypeError("Peso debe ser un numero")
        
    def establecer_altura(self,altura_final):
        if isinstance(altura_final,(int,float)) and altura_final>0:
            self.altura = float(altura_final)
        else:
            raise TypeError("Altura debe ser un float  mayor que 0")
    @property
    def imc(self):
        return self.peso/(self.altura**2)
    @property
    def darinfo(self):
        imc=self.imc
        if imc < 18.5:
            return f"Tu IMC {imc:.2f} está debajo de lo normal"
        elif imc < 25:
            return f"Tu IMC {imc:.2f} está en el rango normal"
        elif imc < 30:
            return f"Tu IMC {imc:.2f} indica Sobrepeso"
        else:
            return f"Tu IMC {imc:.2f} indica Obesidad"

def prueba_imc():
    p=CalculadoraIMC(61,1.67)
    print(p.darinfo)

if __name__ == "__main__":
    prueba_imc()

#ejercicio 8
class analizar_texto:
    CARACTERES = (',', '.', ':', ';', '-', '_')

    def __init__(self,texto):
        self.establecer_texto(texto)

    def establecer_texto(self,texto_nuevo):
        if isinstance(texto_nuevo,str):
            self.texto=texto_nuevo
            self.depurado=self.depurar(texto_nuevo)
        else:
            raise TypeError("El texto debe ser una cadena de string")

    def depurar(self,texto):
        texto_depurado=texto
        for caracteres in self.CARACTERES:
            texto_depurado = texto_depurado.replace(caracteres," ")
        return (texto_depurado)

    def obtener_palabras(self):
        return self.depurado.lower()
    def obtener_texto(self):
        return self.texto
    def obtener_depurado(self):
        return self.depurado
    def obtener_total_palabras(self):
        return len(self.obtener_palabras())

def prueba_palabra():
    texto_prueba = ("Hola, mundo: este es un texto-de prueba; sí, un_texto de prueba.")
    p = analizar_texto(texto_prueba)
    
    print(f"Original: {p.obtener_texto()}")
    print(f"Depurado: {p.obtener_depurado()}")
    print(f"Número total de palabras: {p.obtener_total_palabras()}")
    print("ERRORES")
    try:
        p("   ")
    except TypeError as e:
        print(f"Error detectado en inicialización: {e}")

if __name__ == "__main__":
    prueba_palabra()

#ejercicio 9
class Temperatura:
    UNIDADES = ("C", "K", "F")
    def __init__(self,temperatura,escala):
        self.establecer_temperatura(temperatura,escala)

    def establecer_temperatura(self,temperatura,escala):
        if not isinstance(temperatura,(int,float)):
            raise TypeError ("Temperatura debe ser un numero")
        if not isinstance(escala,str):
            raise TypeError ("La escala debe ser un string")
        escala=escala.upper()
        if escala not in self.UNIDADES:
            raise ValueError("La unidad no es valida")

        temperatura_kelvin=self.kelvin(float(temperatura),escala)
        if temperatura_kelvin <0:
            raise ValueError ("Calculo fisicamente no realizable")

        self.temperatura=float(temperatura)
        self.escala=escala

    def kelvin(self,temperatura,escala):
        if escala == "K":
            return temperatura
        elif escala == "C":
            return temperatura+273.15
        elif escala == "F":
            return (temperatura+459.67)*5/9

    def a_otra(self,kelvin,escala_final):
        if escala_final == 'K':
            return kelvin
        elif escala_final == 'C':
            return kelvin - 273.15
        elif escala_final == 'F':
            return (kelvin * 9 / 5) - 459.67

    def obtener_temperatura(self):
        return self.temperatura

    def obtener_escala(self):
        return self.escala

    def escala_destino(self,escala_final):
        if not isinstance(escala_final, str):
            raise TypeError("La escala final debe ser un texto.")

        final = escala_final.upper()
        if final not in self.UNIDADES:
            raise ValueError("Unidad no válida")
        if final == self.escala:
            return self.temperatura
        temp_kelvin = self.kelvin(self.temperatura, self.escala)
        return self.a_otra(temp_kelvin, final)

def prueba():
    temp = Temperatura(25, 'C')
    print(f"25°C a Kelvin: {temp.escala_destino('K'):.2f} K")
    print(f"25°C a Fahrenheit: {temp.escala_destino('F'):.2f} °F")
    print(f"25°C a Celsius (misma unidad): {temp.escala_destino('C')} °C")

    try:
        Temperatura(-300, 'C')
    except ValueError as e:
        print("Error detectado (< 0 K):", e)

    try:
        Temperatura(100, 'X')
    except ValueError as e:
        print("Error detectado (Unidad inválida):", e)

if __name__ == "__main__":
    prueba()
        
