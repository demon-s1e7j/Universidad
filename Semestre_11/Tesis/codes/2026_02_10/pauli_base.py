import numpy as np
import itertools

I = np.array([[1, 0], [0, 1]])
X = np.array([[0, 1], [1, 0]])
Z = np.array([[1, 0], [0, -1]])
XZ = X @ Z

def producto_interno(A, B):
    A_dagger = np.conjugate(A).T
    return np.trace(A_dagger @ B)

matrices = {"I": I, "X": X, "Z": Z, "XZ": XZ}

def array_to_latex_pmatrix(arr):
    if arr.ndim > 2:
        raise ValueError("El array debe ser 1D o 2D")
    
    if arr.ndim == 1:
        arr = arr.reshape(1, -1)
    
    rows = []
    for row in arr:
        row_str = " & ".join(str(val) for val in row)
        rows.append(row_str)
    
    latex_body = " \\\\".join(rows)
    
    latex_str = f"\\begin{{pmatrix}}{latex_body}\\end{{pmatrix}}"
    
    return latex_str

def operation(nombre1: str, nombre2: str) -> str:
    A, B = matrices[nombre1], matrices[nombre2]
    op1 = array_to_latex_pmatrix(A)
    op2 = array_to_latex_pmatrix(B)
    op3 = array_to_latex_pmatrix((np.conjugate(A).T) @ B)
    result = producto_interno(A, B)
    return f"""\\left<{nombre1}, {nombre2}\\right> &= Tr\\left( {op1}^* {op2} \\right) = Tr\\left({op3}\\right)\\\\
            &= {result}\\\\"""


combinaciones = list(itertools.combinations(matrices.keys(), 2))
for (nombre1, nombre2) in combinaciones:
    if nombre1 == nombre2:
        continue
    print("%"*60)
    print(operation(nombre1, nombre2))
