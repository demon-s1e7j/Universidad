import pandas as pd
import os
import numpy as np
from punto_5_a_b import index, degeneramiento
from punto_5_c import LP


os.system('clear')

data = pd.read_csv("./data_5.csv")
long_onda = 1.542


data["theta"] = np.radians(data["2theta"] / 2)
data["sin"] = np.sin(data["theta"])
data["LP"] = data["theta"].apply(LP)
data["|F|^2"] = data["Area"]/data["LP"]
data["2sin"] = 2 * data["sin"]
data["d"] = long_onda / data["2sin"]
data["sin^2"] = np.pow(data["theta"], 2)
data["s/s"] = (data["sin^2"] / data["sin^2"][0]).round().astype(int)
data.loc[6, "s/s"] = 8
data.loc[9, "s/s"] = 12
data["hkl"] = data["s/s"].apply(index)
data["sqrt(hkl)"] = data["hkl"].apply(lambda t: np.sqrt(t[0]**2 + t[1]**2 + t[2]**2))
data["a"] = data["d"]*data["sqrt(hkl)"]
data["m"] = data["hkl"].apply(degeneramiento)
data["Pm|F|^2"] = data["P"] * data["m"] * data["|F|^2"]
data["test"] = data["Area"]/data["Pm|F|^2"]


print(data)
print(f"Promedio: {data["a"].mean()}\nDivergencia: {data["a"].var()}")
