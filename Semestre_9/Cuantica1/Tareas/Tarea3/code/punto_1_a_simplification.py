import sympy as sp

r = sp.Symbol("r")
a0 = sp.Symbol("a0", positive=True)


def sqrt(n, ell):
    first_factor = (2/(n*a0))**3
    second_factor = sp.factorial(n - ell - 1)/(2*n*(sp.factorial(n + ell))**3)
    return sp.sqrt(first_factor * second_factor)


def sec_2(n, ell):
    first_factor = 2 * r
    second_factor = n * a0
    return (first_factor/second_factor)**ell


def expr(n, ell):
    return sp.simplify(sqrt(n, ell) * sec_2(n, ell))


expr = expr(4, 3)
sp.print_latex(expr)
