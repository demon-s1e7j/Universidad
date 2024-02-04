import numpy as np
import matplotlib.pyplot as plt

def BE(x,T):
    kb = 1.38e-23
    numerador = 1
    denominador = np.e**(x/(T*kb))+1
    return numerador/denominador

Elin = np.linspace(0,5,30);
Temp = np.linspace(0.1,200,5)

print(BE(Elin,100))
