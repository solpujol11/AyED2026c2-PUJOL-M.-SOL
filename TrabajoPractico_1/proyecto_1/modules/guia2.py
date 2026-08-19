def calcular_potencia_dos_iterativo(n):
    if not isinstance(n, int):
        raise TypeError("El n debe ser un número entero")
    if n < 0:
        raise ValueError("El n debe ser un número entero no negativo")
    resultado = 1
    for i in range (0,n,1):
        resultado=resultado*2
    return resultado
