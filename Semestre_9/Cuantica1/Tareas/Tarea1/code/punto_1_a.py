from sympy.solvers import solve
from sympy.physics.units import (
        speed_of_light,
        convert_to,
        meter,
        second,
        planck,
        kg,
        boltzmann_constant,
        joules,
        kelvin,
)
from sympy import (
        Symbol,
        exp,
        nsolve
)

x = Symbol('x')

eq = 5 * (1 - exp(-x)) - x

h = convert_to(planck, [meter, kg, second])

c = convert_to(speed_of_light, [meter, second])

k = convert_to(boltzmann_constant, [joules, kelvin])


if __name__ == "__main__":
    print(eq)

    # Resultados de x
    symbolic = solve(eq, x)
    # Los ultimos son las unidades de este objeto
    numeric = nsolve(eq, x, 10000) * (meter**2 * kg) / (second**2 * joules)
    print(f"Soluciones en Simbolos: {symbolic}")
    print(f"Aproximacion numerica: {numeric}")
    print(
        f"Aproximacion numerica a partir de los simbolos: {
            symbolic[1].evalf()}")

    # Despejar

    print("######## Constantes #################")
    print(c)
    print(h)
    print(k)
    print("####### Fin Constantes ##############")

    lambdaT = (h * c) / (numeric * k)
    print(f"Comprobacion del valor de lambda T {lambdaT}")
