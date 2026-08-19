from modules.guia1 import CalculadoraIMC
from modules.guia2 import calcular_potencia_dos_iterativo

if __name__ == "__main__":
    calculadora = CalculadoraIMC(75,1.80)
    print(calculadora.info)

    potencia = calcular_potencia_dos_iterativo(9)
    print(f"El resultado es: {potencia}")