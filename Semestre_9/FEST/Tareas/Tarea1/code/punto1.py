import os
import math

os.system('clear')

def probability(n: int, N: int, p1: float = 1/6, p2: float = 5/6) -> float:
    comb = math.comb(N, n)
    prob1 = math.pow(p1, n)
    prob2 = math.pow(p2, N - n)
    return comb*prob1*prob2

## Punto 1
print("Parte A:", probability(2, 6))

## Punto 2
print("Parte B:", 1 - sum([probability(n, 6) for n in range(2)]))

## Punto 3
print("Parte C:", probability(4, 6))
