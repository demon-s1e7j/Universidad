import numpy as np
from numpy import pi
from scipy.constants import h, m_e, k

T = 300

def density(mc, mv, Eg):
    def cal_N(m):
        return 2 * np.pow((2 * pi * m * k * T)/h**2, (3/2))
    N_c = cal_N(mc)
    N_v = cal_N(mv)
    ex = np.exp(- (Eg) / (k * T))
    return N_c * N_v * ex

E = 1.602176634e-19

n_i_squared = density(0.25 * m_e, 0.4 * m_e, E)
n_i = np.sqrt(n_i_squared)
print("Densidad intrínseca n_i =", n_i, "m^-3")

n = 1e18  # m^-3
p = n_i_squared / n
print("Densidad de huecos p =", p, "m^-3")
