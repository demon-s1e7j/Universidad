import sympy as sp

z, R, d, I, mu0, B_tierra = sp.symbols(
    'z R d I mu0 B_tierra', real=True, positive=True)

B = (mu0*I*R**2/sp.Integer(2)) * (
    1 / ((R**2 + (z - d/sp.Integer(2))**2)**(sp.Rational(3, 2))) +
    1 / ((R**2 + (z + d/sp.Integer(2))**2)**(sp.Rational(3, 2)))
)

B_center = B.subs({z: 0, d: R})
B_center_simp = sp.simplify(B_center)
print("B(0) =")
sp.print_latex(B_center_simp)

eq = sp.Eq(B_center_simp, B_tierra)
sp.print_latex(eq)

I_sol = sp.simplify(sp.solve(eq, I)[0])
print("I = ")
sp.print_latex(I_sol)
