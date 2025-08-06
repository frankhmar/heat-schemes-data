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

# Coefficients for tridiagonal matrix
A = np.zeros((nx-2, nx-2))
np.fill_diagonal(A, 1 + 2*r)
np.fill_diagonal(A[1:], -r)
np.fill_diagonal(A[:,1:], -r)

# Time stepping
for _ in range(nt):
    b = u[1:-1]
    u[1:-1] = np.linalg.solve(A, b)

# Plot
plt.plot(x, u, label="t = {:.3f}s".format(T))
plt.xlabel("x")
plt.ylabel("Temperature")
plt.title("BTCS Scheme (Implicit)")
plt.legend()
plt.grid()
plt.show()
