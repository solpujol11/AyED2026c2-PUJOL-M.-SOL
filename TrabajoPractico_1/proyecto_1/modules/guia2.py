def calcular_potencia_dos_iterativo(n):
    if not isinstance(n, int):
        raise TypeError("El n debe ser un número entero")
    if n < 0:
        raise ValueError("El n debe ser un número entero no negativo")
    if n == 0:
        return 1
    resultado = 1
    for i in range (0,n,1):
        resultado=resultado*2
    return resultado

def calcular_potencia_dos_recursivo(n):
    if not isinstance(n,int):
        raise TypeError ("El n debe ser un numero entero")
    if n<0:
        raise ValueError ("El n debe ser un numero entero no negativo")
    if n==0:
        return 1
    resultado=1
    return 2*calcular_potencia_dos_recursivo(n-1)

def calcular_fibonacci_recursiva(n):
    if not isinstance(n,int):
        raise TypeError ("El n debe ser un numero entero")
    if n<0:
        raise ValueError ("El n debe ser un numero entero no negativo")
    if n==0:
        return 0
    if n==1:
        return 1
    return calcular_fibonacci_recursiva(n-1)+calcular_fibonacci_recursiva(n-2)