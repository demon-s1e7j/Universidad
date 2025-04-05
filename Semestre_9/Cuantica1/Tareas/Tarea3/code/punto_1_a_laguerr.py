import sympy as sp

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


print(laguerr_polynomi(7, 7))
