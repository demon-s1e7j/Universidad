from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
import numpy as np

getcontext().prec = 50

class Point():
    def __init__(self, k_x, k_y, k_z):
        self.k_x = Decimal(k_x)
        self.k_y = Decimal(k_y)
        self.k_z = Decimal(k_z)

    def __pow__(self, p):
        return Point(self.k_x**p, self.k_y**p, self.k_z**p)

    def __add__(self, other):
        if not isinstance(other, Point):
            raise TypeError(f"unsupported operand type(s) for +:'Point' and '{other.__class__.__name__}'")
        return Point(self.k_x + other.k_x, self.k_y + other.k_y, self.k_z + other.k_z)

    def __sub__(self, other):
        if not isinstance(other, Point):
            raise TypeError(f"unsupported operand type(s) for -:'Point' and '{other.__class__.__name__}'")
        return Point(self.k_x - other.k_x, self.k_y - other.k_y, self.k_z - other.k_z)

    def _sum(self) -> Decimal:
        return self.k_x + self.k_y + self.k_z

    def distance(self, other) -> float:
        return (((self - other)**2)._sum()).sqrt()

# Puntos
Gamma = Point(0, 0, 0)
Xp = Point(1, 0, 0)
Wp = Point(1, 0.5, 0)
Lp = Point(0.5, 0.5, 0.5)
Kp = Point((3/4), (3/4), 0)

# Distancias
dXG = Xp.distance(Gamma)
dGW = Gamma.distance(Wp)
dLG = Lp.distance(Gamma)
dGK = Gamma.distance(Kp)

# Posiciones Acumuladas
x_X = 0
x_G1 = x_X + dXG
x_W = x_G1 + dGW
x_L = 0
x_G2 = x_L + dLG
x_K = x_G2 + dGK

### CONVIRTIENDO A FLOAT
x_X_f = float(x_X)
x_G1_f = float(x_G1)
x_W_f = float(x_W)
x_L_f = float(x_L)
x_G2_f = float(x_G2)
x_K_f = float(x_K)

## Energias

E_s = 0
Beta = 0

def energy_GX(mu, gamma = 1.0):
    return E_s - Beta - 4 * gamma * (1 + 2 * np.cos(mu * np.pi))

def energy_GL(mu, gamma = 1.0):
    return E_s - Beta - 12 * gamma * (np.pow(np.cos(mu * np.pi), 2))

def energy_GK(mu, gamma = 1.0):
    return E_s - Beta - 4 * gamma * (np.pow(np.cos(mu * np.pi), 2) + 2 * np.cos(mu * np.pi))

def energy_GW(mu, gamma = 1.0):
    cos_mu_pi = np.cos(mu * np.pi)
    cos_mu_pi_half = np.cos(mu * np.pi / 2)
    return E_s - Beta - 4 * gamma * (cos_mu_pi + cos_mu_pi_half + cos_mu_pi * cos_mu_pi_half)

N_points = 200

mu_XG = np.linspace(1, 0, N_points)
x_XG = np.linspace(x_X_f, x_G1_f, N_points)

mu_GW = np.linspace(0, 1, N_points)
x_GW = np.linspace(x_G1_f, x_W_f, N_points)

mu_LG = np.linspace(0.5, 0, N_points)
x_LG = np.linspace(x_L_f, x_G2_f, N_points)

mu_GK = np.linspace(0, 3/4, N_points)
x_GK = np.linspace(x_G2_f, x_K_f, N_points)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

colores = [
    "#FF0000",  # Rojo Puro (Clásico y potente)
    "#00FF00",  # Verde Lima Eléctrico (Saturación máxima)
    "#0000FF",  # Azul Eléctrico/Cian (Brillante e intenso)
    "#FFFF00",  # Amarillo Neón (Máximo brillo)
    "#FF00FF",  # Magenta Brillante (Púrpura intenso)
    "#FFA500"   # Naranja Brillante (Un naranja muy vivo)
]

for i, gamma in enumerate([2.0, 1.0, 0.5, -0.5, -1.0, -2.0]):
    e_XG = energy_GX(mu_XG, gamma=gamma)
    e_GW = energy_GW(mu_GW, gamma=gamma)
    e_LG = energy_GL(mu_LG, gamma=gamma)
    e_GK = energy_GK(mu_GK, gamma=gamma)
    
    label = label_gamma = fr"$\gamma = {gamma}$"

    ax1.plot(x_XG, e_XG, color=colores[i], label=label)
    ax1.plot(x_GW, e_GW, color=colores[i])


    ax2.plot(x_LG, e_LG, color=colores[i], label=label)
    ax2.plot(x_GK, e_GK, color=colores[i]) 



ax1.set_ylabel(r'$\epsilon(k)$', fontsize=14)
ax1.set_xticks([x_X_f, x_G1_f, x_W_f])
ax1.set_xticklabels(['X', r'$\Gamma$', 'W'], fontsize=12)
ax1.axvline(x_G1_f, color='gray', linestyle='--')
ax1.axvline(x_W_f, color='gray', linestyle='--')
ax1.set_xlim(x_X_f, x_W_f)
ax1.grid(axis='y', linestyle=':', alpha=0.7)
ax1.legend()

ax2.set_ylabel(r'$\epsilon(k)$', fontsize=14)
ax2.set_xticks([x_L_f, x_G2_f, x_K_f])
ax2.set_xticklabels(['L', r'$\Gamma$', 'K'], fontsize=12)
ax2.axvline(x_G2_f, color='gray', linestyle='--')
ax2.axvline(x_K_f, color='gray', linestyle='--')
ax2.set_xlim(x_L_f, x_K_f)
ax2.grid(axis='y', linestyle=':', alpha=0.7)
ax2.legend()

plt.tight_layout()
plt.savefig("./punto_2_f.png")
