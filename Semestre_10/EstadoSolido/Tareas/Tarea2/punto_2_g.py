import numpy as np
import matplotlib.pyplot as plt

# Parámetros
m1 = 1.0
m2 = 2.0
k1 = 1.0
k2 = 2.0
a = 1.0

# Vector de números de onda k en la primera zona de Brillouin [0, π/a]
k = np.linspace(0, np.pi/a, 500)

# Término común en la relación de dispersión
sin_term = np.sin(k*a/2)**2
discriminant = (m1 + m2)**2 * (k1 + k2)**2 - 16 * m1 * m2 * k1 * k2 * sin_term

# Frecuencias para los modos acústico y óptico
omega_ac = np.sqrt(((m1 + m2)*(k1 + k2) - np.sqrt(discriminant)) / (2 * m1 * m2))
omega_op = np.sqrt(((m1 + m2)*(k1 + k2) + np.sqrt(discriminant)) / (2 * m1 * m2))

# Valores destacados de los incisos (c) y (f)
# Inciso (c): velocidad del modo acústico para k pequeño
v_ac = a * np.sqrt(k1*k2 / ((m1 + m2)*(k1 + k2)))
omega_ac_small_k = v_ac * k  # Aproximación lineal para k pequeño

# Inciso (f): frecuencias en k = π/a
k_brillouin = np.pi/a
sin_brillouin = np.sin(k_brillouin*a/2)**2
discriminant_brillouin = (m1 + m2)**2 * (k1 + k2)**2 - 16 * m1 * m2 * k1 * k2 * sin_brillouin
omega_ac_brillouin = np.sqrt(((m1 + m2)*(k1 + k2) - np.sqrt(discriminant_brillouin)) / (2 * m1 * m2))
omega_op_brillouin = np.sqrt(((m1 + m2)*(k1 + k2) + np.sqrt(discriminant_brillouin)) / (2 * m1 * m2))

# Gráfica
plt.figure(figsize=(8, 6))
plt.plot(k, omega_ac, label='Modo acústico')
plt.plot(k, omega_op, label='Modo óptico')
plt.plot(k, omega_ac_small_k, '--', label='Aprox. lineal (acústico)')
plt.axhline(y=omega_ac_brillouin, color='r', linestyle=':', label=r'$\omega_{ac}(\pi/a)$')
plt.axhline(y=omega_op_brillouin, color='g', linestyle=':', label=r'$\omega_{op}(\pi/a)$')
plt.xlabel('Número de onda $k$')
plt.ylabel('Frecuencia $\omega$')
plt.title('Relación de dispersión para cadena diatómica')
plt.legend()
plt.grid(True)
plt.show()
