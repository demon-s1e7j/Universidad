import sympy as sp

r = sp.Symbol("r", positive=True)
a0 = sp.Symbol("a0", positive=True)

exp = sp.exp(- r / (2 * a0))**2 * r**2
result = sp.integrate(exp, (r, 0, sp.oo))
sp.print_latex(result)
