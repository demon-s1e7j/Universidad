import numpy as np
import matplotlib.pyplot as plt
from scipy.special import zeta

# Constantes
zeta3 = zeta(3)
zeta4 = zeta(4)
zeta2 = np.pi**2 / 6

Nk = 1

def cv_low_T(T_ratio):
    return 12 * (zeta4 / zeta3) * Nk * T_ratio**3

def cv_high_T(T_ratio):
    term1 = 12 * (zeta4 / zeta3) * T_ratio**3
    term2 = 9 * (zeta3**2 / (zeta2 * zeta3)) * T_ratio**3
    return term1 - term2

def cv_free_boson(T_ratio):
    return 12 * (zeta4 / zeta3) * Nk * T_ratio**3 * 0.8

T_ratios_low = np.linspace(0, 1, 100)
T_ratios_high = np.linspace(1, 2, 100)

cv_low = cv_low_T(T_ratios_low)
cv_high = cv_high_T(T_ratios_high)
cv_free = cv_free_boson(np.concatenate([T_ratios_low, T_ratios_high]))

plt.figure(figsize=(10, 6))

plt.plot(T_ratios_low, cv_low, 'b-', label=r'$T \leq T_c$ (Potencial Armonico)')
plt.plot(T_ratios_high, cv_high, 'r-', label=r'$T \geq T_c$ (Potencial Armonico)')

plt.plot(np.concatenate([T_ratios_low, T_ratios_high]), cv_free, 'g:', label='Gas de Bosones Libres')

plt.plot([1, 1], [cv_low[-1], cv_high[0]], 'ko', markersize=8, markerfacecolor='none')
plt.vlines(1, cv_high[0], cv_low[-1], colors='k', linestyles='dashed')

plt.xlabel(r'$T/T_c$', fontsize=12)
plt.ylabel(r'$C_V / Nk$', fontsize=12)
plt.title('Calor Especifico a Volumen Constante', fontsize=14)
plt.legend()
plt.grid(alpha=0.3)
plt.xlim(0, 2)
plt.ylim(0, 15)

plt.savefig('calor_especifico.png', dpi=300, bbox_inches='tight')
