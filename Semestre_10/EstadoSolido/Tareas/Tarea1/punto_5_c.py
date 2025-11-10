import pandas as pd
import os
import numpy as np
from punto_5_a_b import index


os.system('clear')

data = pd.read_csv("./data_5.csv")
long_onda = 1.542

def LP(data):
    num = 1 + np.pow(np.cos(2*data), 2)
    den = np.pow(np.sin(data), 2) * np.cos(data)
    return num/den


data["theta"] = np.radians(data["2theta"] / 2)
data["LP"] = data["theta"].apply(LP)
data["|F|^2"] = data["Area"]/data["LP"]
print(data)
