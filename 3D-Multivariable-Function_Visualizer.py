import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x**2 - y**2

x = np.linspace(-4, 4, 30)
y = np.linspace(-4, 4, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(projection='3d')

surface = ax.plot_surface(
    X, Y, Z,
    cmap='coolwarm',
    alpha=0.9,
    edgecolor='none'
)

ax.set_title("Saddle Surface")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z = f(x, y)")

fig.colorbar(surface, shrink=0.5, aspect=10)
plt.show()
