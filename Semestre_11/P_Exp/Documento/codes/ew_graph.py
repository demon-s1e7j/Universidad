import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from matplotlib.patches import Polygon

# Configuración para etiquetas en español
plt.rcParams.update({'font.size': 12})

# Generar datos del espectro simulado
lambda_vals = np.linspace(4800, 5200, 1000)  # Longitudes de onda (Å)
continuum = np.ones_like(lambda_vals)  # Continuo normalizado a 1

# Crear una línea de absorción gaussiana
central_lambda = 5000  # Línea en 5000 Å
sigma = 10  # Ancho de la línea
depth = 0.6  # Profundidad máxima

absorption_line = continuum - depth * np.exp(-0.5 * ((lambda_vals - central_lambda) / sigma)**2)
observed_spectrum = absorption_line

# Calcular el ancho equivalente manualmente
equivalent_width = np.trapezoid(continuum - observed_spectrum, lambda_vals)

# Crear la figura
fig, ax = plt.subplots(1, 1, figsize=(12, 8))

# Graficar el espectro continuo y observado
ax.plot(lambda_vals, continuum, 'k--', linewidth=2, label='Espectro Continuo (Fc)')
ax.plot(lambda_vals, observed_spectrum, 'b-', linewidth=2, label='Espectro Observado (Fλ)')

# Resaltar la región del ancho equivalente
# Encontrar los puntos donde la línea es significativa
mask = (continuum - observed_spectrum) > 0.01 * depth
absorption_region = lambda_vals[mask]

if len(absorption_region) > 0:
    lambda_start, lambda_end = absorption_region[0], absorption_region[-1]
    
    # Crear el polígono del área integrada
    poly_vertices = []
    poly_vertices.extend(list(zip(lambda_vals[mask], observed_spectrum[mask])))
    poly_vertices.extend(list(zip(lambda_vals[mask][::-1], continuum[mask][::-1])))
    
    polygon = Polygon(poly_vertices, closed=True, alpha=0.3, color='red', 
                     label=f'Área integrada = EW')
    ax.add_patch(polygon)
    
    # Dibujar el rectángulo equivalente
    rect_height = 0.95
    rect_width = equivalent_width
    equivalent_rect = plt.Rectangle((central_lambda - rect_width/2, continuum[0] - rect_height), 
                                   rect_width, rect_height, 
                                   alpha=0.2, color='green', 
                                   label=f'Ancho Equivalente = {equivalent_width:.1f} Å')
    ax.add_patch(equivalent_rect)

# Configuración del gráfico
ax.set_xlabel('Longitud de Onda (Å)', fontsize=14)
ax.set_ylabel('Flujo Normalizado', fontsize=14)
ax.set_title('Representación del Area Equivalente en Espectroscopia', fontsize=16)

# Líneas de referencia
ax.axhline(y=1, color='gray', linestyle=':', alpha=0.7)
ax.axvline(x=central_lambda, color='red', linestyle=':', alpha=0.7, 
           label=f'Línea en {central_lambda} Å')

# Texto explicativo

ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 1.1)

plt.tight_layout()
plt.savefig("../Fig/ew_img1.png")

print(f"Ancho Equivalente calculado: {equivalent_width:.2f} Å")
