import sympy
from tabulate import tabulate
import os

os.system("clear")


x, mean, std_dev = sympy.symbols('x mu sigma')

gaussian = (1 / (std_dev * sympy.sqrt(2 * sympy.pi))) * \
    sympy.exp(-((x - mean)**2) / (2 * std_dev**2))


def replicate_table_sympy(mean_val=0, std_dev_val=1):
    integral_sym = sympy.integrate(gaussian, x)

    ranges = [1, 1.65, 2, 2.58, 3, 4, 5]
    table_data = []

    for r in ranges:
        x_min = mean_val - r * std_dev_val
        x_max = mean_val + r * std_dev_val

        result = (integral_sym.subs(x, x_max) - integral_sym.subs(x, x_min))
        result = result.subs({mean: mean_val, std_dev: std_dev_val})

        fraction_in_range = float(result)

        fraction_out_range = 1 - fraction_in_range

        range_str = f"\\pm {r} \\sigma"
        in_range_percent = f"{fraction_in_range * 100:.2f}%"
        out_range_percent = f"{fraction_out_range * 100:.2f}%"
        table_data.append([range_str, in_range_percent, out_range_percent])

    headers = [
        "Centrado en media",
        "Medidas dentro del rango",
        "Medidas fuera del rango"]

    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
    print(tabulate(table_data, headers=headers, tablefmt="latex"))


replicate_table_sympy()
