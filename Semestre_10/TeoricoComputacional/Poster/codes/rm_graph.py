import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Configuración para etiquetas en español
plt.rcParams.update({'font.size': 12})

# Generar datos del espectro simulado
lambda_vals = np.linspace(4800, 5200, 100)  # Longitudes de onda (Å)
continuum = np.ones_like(lambda_vals)  # Continuo normalizado a 1

# Crear una línea de absorción gaussiana (la misma que antes)
central_lambda = 5000  # Línea en 5000 Å
sigma = 10  # Ancho de la línea
depth = 0.6  # Profundidad máxima

absorption_line = continuum - depth * np.exp(-0.5 * ((lambda_vals - central_lambda) / sigma)**2)
observed_spectrum = absorption_line

# Configurar la suma de Riemann
num_rectangles = 20  # Número de rectángulos para la aproximación

# Encontrar la región donde la línea es significativa
absorption_mask = (continuum - observed_spectrum) > 0.01 * depth
absorption_range = lambda_vals[absorption_mask]

if len(absorption_range) > 0:
    lambda_start, lambda_end = absorption_range[0], absorption_range[-1]
    
    # Crear los intervalos para los rectángulos de Riemann
    riemann_lambdas = np.linspace(lambda_start, lambda_end, num_rectangles + 1)
    rectangle_width = riemann_lambdas[1] - riemann_lambdas[0]
    
    # Calcular la suma de Riemann (aproximación del ancho equivalente)
    riemann_sum = 0
    rectangles_data = []
    
    for i in range(num_rectangles):
        # Punto medio del intervalo para evaluar la función
        mid_point = (riemann_lambdas[i] + riemann_lambdas[i+1]) / 2
        # Encontrar el índice más cercano en nuestros datos
        idx = np.argmin(np.abs(lambda_vals - mid_point))
        
        # Altura del rectángulo = diferencia entre continuum y espectro observado
        height = continuum[idx] - observed_spectrum[idx]
        
        # Área del rectángulo
        area = rectangle_width * height
        riemann_sum += area
        
        rectangles_data.append({
            'lambda_start': riemann_lambdas[i],
            'width': rectangle_width,
            'height': height,
            'area': area,
            'y_position': observed_spectrum[idx]  # Posición Y desde donde empieza el rectángulo
        })
    
    # Calcular el ancho equivalente exacto para comparación
    exact_equivalent_width = np.trapz(continuum - observed_spectrum, lambda_vals)

    # Crear la figura
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    
    # Graficar el espectro continuo y observado
    ax.plot(lambda_vals, continuum, 'k--', linewidth=2, label='Espectro Continuo (Fc)')
    ax.plot(lambda_vals, observed_spectrum, 'b-', linewidth=2, label='Espectro Observado (Fλ)')
    
    # Dibujar los rectángulos de Riemann DESDE EL CONTINUUM HACIA ABAJO
    for rect_data in rectangles_data:
        # El rectángulo comienza en el continuum (y=1) y tiene altura = (Fc - Fλ)
        rect = Rectangle((rect_data['lambda_start'], 1 - rect_data['height']), 
                        rect_data['width'], rect_data['height'],
                        alpha=0.3, color='red', edgecolor='darkred', linewidth=1)
        ax.add_patch(rect)
        
        # Opcional: agregar una línea delgada para marcar el borde superior de cada rectángulo
        ax.axhline(y=1 - rect_data['height'], xmin=0, xmax=1, color='darkred', 
                  linestyle='-', alpha=0.5, linewidth=0.5)
    
    # Configuración del gráfico
    ax.set_xlabel('Longitud de Onda (Å)', fontsize=14)
    ax.set_ylabel('Flujo Normalizado', fontsize=14)
    ax.set_title(f'Cálculo del Ancho Equivalente por Sumas de Riemann\n({num_rectangles} rectángulos)', fontsize=15)
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0.3, 1.1)
    
    # Líneas de referencia
    ax.axhline(y=1, color='gray', linestyle=':', alpha=0.7)
    ax.axvline(x=central_lambda, color='red', linestyle=':', alpha=0.7, 
               label=f'Línea en {central_lambda} Å')
    
    # Texto informativo
    # info_text = f'Suma de Riemann = {riemann_sum:.2f} Å\nValor exacto = {exact_equivalent_width:.2f} Å\nError = {abs(riemann_sum - exact_equivalent_width):.3f} Å'
    # ax.text(0.02, 0.98, info_text, transform=ax.transAxes, verticalalignment='top',
    #         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8), fontsize=12)
    #
    # # Ecuación
    # ax.text(0.02, 0.15, r'$EW = \sum_{i=1}^{n} (F_c - F_{\lambda,i}) \cdot \Delta\lambda_i$', 
    #         transform=ax.transAxes, verticalalignment='top',
    #         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8), fontsize=14)
    
    plt.tight_layout()
    plt.savefig("../imgs/rm_img1.png")
    
    print(f"Ancho Equivalente exacto: {exact_equivalent_width:.4f} Å")
    print(f"Suma de Riemann ({num_rectangles} rectángulos): {riemann_sum:.4f} Å")
    print(f"Error: {abs(riemann_sum - exact_equivalent_width):.4f} Å")

else:
    print("No se detectó una línea de absorción significativa en el rango especificado")
