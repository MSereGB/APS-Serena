import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
N = 1000  # frecuencia de muestreo (Hz)
t = np.arange(0, 1, 1/N)  # vector de tiempo de 1 segundo
N = len(t)

# Señal original
f0 = 5  # frecuencia de la señal (Hz)
x = np.sin(2 * np.pi * f0 * t)

# SNR deseado en dB
SNR_dB = 10

# Calcular potencia de la señal
P_signal = np.mean(x**2)

# Calcular potencia del ruido necesaria
P_noise = P_signal / (10**(SNR_dB/10))

# Generar ruido blanco gaussiano
noise = np.random.normal(0, np.sqrt(P_noise), x.shape)

# Señal ruidosa
x_noisy = x + noise

# Graficar
plt.figure(figsize=(10,4))
plt.plot(t, x, label='Señal original')
plt.plot(t, x_noisy, label=f'Señal con SNR={SNR_dB} dB', alpha=0.7)
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.title('Señal con y sin ruido')
plt.show()