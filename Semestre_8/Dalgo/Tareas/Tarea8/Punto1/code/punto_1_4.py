import sys

def isAllUnique(route):
    visited = []
    for i in route:
        if i in visited:
            return False
    return True

def analize(matrix, k, route):
    if (route[0] != route[-1]):
        return False
    if (len(route) != len(matrix) + 1):
        return False
    if (not isAllUnique(route[:-2])):
        return False
    value = sum(matrix[route[n]][route[n + 1]] 
             for n in range(len(route) - 1))
    return value <= k

def get_matrix():
    matrix = []
    n = int(sys.stdin.readline())
    for __ in range(n):
        matrix.append([int(n) for n in sys.stdin.readline().split(" ")])
    return matrix

def get_k():
    return int(sys.stdin.readline())

def get_route():
    return [int(n) for n in sys.stdin.readline().split(" ")]

if __name__ == "__main__":
    matrix = get_matrix()
    k = get_k()
    route = get_route()

    print(analize(matrix, k, route))

"""
El formato de entrada debe seguir esta estructura:

(numero de nodos de la matriz)
(matriz fila a fila)
(valor a checkear)
(ruta que inicia y termina en el mismo lugar)

Un ejemplo de este formato seria:

3
0 10 10
10 0 10
10 10 0
30
0 1 2 0
"""
