import numpy as np
from typing import Literal
import matplotlib.pyplot as plt

k = 8.617e-5
Eg = 1.12
N0 = 2.4e19

Nd = 1e17
Na = 1e17

T = np.linspace(100, 1000, 5000)

def var_don(N, T, type: Literal["p", "n"] = "n"):
    Ef = np.zeros_like(T)
    for i, temp in enumerate(T):
        A = (N/N0) * np.exp(Eg / (2 * k * temp))
        x = np.log(((1 if type == "n" else -1) * A + np.sqrt(A**2 + 4)) / 2)
        Ef[i] = k * temp * x
    return Ef

Ef_n = var_don(Nd, T)
Ef_p = var_don(Na, T, type="p")

plt.figure(figsize=(10, 6))
plt.plot(T, Ef_n, 'r-', label='Tipo n (Donantes)')
plt.plot(T, Ef_p, 'b-', label='Tipo p (Aceptores)')
plt.axhline(y=0, color='k', linestyle='--', label='Nivel intrínseco $E_i$')
plt.xlabel('Temperatura (K)')
plt.ylabel('$E_F - E_i$ (eV)')
plt.title('Variación del Potencial Químico con la Temperatura')
plt.legend()
plt.grid(True)
plt.savefig("punto3b.png")
