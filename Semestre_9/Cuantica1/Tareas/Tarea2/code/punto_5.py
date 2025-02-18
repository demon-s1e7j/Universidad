from sympy import *

x = Symbol('x')
L = Symbol('L')

C = {1 : 100*L/512, 3: 25*L/512, 5: L/512}
A = 16/sqrt(63*L)

def calculate_integral(n: int):
    phi_n = sqrt(2/L) * sin((n * pi * x)/L)
    ecuation = C[n] * pow(x, 2) * pow(phi_n, 2)
    integral = Integral(ecuation, (x, 0, L))
    res_integrate = integrate(integral)
    return integral, simplify(res_integrate)

def return_value(integrales, result, complete_result):
    return f"""
  \\int_0^L x^2 C_1^2\\phi_1^2 dx &= {latex(integrales[1][0])}\\\\
  &={latex(integrales[1][1])}\\\\ 
  \\int_0^L x^2 C_2^2\\phi_3^2 dx &= {latex(integrales[3][0])}\\\\
  &= {latex(integrales[3][1])}\\\\
  \\int_0^L x^2 C_3^2\\phi_5^2 dx &= {latex(integrales[5][0])}\\\\
  &={latex(integrales[5][1])}\\\\
  \\left(\\int_0^L x^2 C_1^2\\phi_1^2 dx+ \\int_0^L C_2^2\\phi_3^2 dx+ \\int_0^L C_3^2\\phi_5^2 dx\\right) &= {latex(result)}\\\\
  \\left< x^2 \\right> &= \\int_0^L x^2 \\psi^2 dx\\\\
  \\left< x^2 \\right> &= A^2 \\left(\\int_0^L x^2 C_1^2\\phi_1^2 dx+ \\int_0^L C_2^2\\phi_3^2 dx+ \\int_0^L C_3^2\\phi_5^2 dx\\right)\\\\
  \\left< x^2 \\right> &={latex(complete_result)}\\\\
  &= {latex(complete_result.evalf())}
"""

if __name__ == "__main__":
    integrals = {index:calculate_integral(index) for index in [1, 3, 5]}
    result = simplify(sum([val[1] for val in integrals.values()]))
    complete_result = simplify(pow(A, 2) * result)
    print(return_value(integrals, result, complete_result))

    sigma_x = simplify(sqrt(complete_result - pow(L, 2)/4))
    print_latex(sigma_x)
