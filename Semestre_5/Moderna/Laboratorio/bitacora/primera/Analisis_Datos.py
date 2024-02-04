import matplotlib.pyplot as plt 
import pandas as pd 

Datos = pd.read_csv('Datos_Exp1.csv')
Azul = Datos[Datos['Color'] == 'Azul']
Amarillo = Datos[Datos['Color'] == 'Amarillo']
Verde = Datos[Datos['Color'] == 'Verde']
Rojo = Datos[Datos['Color'] == 'Rojo']

plt.plot(Amarillo['Corriente'],Amarillo['Voltaje'],'yo')
plt.plot(Azul['Corriente'],Azul['Voltaje'],'bo')
plt.plot(Verde['Corriente'],Verde['Voltaje'],'go')
plt.plot(Rojo['Corriente'],Rojo['Voltaje'],'ro')
plt.legend(('Amarillo','Azul','Verde','Rojo'))
plt.title('Grafia de Corriente vs Voltaje')
plt.show()
