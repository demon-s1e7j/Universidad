import sympy as sp

z, R, d, I, mu0 = sp.symbols('z R d I mu0', real=True, positive=True)

B = (mu0*I*R**2/sp.Integer(2)) * (
    1 / ((R**2 + (z - d/sp.Integer(2))**2)**(sp.Rational(3, 2))) +
    1 / ((R**2 + (z + d/sp.Integer(2))**2)**(sp.Rational(3, 2)))
)

dBdz = sp.diff(B, z)

d2Bdz2 = sp.diff(dBdz, z)

print("B(z) =")
sp.print_latex(sp.simplify(B))
print("\n")
print("dB/dz =")
sp.print_latex(sp.simplify(dBdz))
print("\n")
print("d^2B/dz^2 =")
sp.print_latex(sp.simplify(d2Bdz2))
print("\n")

eq = sp.Eq(d2Bdz2.subs(z, 0), 0)

print("d^2B/dz^2(0) =")
sp.print_latex(sp.simplify(eq))
print("\n")

solution_for_d = sp.solve(eq, d, dict=True)
print("Solucion para d de modo que d^2B/dz^2(0) = 0:")
sp.print_latex(solution_for_d)
print("\n")
