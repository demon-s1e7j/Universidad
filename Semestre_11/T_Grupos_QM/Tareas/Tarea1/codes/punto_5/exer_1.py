from typing import Tuple
import sympy as sp

Point = Tuple[sp.Symbol, sp.Symbol]

def distancia(p1: Point, p2: Point) -> sp.Expr:
    return sp.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

R_1 = (-sp.sqrt(3)/2, -sp.Rational(1,2))
R_2 = ( sp.sqrt(3)/2, -sp.Rational(1,2))
R_3 = (0, 1)

puntos = {k: v for k, v in globals().items() if 'R_' in k}

for n_i, v_i in puntos.items():
    for n_j, v_j in puntos.items():
        dist = distancia(v_i, v_j)
        dist_simplificada = sp.simplify(dist)
        print(f"Longitud Equilibrio {n_i} - {n_j}: {dist_simplificada}")
