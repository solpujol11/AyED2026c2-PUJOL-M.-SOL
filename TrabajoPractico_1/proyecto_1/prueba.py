from modules.guia0 import encontrar_el_maximo
if __name__ == "__main__":
    lista=[1,"a"]
    maximo=encontrar_el_maximo(lista)
    print(help(encontrar_el_maximo)) #ver documentacion en la funcion

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

if __name__ == "__main__":
    prueba_cuadrado()

from modules.guia1 import CalculadoraIMC

if __name__ == "__main__":
    calculadora = CalculadoraIMC(75,1.80)
    print(calculadora.info)