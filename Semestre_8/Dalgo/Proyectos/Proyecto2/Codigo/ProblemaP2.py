from enum import Enum
import sys
from typing import Callable, Dict, List, Tuple, TypeVar
import math
from copy import deepcopy

# AUXILIARES

T = TypeVar("T")
W = TypeVar("W")


def print_matrix(matrix: List[List[T]]) -> None:
    for v in matrix:
        print(v)


def change(origin: str, destiny: str):
    def inner(func):
        def wrapper(*args):
            return func(*args).replace(origin, destiny)
        return wrapper
    return inner


@change("\n", "")
@change(" ", "")
def clean(v: str) -> str:
    return v.strip()


def readLine() -> str | None: return sys.stdin.readline()


def atoi(val: str | None):
    if val is None:
        raise ValueError('No se puede sacar el valor de nada')
    return int(val)


def checkNone(v: T | None) -> T:
    if v is None:
        raise ValueError("Este valor no puede ser 0")
    return v


def try_or_default(function: Callable[[T], W],
                   parameter: T,
                   default: W,
                   errorMessage: str,
                   errorType=ValueError) -> W:
    value: W
    try:
        value = function(parameter)
    except errorType as e:
        print(errorMessage, e, file=sys.stderr)
        value = default
    return value


# FORD FULKERSON
"""
Es importante aclarar que este sector no fue desarrollado por mi.
Para la implementación de este problema era necesario conocer el
flujo maximo que se puede obtener de este grafo y para eso vamos
a usar el algoritmo de FORD FULKERSON pues no serviria de nada
intentar encontrar un algoritmo mejor.
"""


class Graph:

    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)

    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] is False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        return False

    def FordFulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0
        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

# CLASES UTILES


class TipoCelula(Enum):
    INICIADORA = 1
    CALCULADORA = 2
    EJECUTORA = 3


class Neurona():
    def __init__(self, values: str | None):
        if values is None:
            raise ValueError("No se puede crear una neurona de la nada")
        v = values.strip().split()
        self.identifier: int = atoi(v[0])
        self.x, self.y = (atoi(v[1]), atoi(v[2]))
        self.position = self.x, self.y
        self.cellType: TipoCelula = TipoCelula(atoi(v[3]))
        self.peptides: List[str] = [clean(v[a]) for a in range(4, len(v))]

    def __str__(self) -> str:
        return f"Esta neurona tiene es {
            self.identifier} es de tipo {
            self.cellType.name}, se encuentra en la posición {
            self.position} y tiene los peptidos {
                self.peptides}"

    def distance(self, n):
        distance = math.sqrt((self.x - n.x)**2 + (self.y - n.y)**2)
        return distance

# INPUT


def get_case_description(i: int) -> Tuple[int, int]:
    values = readLine()
    if values is None:
        raise ValueError(f"El caso {i} no tiene descripción")
    values = [atoi(n) for n in values.strip().split(" ")]
    return (values[0], values[1])


def get_matrix(
        n_celulas: int) -> Tuple[List[List[int]], Dict[int, Neurona]]:
    matrix: List[List[int]] = [[0] * n_celulas for __ in range(n_celulas)]
    peptides_share: Dict[str, List[int]] = {}
    neuronas: Dict[int, Neurona] = {}
    for n in range(n_celulas):
        line = readLine()
        neurona = Neurona(line)
        neuronas[neurona.identifier] = neurona
        for peptide in neurona.peptides:
            if peptides_share.get(peptide) is None:
                peptides_share[peptide] = []
            peptides_share[peptide].append(neurona.identifier)

    for cells in peptides_share.values():
        for cell1 in cells:
            for cell2 in cells:
                matrix[cell1 - 1][cell2 - 1] += 1 if cell1 != cell2 else 0
    return matrix, neuronas

# CHANGE MATRIX


def check_distances(matrix: List[List[int]], neuronas: Dict[int, Neurona], d):
    for a in range(len(matrix)):
        for b in range(len(matrix[0])):
            neurona1 = checkNone(neuronas.get(a + 1))
            neurona2 = checkNone(neuronas.get(b + 1))
            if neurona1.distance(neurona2) > d:
                matrix[a][b] = 0


def set_gsink_gsource(matrix: List[List[int]], neuronas: Dict[int, Neurona]):
    size = len(matrix)
    for v in range(size):
        matrix[v].append(0)
        matrix[v].append(0)
    matrix.append([0] * (size + 2))
    matrix.append([0] * (size + 2))
    for key, value in neuronas.items():
        k = key - 1
        match value.cellType:
            case TipoCelula.INICIADORA:
                # matrix[k][-2] = sys.maxsize
                matrix[-2][k] = sys.maxsize
            case TipoCelula.CALCULADORA:
                pass
            case TipoCelula.EJECUTORA:
                matrix[k][-1] = sys.maxsize
                # matrix[-1][k] = sys.maxsize


def remove_cell(matrix, remove):
    for v in range(len(matrix)):
        matrix[remove][v] = 0
        matrix[v][remove] = 0

# EXECUTE FORD-FULKERSON


def get_max_flow(matrix: List[List[int]],
                 source: int,
                 sink: int,
                 remove: int = -1):
    new_matrix = deepcopy(matrix)
    if remove >= 0:
        remove_cell(new_matrix, remove)
    g = Graph(new_matrix)
    return g.FordFulkerson(source, sink)

# MAIN


linea: str | None
casos: int

try:
    linea = readLine()
    casos = try_or_default(
        atoi,
        linea,
        0,
        "El numero de casos no concuerda con el formato esperado")
    for i in range(casos):
        n_celulas, distancia_max = get_case_description(i)
        matrix, neuronas = get_matrix(n_celulas)
        check_distances(matrix, neuronas, distancia_max)
        set_gsink_gsource(matrix, neuronas)
        original_flow = get_max_flow(matrix, n_celulas, n_celulas + 1)
        best_cell = 0
        best_value = sys.maxsize
        for v in range(n_celulas):
            neurona = neuronas.get(v + 1)
            if neurona is not None and neurona.cellType is TipoCelula.CALCULADORA:
                max_flow = get_max_flow(
                    matrix, n_celulas, n_celulas + 1, remove=v)
                if max_flow <= best_value:
                    best_cell = v + 1
                    best_value = max_flow
        print(f"{best_cell} {original_flow} {best_value}")
except BaseException as e:
    print("Ocurrio un error desconocido", e)
