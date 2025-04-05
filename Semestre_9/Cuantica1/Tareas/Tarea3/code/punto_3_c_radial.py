import sympy as sp

r = sp.Symbol("r", positive=True)
a0 = sp.Symbol("a0", positive=True)

exp = 1/(2 * a0**3) * sp.exp(- r / (2 * a0))**2 * r**3
result = sp.integrate(exp, (r, 0, sp.oo))
sp.print_latex(result)
