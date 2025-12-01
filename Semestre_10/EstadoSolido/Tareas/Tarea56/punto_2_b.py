import numpy as np
from scipy.constants import m_e

k_BT = 0.02585

N_c = 8.86e18
N_v = 8.86e18

m_e_s = 0.5 * m_e
m_h_s = 0.5 * m_e

E_g_silicio = 1.1

E_g_germanio = 0.75

def n_i(E_g):
    return np.sqrt(N_c * N_v) * np.exp( - E_g / (2 * k_BT))

n_i_silicio = n_i(E_g_silicio)
n_i_germanio = n_i(E_g_germanio)
if __name__=="__main__":
    print(n_i_silicio)
    print(n_i_germanio)
