import sympy as sp

x = sp.Symbol("x")
theta = sp.Symbol("theta")
phi = sp.Symbol("phi")


def derivate_n(n, expr, s=x):
    res = expr
    for _ in range(n):
        res = sp.diff(res, s)
    return sp.simplify(res)


def asociado(ell, m, s=x):
    first_factor = (-1)**m/(2**ell * sp.factorial(ell))
    second_factor = (1 - s**2)**(m/2)
    expr = (s**2 - 1)**ell
    tird_factor = derivate_n((ell + m), expr, s=s)
    return first_factor * second_factor * tird_factor


def Yellm(ell, m):
    first_factor_sqrt = (2*ell + 1)/(4*sp.pi)
    second_factor_sqrt = sp.factorial(ell - m)/sp.factorial(ell + m)
    first_factor = sp.sqrt(first_factor_sqrt * second_factor_sqrt)
    second_factor = asociado(ell, m).subs(x, sp.cos(theta))
    third_factor = sp.exp(sp.I * m * phi)
    return sp.simplify(first_factor * second_factor * third_factor)


sp.print_latex(Yellm(3, 3))
