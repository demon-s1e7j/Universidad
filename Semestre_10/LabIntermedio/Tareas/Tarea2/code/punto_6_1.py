import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

os.system("clear")

data = pd.read_csv("./data_6_1.csv")
print(data)

x, y, yerr = data["Frecuency (Hz)"].to_numpy(
), data["Voltage (mV)"].to_numpy(), data["Error (mV)"].to_numpy()

plt.errorbar(
    x,
    y,
    yerr=yerr,
    fmt='o',
    ecolor='red',
    capsize=5,
    linestyle='none',
    markerfacecolor='blue',
    label="Voltage measurements"
)

plt.xlabel("Frequency (Hz)")
plt.ylabel("Voltage (mV)")
plt.title("Voltage vs Frequency with Error Bars")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("punto_6_1_a.png")

sum_x, sum_y, sum_x_sq, sum_xy = (np.sum(x) for x in [x, y, x**2, x * y])

delta = len(x) * np.sum(x**2) - (np.sum(x))**2

num_c = (sum_x_sq * sum_y) - (sum_x * sum_xy)
c = num_c / delta

num_m = (len(x) * sum_xy) - (sum_x * sum_y)
m = num_m / delta

alpha_CU = np.sqrt(1 / (len(x) - 2) * np.sum((y - m * x - c)**2))

alpha_c = alpha_CU * np.sqrt(sum_x_sq / delta)
alpha_m = alpha_CU * np.sqrt(len(x) / delta)

plt.figure(figsize=(10, 6))

plt.errorbar(
    x,
    y,
    yerr=yerr,
    fmt='o',
    ecolor='red',
    capsize=5,
    linestyle='none',
    markerfacecolor='blue',
    label="Datos de voltaje con error"
)

plt.plot(
    x,
    m * x + c,
    color='b',
    label=f'Ajuste lineal: y = {m:.2f}x + {c:.2f}'
)

plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Voltaje (mV)")
plt.title("Ajuste de Regresion Lineal No Ponderada")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("punto_6_1_b.png")
