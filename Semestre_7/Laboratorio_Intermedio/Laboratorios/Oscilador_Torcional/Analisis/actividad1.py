import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_csv("../Datos/actividad1.csv")

fuerza = datos["Masa"]*9.84*0.00001
err = 0.00984

lin_reg = np.polyfit(datos["Pos.Equi"] - 3, fuerza, 1)
lin_reg = np.poly1d(lin_reg)

fig = plt.figure()
ax = fig.add_subplot()
ax.errorbar(datos["Pos.Equi"] - 3, fuerza, xerr=0.01, yerr=err, label="Datos")
ax.plot(datos["Pos.Equi"] - 3, lin_reg(datos["Pos.Equi"] - 3), label="Regresión Lineal")
ax.legend()

plt.savefig("Graficas/actividad1.png")

print(lin_reg)
