from sympy import symbols, Eq, Poly, print_latex

a = symbols('a')

ecuacion = Eq(1/a**4 + 1/(a + 1)**4, 2)

numerador = (ecuacion.lhs - ecuacion.rhs).together().as_numer_denom()[0]

polinomio = Poly(numerador, a)

raices = polinomio.nroots()

for raiz in raices:
    print_latex(raiz)
