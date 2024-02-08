import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_csv("../Datos/actividad2.csv")
print(datos)
x = datos["Numero de Cuadrantes"]
y = datos["Total"]/1000

lin_reg = np.polyfit(x,y,1)
lin_reg = np.poly1d(lin_reg)

fig = plt.figure()
ax = fig.add_subplot()
ax.errorbar(x, y, yerr=0.01, label="Datos")
ax.plot(x, lin_reg(x), label="Regresión Lineal")
ax.legend()

print(lin_reg)

plt.savefig("Graficas/actividad2.png")
