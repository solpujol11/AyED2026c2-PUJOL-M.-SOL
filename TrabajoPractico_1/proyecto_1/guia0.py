def encontrar_el_maximo(lista):
    """
    Encuentra el maximo de una lista.
    Precondiciones:
        - lista es una lista no vacía
        - lista es una lista de elementos comparables
    Postcondiciones:
        -
    Raises
        -ValueError si lista está vacía
        -TypeError si lista contiene elementos no comparables
    """
    N = len(lista)
    if N == 0: #Equivalanete a N<1
        raise ValueError("La lista está vacía")
    maximo = lista[0]
    for i in range(N):
        if lista[i] > maximo:
            maximo = lista[i]
    return maximo

def main():
    lista=[3, 5, 2, 8, 1]
    maximo = encontrar_el_maximo(lista)
    print(maximo)

if __name__ == "__main__":
    main()
