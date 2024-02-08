import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_csv("../Datos/actividad3.csv")
print(datos)
x = datos["Corriente"]
y1 = datos["Theta (Primeros)"]
y2 = datos["Theta (Segundos)"]

lin_reg = np.polyfit(x,y1,1)
lin_reg = np.poly1d(lin_reg)

fig = plt.figure()
ax = fig.add_subplot()
ax.errorbar(x, y1, yerr=0.01, label="Datos")
ax.errorbar(-x, y2, yerr=0.01, label="Datos")
ax.plot(x, lin_reg(x), label="Regresión Lineal")
ax.legend()

print(lin_reg)

plt.savefig("Graficas/actividad3.png")
