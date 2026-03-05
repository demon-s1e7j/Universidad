from typing import Tuple
import sympy as sp

Point = Tuple[sp.Symbol, sp.Symbol]

x1, x2, x3, y1, y2, y3 = sp.symbols("x_1 x_2 x_3 y_1 y_2 y_3")
k = sp.Symbol('k')

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

def U_resorte(l_new):
    return sp.Rational(1, 2) * k * (l_new - sp.sqrt(3))**2

def calcular_matriz(U, derivandos):
    def doble_derivada(U, i, j):
        return sp.diff(sp.diff(U, i), j)

    n = len(derivandos)

    matrix = [[sp.Integer(0) for _ in range(n)] for _ in range(n)]

    for n_i, i in enumerate(derivandos):
        for n_j, j in enumerate(derivandos):
            derivada_segunda = doble_derivada(U, i, j)
            valor_equilibrio = derivada_segunda.subs({var: 0 for var in derivandos})
            matrix[n_i][n_j] = valor_equilibrio
    return sp.Matrix(matrix)

puntos = ['1', '2', '3']

U: sp.Expr = 0
for i in puntos:
    for j in puntos:
        if j >= i:
            continue
        new_r_i = avanzar_tiempo(i)
        new_r_j = avanzar_tiempo(j)
        dist = distancia(new_r_i, new_r_j)
        dist_simplificada = sp.simplify(dist)
        U += U_resorte(dist_simplificada)

U_simpl = sp.simplify(U)

m = sp.Symbol('m')

h = [x1, y1, x2, y2, x3, y3]

K = calcular_matriz(U, h)

M = m * sp.eye(len(h))

Lambda = M.inv() * K

sqrt3 = sp.sqrt(3)

D_e = sp.eye(2)
D_rho = sp.Matrix([[-sp.S(1)/2, -sqrt3/2], [sqrt3/2, -sp.S(1)/2]])
D_tau = sp.Matrix([[-sp.S(1)/2, sqrt3/2], [-sqrt3/2, -sp.S(1)/2]])

D_s3 = sp.Matrix([[-1, 0], [0, 1]]) 
D_s1 = D_rho * D_s3 * D_tau
D_s2 = D_tau * D_s3 * D_rho

P_e = sp.eye(3)
P_rho = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
P_tau = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])

P_s1 = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
P_s2 = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
P_s3 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])

operaciones = [
    sp.kronecker_product(P_e, D_e),
    sp.kronecker_product(P_rho, D_rho),
    sp.kronecker_product(P_tau, D_tau),
    sp.kronecker_product(P_s1, D_s1),
    sp.kronecker_product(P_s2, D_s2),
    sp.kronecker_product(P_s3, D_s3)
]

P1 = (sp.S(1)/6) * sum(operaciones, sp.zeros(6, 6))

P1_clean = sp.nsimplify(P1)

v_1 = sp.simplify(P1_clean * sp.Matrix([0, 0, 0, 0, 0, 1]))

print(f"Vector Propio:")
print(f"$$v_1 = {sp.latex(v_1)}$$")

Lambda_v_1 = sp.simplify(Lambda * v_1)
print(f"Aplicando Lambda al Vector Propio:")
print(f"$$\\Lambda v_1 = {sp.latex(Lambda_v_1)}$$")

idx = next(i for i, val in enumerate(v_1) if val != 0)
lambda_1 = sp.simplify(Lambda_v_1[idx] / v_1[idx])

print(f"\nlambda obtenido: ${sp.latex(lambda_1)}$", end='\n\n')

diff = sp.simplify(Lambda_v_1 - (lambda_1 * v_1))
verification = diff == sp.zeros(6, 1)

print(f"Es vector propio real: {verification}")
if not verification:
    sp.pprint(diff)
