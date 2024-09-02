# Definir la matriz bidimensional
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def buscar_valor(matriz, valor):
    """
    Busca un valor en una matriz bidimensional.

    :param matriz: Lista de listas que representa la matriz.
    :param valor: El valor a buscar en la matriz.
    :return: Tupla con la posición (fila, columna) si se encuentra el valor, o None si no se encuentra.
    """
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == valor:
                return (fila, columna)
    return None


# Valor a buscar
valor_buscado = 5

# Llamar a la función y mostrar el resultado
resultado = buscar_valor(matriz, valor_buscado)
if resultado:
    print(f"El valor {valor_buscado} se encontró en la posición: {resultado}")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")







