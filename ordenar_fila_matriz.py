def bubble_sort(fila):
    """
    Ordena una fila usando el algoritmo de Bubble Sort.

    :param fila: Lista de números a ordenar.
    :return: La lista ordenada en orden ascendente.
    """
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila


# Definir la matriz bidimensional
matriz = [
    [7, 2, 5],
    [1, 9, 3],
    [4, 6, 8]
]

# Mostrar la matriz original
print("Matriz Original:")
for fila in matriz:
    print(fila)

# Índice de la fila a ordenar (por ejemplo, la segunda fila, índice 1)
fila_a_ordenar = 1

# Ordenar la fila específica
matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)








