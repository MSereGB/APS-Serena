import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Parámetros de frecuencia
# -----------------------------
N = 4096  # resolución en frecuencia
w = np.linspace(-np.pi, np.pi, N)     # eje ω en rad/muestra
z = np.exp(1j * w)                    # puntos sobre el círculo unitario

# -----------------------------
# T(z) = 1/3 * (z^2 + z + 1) / z^3
# -----------------------------
H = (1/3) * (z**2 + z + 1) / (z**3)

# Módulo y fase
magH = np.abs(H)
phase_rad = np.angle(H)              # fase envuelta en radianes
phase_unwrapped = np.unwrap(phase_rad)
phase_deg = phase_unwrapped * 180/np.pi  # fase en grados

# -----------------------------
# Gráficos
# -----------------------------
xticks = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]
xtick_labels = [r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$']

plt.figure(figsize=(10, 6))

# Módulo
plt.subplot(2, 1, 1)
plt.plot(w, magH)
plt.title(r'Módulo de $T(e^{j\omega})$')
plt.ylabel(r'$|T(e^{j\omega})|$')
plt.xticks(xticks, xtick_labels)
plt.grid(True)

# Fase en grados
plt.subplot(2, 1, 2)
plt.plot(w, phase_deg)
plt.title(r'Fase de $T(e^{j\omega})$ (desenvuelta, en grados)')
plt.ylabel('Fase [°]')
plt.xlabel(r'$\omega$ [rad/muestra]')
plt.xticks(xticks, xtick_labels)
plt.grid(True)

plt.tight_layout()
plt.show()
