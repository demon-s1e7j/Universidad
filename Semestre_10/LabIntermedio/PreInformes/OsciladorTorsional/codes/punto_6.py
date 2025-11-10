import sympy as sp

I, b, kappa, mu, k, i0, omega = sp.symbols('I b kappa mu k i_0 omega', real=True, positive=True)
A, phi = sp.symbols('A phi', real=True)

Z = -I*omega**2 + sp.I*b*omega + kappa

A_complex = mu * k * i0 / Z
A_magnitude = sp.simplify(sp.Abs(A_complex))
phi_angle = sp.simplify(sp.arg(A_complex))

sp.print_latex(f"A = {A_magnitude}")
sp.print_latex(f"phi = {phi_angle}")
