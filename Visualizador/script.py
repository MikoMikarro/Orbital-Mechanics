import numpy as np
import matplotlib.pyplot as plt

ancho = 30
alto = 30

def plot_ellipse(a, e, sigma = 0, init = 0, final = 360, tipo = '-'):
    x_values = []
    y_values = []

    for i in range(final-init):
        angle = np.pi * i / 180.0
        r = float(a) * (1 - float(e)**2 ) / (1 + float(e) * np.cos(angle))

        x = r * np.cos(angle + (np.pi * sigma / 180.0))
        y = r * np.sin(angle + (np.pi * sigma / 180.0))
        x_values.append(x)
        y_values.append(y)

    plt.plot(x_values, y_values, tipo)

circle1 = plt.Circle((0, 0), 1, color='r')

fig, ax = plt.subplots()

ax.add_artist(circle1)
ax.plot()
plot_ellipse(3,2)
plot_ellipse(10, 0.2)
plt.axis([-ancho/2,  ancho/ 2, -alto/2, alto/2])
plt.show()
