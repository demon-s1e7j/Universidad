import numpy as np
import matplotlib.pyplot as plt

N = 1e4
Tc = 1

T_ratios = np.linspace(0, 2, 500)

N0 = np.piecewise(T_ratios, 
                 [T_ratios < 1, T_ratios >= 1], 
                 [lambda x: N*(1 - x**3), 0])

Ne = np.piecewise(T_ratios, 
                 [T_ratios < 1, T_ratios >= 1], 
                 [lambda x: N*x**3, N])

plt.figure(figsize=(10, 6))
plt.plot(T_ratios, N0, 'b-', label='Estado base ($N_0$)')
plt.plot(T_ratios, Ne, 'r--', label='Estados excitados ($N_e$)')
plt.axvline(x=1, color='k', linestyle=':', label=r'$T_c$')

plt.xlabel(r'$T/T_c$', fontsize=12)
plt.ylabel('Numero de particulas', fontsize=12)
plt.title('Distribucion de Bosones en el Condensado', fontsize=14)
plt.legend()
plt.grid(alpha=0.3)
plt.xlim(0, 2)
plt.ylim(-0.05*N, 1.05*N)

plt.text(0.4, 0.9*N, r'$N_0 = N\left(1 - (T/T_c)^3\right)$', fontsize=12)
plt.text(1.2, 0.6*N, r'$N_e = N$', fontsize=12)
plt.text(0.4, 0.5*N, r'$N_e = N(T/T_c)^3$', fontsize=12)

plt.savefig('n_0_N.png', dpi=300, bbox_inches='tight')
