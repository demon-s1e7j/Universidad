import numpy as np
import matplotlib.pyplot as plt

def alpha(omega=7.3e-5, radio=6371000, g_0=9.8, theta=0):
    g_rad=g_0+(omega**2)*radio*(np.sin(theta))**2
    g_tan=omega**2*radio*(np.sin(theta)*np.cos(theta))
    return g_tan/g_rad

def latitud_colatitud(latitud):
    return np.deg2rad(90 - latitud)

pi = np.pi
espacio = np.linspace(-90, 90, 500)

plt.plot(espacio, alpha(theta=latitud_colatitud(espacio)))
plt.title("Relacion entre Alpha y la latitud")
plt.xlabel("Latitud")
plt.ylabel("Alpha")
plt.savefig("alpha_tierra.png")
