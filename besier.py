import matplotlib.pyplot as plt
import numpy as np

def bezier_curve(p0, p1, p2, p3, num_points):
    t = np.linspace(0, 1, num_points)
    x = ((1 - t)**3 * p0[0] +
         3 * (1 - t)**2 * t * p1[0] +
         3 * (1 - t) * t**2 * p2[0] +
         t**3 * p3[0])

    y = ((1 - t)**3 * p0[1] +
         3 * (1 - t)**2 * t * p1[1] +
         3 * (1 - t) * t**2 * p2[1] +
         t**3 * p3[1])

    return x, y

# Pontos de controle da curva de Bézier
p0 = (0, 0)
p1 = (2, 4)
p2 = (6, 6)
p3 = (8, 2)

# Gera a curva de Bézier
num_points = 100
curve_x, curve_y = bezier_curve(p0, p1, p2, p3, num_points)

# Plota a curva de Bézier e os pontos de controle
plt.plot(curve_x, curve_y, label='Curva de Bézier')
plt.scatter([p0[0], p1[0], p2[0], p3[0]], [p0[1], p1[1], p2[1], p3[1]], c='red', label='Pontos de Controle')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Curva de Bézier de Grau 3')
plt.grid(True)
plt.show()
