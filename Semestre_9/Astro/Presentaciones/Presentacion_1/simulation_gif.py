import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Establecer la semilla para la aleatoriedad
np.random.seed(42)  # Esto garantiza que los resultados sean siempre los mismos

# Parámetros
frequency = 1  # Frecuencia de la onda seno (en Hz)
amplitude = 1  # Amplitud de la onda seno
duration = 10  # Duración de la señal (en segundos)
sampling_rate = 1000  # Frecuencia de muestreo (muestras por segundo)

# Tiempo inicial (con tamaño pequeño)
t_initial = np.linspace(0, duration, 10)  # Comenzamos con 10 muestras
signal_initial = amplitude * np.sin(2 * np.pi * frequency * t_initial)
noise_initial = np.random.normal(0, 0.2, len(t_initial))
signal_with_noise_initial = signal_initial + noise_initial

# Configuración de la figura y el eje
fig, ax = plt.subplots(figsize=(10, 6))
# Usar scatter en lugar de plot para dibujar círculos
scatter = ax.scatter([], [], label="Señal con Ruido", color='r')
ax.set_xlim(0, duration)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Datos Periódicos con Ruido (Tamaño de Muestra Incremental)")
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Amplitud")
ax.legend()
ax.grid(True)

# Función de actualización para la animación


def update(frame):
    # Aumentar el número de muestras por cada cuadro
    num_samples = 10 + frame
    t = np.linspace(0, duration, num_samples)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    noise = np.random.normal(0, 0.2, len(t))  # Ruido aleatorio
    signal_with_noise = signal + noise

    # Actualizar los datos para el scatter
    # Ajustamos las coordenadas de los puntos
    scatter.set_offsets(np.column_stack((t, signal_with_noise)))
    return scatter,


# Crear la animación
ani = FuncAnimation(fig, update, frames=range(1, 200), interval=50, blit=True)

# Guardar la animación como GIF
# Establecer los cuadros por segundo (fps) para el GIF
writer = PillowWriter(fps=15)
ani.save("signal_with_noise_circles.gif", writer=writer)

plt.show()
