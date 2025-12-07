import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

J = -1.0
z = 6
kB = 1.0

T_N = abs(J) * z / (4 * kB)

def equation(x, T):
    if T == 0:
        return 0.5
    if T >= T_N:
        return 0.0
    return x - 0.5 * np.tanh(abs(J) * z * x / (2 * kB * T))

T_range = np.linspace(0.01, 2 * T_N, 200)
x_solutions = []

for T in T_range:
    if T >= T_N:
        x_solutions.append(0.0)
    else:
        initial_guesses = [0.1, 0.2, 0.3, 0.4, 0.5]
        found_solution = False
        
        for guess in initial_guesses:
            try:
                sol = fsolve(equation, guess, args=(T,), full_output=True)
                if sol[2] == 1 and sol[0][0] > 1e-6:
                    x_solutions.append(float(sol[0][0]))
                    found_solution = True
                    break
            except:
                continue
        
        if not found_solution:
            x_solutions.append(0.0)

x_solutions = np.array(x_solutions)

plt.figure(figsize=(10, 6))
plt.plot(T_range, x_solutions, 'b-', linewidth=3, label=r'$x = \frac{1}{2}\tanh\left(\frac{|J|z x}{2k_B T}\right)$')
plt.fill_between(T_range, 0, x_solutions, where=(T_range < T_N), 
                 alpha=0.2, color='blue', label='Fase ordenada ($T < T_N$)')
plt.fill_between(T_range, 0, 0.001, where=(T_range >= T_N), 
                 alpha=0.2, color='red', label='Fase paramagnetica ($T <= T_N$)')
plt.xlabel('Temperatura (T)', fontsize=14)
plt.ylabel(r'$x = |s_A| = |s_B|$', fontsize=14)
plt.title('Solucion de la ecuacion autoconsistente: $x = \\frac{1}{2}\\tanh\\left(\\frac{|J|z x}{2k_B T}\\right)$', 
          fontsize=16, fontweight='bold')
plt.xlim([0, 2 * T_N])
plt.ylim([-0.05, 0.55])
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right', fontsize=12)
plt.tight_layout()
plt.savefig("./punto_5c.png")
