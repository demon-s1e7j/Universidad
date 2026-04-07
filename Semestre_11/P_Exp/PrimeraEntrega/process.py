import pandas as pd

# Esto le dice a Pandas que no oculte ninguna columna al imprimir
pd.set_option('display.max_columns', None) 

data = pd.read_csv("./dielectricos_absolutamente_todo.csv")

# Si quieres ver todo sobre el Germanio:
print(data[data['formula_pretty'] == "Ge"])
