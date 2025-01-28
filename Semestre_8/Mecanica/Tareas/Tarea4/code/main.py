import math
import pandas as pd

# Definicion de los datos
data = {
    "Cuerpo Celeste": ["Sol", "Jupiter", "Tierra", "Marte", "Luna", "Estrella de neutrones"],
    "R (m)": [6.96e8, 6.99e7, 6.37e6, 3.39e6, 1.74e6, 1.0e4],
    "T (s)": [2.14e6, 3.58e4, 8.64e4, 8.87e4, 2.36e6, 1.0e-3],
    "g (m/s**2)": [274.0, 24.79, 9.81, 3.72, 1.62, 1.0e12]
}

df = pd.DataFrame(data)

# Calcular velocidad angular w y a_max
df["w (rad/s)"] = 2 * math.pi / df["T (s)"]
df["a_max (rad)"] = [math.atan((omega**2 * r) / g)
                     for omega, r, g in zip(df["w (rad/s)"], df["R (m)"], df["g (m/s**2)"])]

# Mostrar resultados
print(df.to_latex())
