import sympy as sp
import os

os.system("clear")

s_theta_i, s_theta_t, delta_theta_i, delta_theta_t = sp.symbols(
    "theta_i theta_t delta_{theta_i} delta_{theta_t}")


def R(theta_i=s_theta_i, theta_t=s_theta_t):
    num = sp.Pow(sp.tan(theta_i - theta_t), 2)
    den = sp.Pow(sp.tan(theta_i + theta_t), 2)
    return num / den


def dR_dA(R_expr, theta=s_theta_i):
    return sp.diff(R_expr, theta)


def delta_R(R_expr, e_theta_i, e_theta_t):
    dR_dtheta_i = dR_dA(R_expr, theta=s_theta_i)
    dR_dtheta_t = dR_dA(R_expr, theta=s_theta_t)
    return sp.sqrt((dR_dtheta_i * e_theta_i)**2 + (dR_dtheta_t * e_theta_t)**2)


expresion = R()
error = delta_R(expresion, delta_theta_i, delta_theta_t)

print("-" * 60)
sp.print_latex(expresion)
print("\n")
sp.print_latex(error)
print("-" * 60)


def rad_of_grad(x): return (x * sp.pi) / 180


values = {
    s_theta_i: 45.0,
    delta_theta_i: 0.1,
    s_theta_t: 34.5,
    delta_theta_t: 0.2}
values = {key: rad_of_grad(value) for key, value in values.items()}

val_expresion = expresion.evalf(subs=values)
val_error = error.evalf(subs=values)

print(val_expresion)
print(val_error)
sp.print_latex(val_expresion)
sp.print_latex(val_error)
