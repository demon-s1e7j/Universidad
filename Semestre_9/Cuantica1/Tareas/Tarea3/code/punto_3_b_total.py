import sympy as sp

expr1 = 1 - 5/(2*sp.E)
expr2 = 1/12 - (5*sp.sqrt(2))/96

result = sp.simplify(expr1 * expr2)

sp.print_latex(result)
