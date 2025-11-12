import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Configuración para etiquetas en español
plt.rcParams.update({'font.size': 12})

# Generar datos del espectro simulado
lambda_vals = np.linspace(4800, 5200, 1000)  # Longitudes de onda (Å)
continuum = np.ones_like(lambda_vals)  # Continuo normalizado a 1

# Crear una línea de absorción gaussiana (la misma que antes)
central_lambda = 5000  # Línea en 5000 Å
sigma = 10  # Ancho de la línea
depth = 0.6  # Profundidad máxima

absorption_line = continuum - depth * np.exp(-0.5 * ((lambda_vals - central_lambda) / sigma)**2)
observed_spectrum = absorption_line

# Configurar el método de los trapecios
num_trapezoids = 15  # Número de trapecios para la aproximación

# Encontrar la región donde la línea es significativa
absorption_mask = (continuum - observed_spectrum) > 0.01 * depth
absorption_range = lambda_vals[absorption_mask]

if len(absorption_range) > 0:
    lambda_start, lambda_end = absorption_range[0], absorption_range[-1]
    
    # Crear los intervalos para los trapecios
    trapezoid_lambdas = np.linspace(lambda_start, lambda_end, num_trapezoids + 1)
    
    # Calcular la aproximación por trapecios
    trapezoid_sum = 0
    trapezoids_data = []
    
    for i in range(num_trapezoids):
        lambda_i = trapezoid_lambdas[i]
        lambda_i1 = trapezoid_lambdas[i+1]
        
        # Encontrar los índices más cercanos en nuestros datos
        idx_i = np.argmin(np.abs(lambda_vals - lambda_i))
        idx_i1 = np.argmin(np.abs(lambda_vals - lambda_i1))
        
        # Alturas en los extremos del trapecio
        height_i = continuum[idx_i] - observed_spectrum[idx_i]
        height_i1 = continuum[idx_i1] - observed_spectrum[idx_i1]
        
        # Área del trapecio: (base * (altura1 + altura2)) / 2
        base = lambda_i1 - lambda_i
        area = base * (height_i + height_i1) / 2
        trapezoid_sum += area
        
        trapezoids_data.append({
            'lambda_start': lambda_i,
            'lambda_end': lambda_i1,
            'height_start': height_i,
            'height_end': height_i1,
            'base': base,
            'area': area,
            'y_start': observed_spectrum[idx_i],
            'y_end': observed_spectrum[idx_i1]
        })
    
    # Calcular el ancho equivalente exacto para comparación
    exact_equivalent_width = np.trapz(continuum - observed_spectrum, lambda_vals)

    # Crear la figura
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    
    # Graficar el espectro continuo y observado
    ax.plot(lambda_vals, continuum, 'k--', linewidth=2, label='Espectro Continuo (Fc)')
    ax.plot(lambda_vals, observed_spectrum, 'b-', linewidth=2, label='Espectro Observado (Fλ)')
    
    # Dibujar los trapecios
    for trap_data in trapezoids_data:
        # Definir los vértices del trapecio
        vertices = [
            (trap_data['lambda_start'], 1),  # Esquina superior izquierda
            (trap_data['lambda_end'], 1),    # Esquina superior derecha
            (trap_data['lambda_end'], 1 - trap_data['height_end']),  # Esquina inferior derecha
            (trap_data['lambda_start'], 1 - trap_data['height_start'])   # Esquina inferior izquierda
        ]
        
        trapezoid = Polygon(vertices, alpha=0.3, color='red', edgecolor='darkred', linewidth=1)
        ax.add_patch(trapezoid)
        
        # Dibujar las líneas que conectan los puntos en el espectro observado
        ax.plot([trap_data['lambda_start'], trap_data['lambda_end']], 
                [1 - trap_data['height_start'], 1 - trap_data['height_end']], 
                'darkred', linewidth=1.5, alpha=0.7)
    
    # Configuración del gráfico
    ax.set_xlabel('Longitud de Onda (Å)', fontsize=14)
    ax.set_ylabel('Flujo Normalizado', fontsize=14)
    ax.set_title(f'Cálculo del Ancho Equivalente por el Método de los Trapecios\n({num_trapezoids} trapecios)', fontsize=15)
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0.3, 1.1)
    
    # Líneas de referencia
    ax.axhline(y=1, color='gray', linestyle=':', alpha=0.7)
    ax.axvline(x=central_lambda, color='red', linestyle=':', alpha=0.7, 
               label=f'Línea en {central_lambda} Å')
    
    # Texto informativo
    # info_text = f'Suma de Trapecios = {trapezoid_sum:.2f} Å\nValor exacto = {exact_equivalent_width:.2f} Å\nError = {abs(trapezoid_sum - exact_equivalent_width):.4f} Å'
    # ax.text(0.02, 0.98, info_text, transform=ax.transAxes, verticalalignment='top',
    #         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8), fontsize=12)
    #
    # # Ecuación
    # ax.text(0.02, 0.15, r'$EW \approx \sum_{i=1}^{n} \frac{(F_c - F_{\lambda,i}) + (F_c - F_{\lambda,i+1})}{2} \cdot \Delta\lambda_i$', 
    #         transform=ax.transAxes, verticalalignment='top',
    #         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8), fontsize=12)
    
    plt.tight_layout()
    plt.savefig("../imgs/tp_img1.png")
    
    print(f"Ancho Equivalente exacto: {exact_equivalent_width:.4f} Å")
    print(f"Aproximación por trapecios ({num_trapezoids} trapecios): {trapezoid_sum:.4f} Å")
    print(f"Error: {abs(trapezoid_sum - exact_equivalent_width):.4f} Å")

else:
    print("No se detectó una línea de absorción significativa en el rango especificado")
