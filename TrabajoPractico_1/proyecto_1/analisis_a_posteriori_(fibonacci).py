import time
from matplotlib import pyplot as plt
from modules.guia2 import calcular_fibonacci_recursiva
if __name__ == "__main__":
    n = 35
    tiempo = []
    for i in range (n):
        tiempo_inicial = time.perf_counter()
        calcular_fibonacci_recursiva(i)
        tiempo_final = time.perf_counter()
        tiempo.append(tiempo_final-tiempo_inicial)
    plt.plot(tiempo)
    plt.show()
