from scipy.constants import (
        Rydberg
)

from sympy.physics.units import (
        meter
)

import duckdb

duckdb.read_csv("./data")

R = Rydberg* (1/meter)

print(type(R))
print(R)
