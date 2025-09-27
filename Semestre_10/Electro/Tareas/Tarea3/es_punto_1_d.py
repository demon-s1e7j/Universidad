import numpy as np
import matplotlib.pyplot as plt

a = 1.0
C = 1.0
M = 1.0
k = np.linspace(-np.pi/a, np.pi/a, 400)
omega = 2 * np.sqrt(C/M) * np.abs(np.sin(k*a/2))

plt.plot(k, omega, label=r'$\omega = 2\sqrt{C/M} |\sin(ka/2)|$')
plt.xlabel('k (either $k_x$ or $k_y$)')
plt.ylabel(r'$\omega$')
plt.title('Dispersión para $k_y=0$ o $k_x=0$')
plt.axvline(x=-np.pi/a, color='gray', linestyle='--')
plt.axvline(x=np.pi/a, color='gray', linestyle='--')
plt.axhline(y=2*np.sqrt(C/M), color='gray', linestyle='--')
plt.grid(True)
plt.legend()
plt.show()
