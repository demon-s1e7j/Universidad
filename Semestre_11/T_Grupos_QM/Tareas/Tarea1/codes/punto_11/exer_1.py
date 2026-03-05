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

chi2 = [2, -1, -1, 0, 0, 0]
P2 = (sp.S(2)/6) * sum([chi2[i] * operaciones[i] for i in range(6)], sp.zeros(6, 6))


P2_clean = sp.nsimplify(P2)
print(f"$P^2$ completo:\n $${sp.latex(P2_clean)}$$")

ux = sp.Matrix([1, 0, 1, 0, 1, 0]) / sp.sqrt(3)
uy = sp.Matrix([0, 1, 0, 1, 0, 1]) / sp.sqrt(3)

E_trasl = sp.simplify(ux * ux.T + uy * uy.T)

P_vib = sp.simplify(P2 - E_trasl)

print(f"$P_{{vib}}$: $${sp.latex(sp.simplify(P_vib))}$$")
print(f"Traza de $P_{{vib}}$: ${sp.latex(sp.simplify(P_vib.trace()))}$", end='\n\n')

v2a = sp.simplify(P_vib * sp.Matrix([1, 0, 0, 0, 0, 0]))
v2b = sp.simplify(P_vib * sp.Matrix([0, 1, 0, 0, 0, 0]))

Lambda_v2a = sp.simplify(Lambda * v2a)
idx = next(i for i in range(6) if v2a[i] != 0)
lambda_2 = sp.simplify(Lambda_v2a[idx] / v2a[idx])

print(f"Valor propio para modo E: ${sp.latex(lambda_2)}$")
