# 1) Definir una función que tome como argumento una lista y devuelva el mayor de sus elementos
def encontrar_mayor (lista):
    """
    Encuentra el maximo de una lista.
    Precondiciones:
        - lista es una lista no vacía
        - lista es una lista de elementos comparables
    Postcondiciones:
        - devuelve el mayor de los elementos de la lista
    Raises
        -ValueError si lista está vacía
        -TypeError si lista contiene elementos no comparables
    """
    N=len(lista)
    if N==0:
        raise ValueError("La lista está vacía")
    else:
        maximo=lista[0]
        for i in range (N):
            if lista [i]>maximo:
                maximo=lista[i]
    return (maximo)   

def main():
    lista=[3, 5, 2, 8, 1]
    maximo = encontrar_mayor(lista)
    print(maximo)

if __name__ == "__main__":
    main()
