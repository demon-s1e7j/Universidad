from typing import Generator, Tuple
import pandas as pd
import numpy as np
from math import factorial
from collections import Counter
import os

os.system('clear')

def degeneramiento(tupla):
    total = factorial(len(tupla))
    repeticiones = Counter(tupla)

    for key, rep in repeticiones.items():
        total //= factorial(rep)
        total *= 2*rep if key != 0 else 1

    return total

def succesion() -> Generator[Tuple[int, int, int], None, None]:
    a = 1
    while True:
        for b in range(a + 1):
            for c in range(b + 1):
                yield (a, b, c)
        a += 1

def index(value):
    def helper(h: int, k: int, l: int):
        return np.pow(h, 2) + np.pow(k, 2) + np.pow(l, 2)
    last = (0, 0, 0)
    for h, k, l in succesion():
        val = helper(h, k, l) 
        if val == value:
            return h, k, l
        if val > value:
            return last
        last = (h, k, l)

data = pd.read_csv("./data_5.csv")
data["theta"] = np.radians(data["2theta"] / 2)
data["sin"] = np.sin(data["theta"])
data["sin^2"] = np.pow(data["theta"], 2)
data["s/s"] = (data["sin^2"] / data["sin^2"][0]).round().astype(int)
data.loc[6, "s/s"] = 8
data.loc[9, "s/s"] = 12
data["hkl"] = data["s/s"].apply(index)
data["m"] = data["hkl"].apply(degeneramiento)
print(data)
