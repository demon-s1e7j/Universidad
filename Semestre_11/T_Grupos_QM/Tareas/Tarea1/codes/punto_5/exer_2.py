from typing import Tuple
import sympy as sp

Point = Tuple[sp.Symbol, sp.Symbol]

x1, x2, x3, y1, y2, y3 = sp.symbols("x_1 x_2 x_3 y_1 y_2 y_3")

R_1 = (-sp.sqrt(3)/2, -sp.Rational(1,2))
R_2 = ( sp.sqrt(3)/2, -sp.Rational(1,2))
R_3 = (0, 1)

def distancia(p1: Point, p2: Point) -> sp.Expr:
    return sp.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def avanzar_tiempo(atomo: str = '1'):
    pos_equiv = globals()[f"R_{atomo}"]
    plus_x = globals()[f"x{atomo}"]
    plus_y = globals()[f"y{atomo}"]
    return (pos_equiv[0] + plus_x, pos_equiv[1] + plus_y)

puntos = ['1', '2', '3']

print('\\begin{itemize}')
for i in puntos:
    for j in puntos:
        if j >= i:
            continue
        new_r_i = avanzar_tiempo(i)
        new_r_j = avanzar_tiempo(j)
        dist = distancia(new_r_i, new_r_j)
        dist_simplificada = sp.simplify(dist)
        print(f"\t\\item $L_{{{j}{i}}}:\\ {sp.latex(dist_simplificada)}$")
print('\\end{itemize}')
