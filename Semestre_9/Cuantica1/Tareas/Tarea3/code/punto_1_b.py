import sympy as sp

r = sp.Symbol("r")
a0 = sp.Symbol("a0", positive=True)
x = sp.Symbol("x")


def derivate_n(n, expr, s=x):
    res = expr
    for _ in range(n):
        res = sp.diff(res, s)
    return sp.simplify(res)


def laguerr_polynomi(p, q):
    factor = (-1)**p
    expr = sp.exp(-x) * x**q
    prim_derivate = derivate_n(q, expr)
    sec_derivate = derivate_n(p, sp.exp(x) * prim_derivate)

    return factor * sec_derivate


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


expr = expr(4, 3) * sp.exp(- (r)/(4*a0)) * laguerr_polynomi(7, 7)
mod_2 = expr * sp.conjugate(expr)
integral = sp.integrate(mod_2 * r**3, (r, 0, sp.oo))
sp.print_latex(sp.simplify(integral))
