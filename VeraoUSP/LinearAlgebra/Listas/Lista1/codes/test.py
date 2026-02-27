import numpy as np

# Definir las matrices
A = np.array([
    [2, 3],
    [3, 4]
])

B = np.array([
    [-4, 3],
    [3, -2]
])

# Calcular el producto matricial
resultado = np.dot(A, B)

print("Matriz A:")
print(A)
print("\nMatriz B:")
print(B)
print("\nResultado A × B:")
print(resultado)
