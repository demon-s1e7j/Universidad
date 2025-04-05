import numpy as np
import matplotlib.pyplot as plt
import random

np.random.seed(42)

# Parameters
frequency = 1  # Frequency of the sine wave (in Hz)
amplitude = 1  # Amplitude of the sine wave
duration = 10  # Duration of the signal (in seconds)
sampling_rate = 50  # Samples per second (sampling frequency)

# Time array
t = np.linspace(0, duration, duration * sampling_rate)

# Generate a sine wave signal
signal = amplitude * np.sin(2 * np.pi * frequency * t)

# Add some variation (random noise) to the signal
noise = np.random.normal(0, 0.2, len(t))  # Mean = 0, Std = 0.2
signal_with_noise = signal + noise

# Plot the signal
plt.figure(figsize=(10, 6))
plt.plot(t, signal_with_noise, 'ro', label="Signal")
plt.title("Time Series Data")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.savefig("Sampled10.png")
plt.show()
