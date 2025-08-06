import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1.0
T = 0.1
alpha = 1.172e-5
nx = 20
nt = 1000
dx = L / (nx - 1)
dt = T / nt
r = alpha * dt / dx**2

# Initial condition
x = np.linspace(0, L, nx)
u = np.sin(np.pi * x)

# FTCS Scheme
for _ in range(nt):
    u[1:-1] = u[1:-1] + r * (u[2:] - 2*u[1:-1] + u[:-2])

# Plot
plt.plot(x, u, label="t = {:.3f}s".format(T))
plt.xlabel("x")
plt.ylabel("Temperature")
plt.title("FTCS Scheme (Explicit)")
plt.legend()
plt.grid()
plt.show()
