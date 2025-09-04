import sympy
from sympy import symbols, exp, ln, sqrt, asin, diff
import numpy as np
import os


os.system("clear")

# Define el símbolo A y los valores numéricos
A = symbols('A')
A_val = 9.274
delta_A = 0.005

# Lista de funciones y sus descripciones en formato LaTeX
funciones = [
    (2 * A, "Z = 2A"),
    (A / 2, "Z = A/2"),
    ((A - 1) / (A + 1), "Z = \\frac{A-1}{A+1}"),
    (A**2 / (A - 2), "Z = \\frac{A^2}{A-2}"),
    (asin(1 / A), "Z = \\arcsin(\\frac{1}{A})"),
    (sqrt(A), "Z = \\sqrt{A}"),
    (ln(1 / sqrt(A)), "Z = \\ln(\\frac{1}{\\sqrt{A}})"),
    (exp(A**2), "Z = \\exp(A^2)"),
    (A + sqrt(1 / A), "Z = A + \\sqrt{\\frac{1}{A}}"),
    (10**A, "Z = 10^A")
]

# Encabezado del documento LaTeX
latex_output = "\\documentclass{article}\n\\usepackage{amsmath}\n\\begin{document}\n\n"

# Iterar sobre cada función
for func, desc in funciones:
    # Derivada simbólica
    dZ_dA = diff(func, A)

    # Valor numérico de la función y la derivada
    Z_val_num = float(func.subs(A, A_val))
    dZ_dA_val_num = float(dZ_dA.subs(A, A_val))

    # Incertidumbre
    delta_Z_num = abs(dZ_dA_val_num) * delta_A

    # Generar el código LaTeX para la sección
    latex_output += f"\\subsection*{{${desc}$}}\n"

    # Ecuación de la derivada
    latex_output += f"\\begin{{itemize}}\n"
    latex_output += f"\\item $\\frac{{dZ}}{{dA}} = {sympy.latex(dZ_dA)}$\n"

    # Ecuación de la incertidumbre (LÍNEA CORREGIDA)
    # Se utiliza \\left| ... \\right|_{} para agrupar correctamente la
    # expresión
    latex_output += f"\\item $\\delta Z = \\left|\\frac{{dZ}}{
        {dA}}\\right|\\_{{\\bar{{A}}}} \\delta A = |{
        dZ_dA_val_num:.5g}|(0.005) \\approx {
            delta_Z_num:.5g}$\n"

    # Resultado final
    # Se ajusta la precisión para los resultados con notación científica
    if 'exp' in str(func) or '10**A' in str(func):
        latex_output += f"\\item $Z \\approx {
            Z_val_num:.4g} \\pm {
            delta_Z_num:.4g}$\n"
    else:
        latex_output += f"\\item $Z \\approx {
            Z_val_num:.5f} \\pm {
            delta_Z_num:.5f}$\n"

    latex_output += f"\\end{{itemize}}\n"
    latex_output += f"\\vspace{{0.5cm}}\n\n"

# Cierre del documento LaTeX
latex_output += "\\end{document}"

# Imprimir el resultado
print(latex_output)
