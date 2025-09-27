import sympy as sp

omega, mu, k_z, h, H_0, pi= sp.symbols("omega mu k_z h H_0 pi")
m, n, a, b = sp.symbols("m n a b")
x, y = sp.symbols("x y")

def S_z():
    fact1 = ((omega * mu * k_z) / h**4) * H_0
    term1 = ((n * pi)/b)**2 * (sp.cos((m * pi * x)/a))**2 * (sp.sin((n * pi * y)/b))**2
    term2 = ((m * pi)/a)**2 * (sp.sin((m * pi * x)/a))**2 * (sp.cos((n * pi * y)/b))**2
    return (1/2) * fact1 * (term1 + term2)

P1 = sp.integrate(S_z(), (x, 0, b), (y, 0, a))
P1_simplified = P1.simplify()

S_z_m0 = S_z().subs(m, 0)
P2 = sp.integrate(S_z_m0, (x, 0, b), (y, 0, a))
P2_simplified = P2.simplify()

S_z_n0 = S_z().subs(n, 0)
P3 = sp.integrate(S_z_n0, (x, 0, b), (y, 0, a))
P3_simplified = P3.simplify()

print("Caso 1: m ≠ 0, n ≠ 0")
sp.print_latex(P1_simplified)
print("\nCaso 2: m = 0, n ≠ 0")
sp.print_latex(P2_simplified)
print("\nCaso 3: m ≠ 0, n = 0")
sp.print_latex(P3_simplified)
