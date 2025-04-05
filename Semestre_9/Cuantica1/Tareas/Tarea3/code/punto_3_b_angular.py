import sympy as sp

theta, phi = sp.symbols('theta phi', real=True)

norm_const = sp.sqrt(3/(8*sp.pi))

Y = - norm_const * sp.exp(-sp.I*phi) * sp.sin(theta)
Y_abs2 = Y * sp.conjugate(Y)
Y_abs2 = sp.simplify(Y_abs2)
expr = Y_abs2 * sp.sin(theta)

integral = sp.integrate(expr, (phi, 0, sp.pi/3), (theta, 0, sp.pi/4))

sp.print_latex(integral)
