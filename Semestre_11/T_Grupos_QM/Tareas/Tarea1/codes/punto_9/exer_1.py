import sympy as sp

sqrt3 = sp.sqrt(3)
un_medio = sp.S(1)/2

D_e = sp.eye(2)
D_rho = sp.Matrix([[-un_medio, -sqrt3/2], [sqrt3/2, -un_medio]])
D_tau = sp.Matrix([[-un_medio, sqrt3/2], [-sqrt3/2, -un_medio]])

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

print("Proyector $P^{(1)}$ (Exacto):")
print(f"$${sp.latex(P1_clean)}$$")
print(f"\nTraza de $P^{(1)}: {sp.simplify(P1.trace())}$")
