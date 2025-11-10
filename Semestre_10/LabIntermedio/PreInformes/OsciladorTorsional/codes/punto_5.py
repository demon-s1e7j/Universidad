import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import sin, asin, symbols, pi, lambdify

# Configuración de matplotlib para mejor visualización
plt.rcParams['figure.figsize'] = [12, 8]
plt.rcParams['font.size'] = 12

# Definir símbolos
theta, phi, kappa, mu, B = symbols('theta phi kappa mu B')

# Tu desarrollo matemático
print("=== DESARROLLO MATEMÁTICO ===")
print("Partiendo de la ecuación de equilibrio:")
print("−κθ + μB sin(φ) = 0")
print("κθ = μB sin(φ)")
print("sin(φ) = (κθ)/(μB)")
print("φ = arcsin(κθ/μB)")

# Definir la relación φ = arcsin(κθ/μB)
phi_expr = asin((kappa * theta) / (mu * B))

print(f"\nExpresión simbólica: φ = {phi_expr}")

# Parámetros físicos típicos (puedes ajustarlos)
kappa_val = 0.058  # N·m/rad
mu_val = 13.5      # A·m²
B_val = 0.1        # T (valor típico del campo magnético)

# Sustituir valores numéricos
phi_num = phi_expr.subs({kappa: kappa_val, mu: mu_val, B: B_val})
print(f"\nCon valores numéricos: φ = {phi_num}")

# Convertir a función numérica para graficar
phi_func = lambdify(theta, phi_num, 'numpy')

# Crear array de valores de theta (en radianes)
theta_range = np.linspace(-kappa_val/(mu_val*B_val) + 0.01, 
                          kappa_val/(mu_val*B_val) - 0.01, 500)

# Calcular phi correspondiente
phi_range = phi_func(theta_range)

# Crear figura con subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

# Gráfico 1: φ vs θ
ax1.plot(theta_range, phi_range, 'b-', linewidth=2, label='φ = arcsin(κθ/μB)')
ax1.set_xlabel('Ángulo θ (rad)')
ax1.set_ylabel('Ángulo φ (rad)')
ax1.set_title('Relación entre φ y θ')
ax1.grid(True, alpha=0.3)
ax1.legend()

# Gráfico 2: sin(φ) vs θ
ax2.plot(theta_range, np.sin(phi_range), 'r-', linewidth=2, label='sin(φ)')
ax2.plot(theta_range, (kappa_val/(mu_val*B_val)) * theta_range, 'g--', 
         linewidth=2, label='(κ/μB)θ')
ax2.set_xlabel('Ángulo θ (rad)')
ax2.set_ylabel('sin(φ)')
ax2.set_title('Verificación: sin(φ) = (κ/μB)θ')
ax2.grid(True, alpha=0.3)
ax2.legend()

# Gráfico 3: En grados para mejor interpretación
theta_deg = np.degrees(theta_range)
phi_deg = np.degrees(phi_range)

ax3.plot(theta_deg, phi_deg, 'purple', linewidth=2, label='φ vs θ')
ax3.set_xlabel('Ángulo θ (grados)')
ax3.set_ylabel('Ángulo φ (grados)')
ax3.set_title('Relación φ vs θ en grados')
ax3.grid(True, alpha=0.3)
ax3.legend()

plt.tight_layout()
plt.show()

# Análisis adicional
print("\n=== ANÁLISIS ADICIONAL ===")
print(f"Rango válido de θ: ±{kappa_val/(mu_val*B_val):.3f} rad")
print(f"Esto equivale a: ±{np.degrees(kappa_val/(mu_val*B_val)):.1f}°")

# Verificar algunos puntos específicos
test_thetas = [0, 0.1, 0.2, 0.3]
print("\nValores específicos:")
print("θ (rad)\t\tφ (rad)\t\tφ (grados)\t¿sin(φ) = (κ/μB)θ?")
for theta_test in test_thetas:
    if abs(theta_test) < kappa_val/(mu_val*B_val):
        phi_test = phi_func(theta_test)
        sin_phi = np.sin(phi_test)
        target = (kappa_val/(mu_val*B_val)) * theta_test
        check = "✓" if abs(sin_phi - target) < 1e-10 else "✗"
        print(f"{theta_test:.3f}\t\t{phi_test:.3f}\t\t{np.degrees(phi_test):.1f}\t\t{check}")
    else:
        print(f"{theta_test:.3f}\t\tFuera del dominio")

# Diagrama esquemático de la relación geométrica
fig2, ax4 = plt.subplots(1, 1, figsize=(8, 8))
ax4.set_xlim(-1.5, 1.5)
ax4.set_ylim(-1.5, 1.5)
ax4.set_aspect('equal')

# Dibujar ejes
ax4.axhline(y=0, color='k', linestyle='-', alpha=0.3)
ax4.axvline(x=0, color='k', linestyle='-', alpha=0.3)

# Campo magnético B (dirección y)
ax4.arrow(0, -1, 0, 2, head_width=0.05, head_length=0.1, fc='red', ec='red', label='B')
ax4.text(0.1, 1.2, 'B (campo magnético)', color='red')

# Momento magnético μ en diferentes ángulos
angles = [0, 30, 60]  # en grados
colors = ['blue', 'green', 'orange']

for i, angle_deg in enumerate(angles):
    angle_rad = np.radians(angle_deg)
    x_end = np.cos(angle_rad)
    y_end = np.sin(angle_rad)
    
    ax4.arrow(0, 0, x_end, y_end, head_width=0.05, head_length=0.1, 
              fc=colors[i], ec=colors[i], 
              label=f'μ (θ={angle_deg}°)')
    
    # Calcular φ correspondiente
    phi_calc = np.degrees(phi_func(angle_rad))
    ax4.text(x_end + 0.1, y_end + 0.1, f'φ={phi_calc:.1f}°', color=colors[i])

ax4.set_title('Diagrama: Relación geométrica entre B, μ y θ')
ax4.legend()
ax4.grid(True, alpha=0.3)
plt.show()
