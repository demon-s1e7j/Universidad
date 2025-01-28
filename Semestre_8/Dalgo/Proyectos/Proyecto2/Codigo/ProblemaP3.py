import functools
from typing import Callable, Dict, List, Tuple, Any, TypeVar
import itertools
import sys
import math
import os
import errno
import signal
import time

T = TypeVar("T")

def matches(l1: List[T], l2: List[T]) -> int:
    return sum(a in l2 for a in l1)

def strip(func: Callable[..., str]):
    def inner(*args, **kwargs):
        return func(*args, **kwargs).strip()
    return inner

def intOrDefault(v: str, default: int = 0, ErrorCode: str = "Ocurrio un error intentando convertir a int:"):
    try:
        value: int | None = int(v)
        return value if value is not None else default
    except Exception as e:
        print(ErrorCode, e, file=sys.stderr)
        return default

def timeout(seconds: int = 10, error_message=os.strerror(errno.ETIME)):
    def decorator(func: Callable[...,Any]):
        def handleTimeout(signum, frame):
            raise TimeoutError(error_message)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, handleTimeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wrapper
    return decorator


def change(org: str, new: str):
    def decorator(func: Callable[..., str]):
        def inner(*args, **kwargs):
            return func(*args, **kwargs).replace(org, new)
        return inner
    return decorator

def checkLength(length: int, default: Any = 0, ErrorCode: str="Ocurrio un error con el tamaño"):
    def decorator(func: Callable[..., List[Any]]):
        def inner(*args, **kwargs):
            val = func(*args, **kwargs)
            if len(val) != length:
                print(ErrorCode, file=sys.stderr)
                return default
            return val
        return inner
    return decorator

def printMatrix(matrix: List[List[Any]]) -> None:
    for a in matrix:
        for b in a:
            print(b, end=" ")
        print()
    return None

@strip
def readStdIn() -> str:
    return sys.stdin.readline()

def readLineOfNumbers(ErrorCode: str = "Ocurrio un error intentando convertir a int:") -> List[int]:
    return [intOrDefault(v, ErrorCode=ErrorCode) for v in readStdIn().split(" ")]

class Cell():
    def __init__(self) -> None:
        values = [v.strip() for v in readStdIn().split(" ")]
        self.id = intOrDefault(values[0]) - 1
        self.x, self.y = intOrDefault(values[1]), intOrDefault(values[2])
        self.position = self.x, self.y
        self.peptides = values[3:]

    def __str__(self) -> str:
        return f"Esta celula es {self.id} tiene una posición {self.position} y sus peptidos son {self.peptides}"

    def distance(self, cellB):
        return math.sqrt(abs(self.x - cellB.x)**2 + abs(self.y - cellB.y)**2)

def valueBetweenCells(cellA: Cell, cellB: Cell, distance: int = 1) -> int:
    if (cellA == cellB):
        return 0
    if cellA.distance(cellB) > distance:
        return 0
    return matches(cellA.peptides, cellB.peptides)
    

def getNumberOfCases() -> int:
    ErrorCode = "Ocurrio un error al intentar conseguir el numero de casos:"
    return intOrDefault(readStdIn(), ErrorCode=ErrorCode)

def getNumberOfCellsAndDistance() -> Tuple[int, int]:
    ErrorCode = "Ocurrio un error al intentar conseguir el numero de celulas o la distancia:"
    @checkLength(2, [0, 0])
    def getNandD() -> List[int]:
        return readLineOfNumbers(ErrorCode=ErrorCode)
    val = getNandD()
    return val[0], val[1]

def getMatrix(n: int, d: int) -> List[List[int]]:
    matrix: List[List[int]] = [[0] * n for _ in range(n)]
    cells: List[Cell] = []
    for _ in range(n):
        cells.append(Cell())
    for cellA in cells:
        for cellB in cells:
            value = valueBetweenCells(cellA, cellB, distance=d)
            matrix[cellA.id][cellB.id] = value
            matrix[cellB.id][cellA.id] = value
    return matrix

def getPossibleCliques(n: int) -> List[int]:
    all_combs =  []
    nums = range(n)
    for r in range(n):
        combs = itertools.combinations(nums, r)
        all_combs.extend(combs)
    return all_combs

def setDefault(n: int) -> Dict[int, int]:
    return {a + 1 : 0 for a in range(n)}

def calculateCase(n: int, d: int):
    matrix = getMatrix(n, d)
    possible_cliques = getPossibleCliques(n)
    print(possible_cliques)
    return {1: 0}

@timeout()
def manageCase() -> Dict[int, int]:
    n, d = getNumberOfCellsAndDistance()
    val: Dict[int, int] = {1: 0}
    try:    
        val = calculateCase(n, d)
    except TimeoutError:
        val = setDefault(n)
    return val

def main() -> None:
    cases = getNumberOfCases()
    for _ in range(cases):
        values = manageCase()
        for k, v in values.items():
            print(f"{k} {v}")

if __name__ == "__main__":
    main()
