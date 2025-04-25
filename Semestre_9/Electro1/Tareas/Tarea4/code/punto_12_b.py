import numpy as np
import matplotlib.pyplot as plt

mu0 = 4 * np.pi * 1e-7

I = 1.0
R = 1.0
d = R


def Bz(z, I, R):
    term1 = mu0 * I * R**2 / (2.0 * (R**2 + (z - d/2.0)**2)**(3.0/2.0))
    term2 = mu0 * I * R**2 / (2.0 * (R**2 + (z + d/2.0)**2)**(3.0/2.0))
    return term1 + term2


z_vals = np.linspace(-2*R, 2*R, 300)

B_vals = [Bz(z, I, R) for z in z_vals]

plt.figure(figsize=(8, 5))
plt.plot(z_vals, B_vals)
plt.xlabel('z [m]')
plt.ylabel('B [T]')
plt.title('Campo magnetico a lo largo del eje de dos bobinas de Helmholtz (d = R)')
plt.grid(True)
plt.savefig("../img/punto_12_b.png")
