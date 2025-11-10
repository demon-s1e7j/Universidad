import numpy as np
import matplotlib.pyplot as plt

omega0 = 1
gamma_values = [0.1, 1, 2]
Omega = np.linspace(0, 2, 1000)

plt.figure(figsize=(10, 6))
for gamma in gamma_values:
    A_norm = 1 / np.sqrt((1 - Omega**2)**2 + (2 * gamma * Omega)**2)
    plt.plot(Omega, A_norm, label=r'\gamma = {gamma}')
plt.xlabel('$\\Omega = \\omega / \\omega_0$')
plt.ylabel('Amplitud Normalizada $A / (\\mu k i_0 / \\kappa)$')
plt.title('Amplitud vs Frecuencia Relativa')
plt.legend()
plt.grid(True)
plt.savefig("punto_6_1.png")

plt.figure(figsize=(10, 6))
for gamma in gamma_values:
    phi = -np.arctan2(2 * gamma * Omega, 1 - Omega**2)
    plt.plot(Omega, phi, label=r'\gamma = {gamma}')
plt.xlabel('$\\Omega = \\omega / \\omega_0$')
plt.ylabel('Fase $\\phi$ (radianes)')
plt.title('Fase vs Frecuencia Relativa')
plt.legend()
plt.grid(True)
plt.savefig("punto_6_2.png")
