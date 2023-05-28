import numpy as np
import matplotlib.pyplot as plt

class Hemite:
    def __init__(self, p0,p1,v0,v1) -> None:
        self.p0 = p0
        self.p1 = p1
        self.v0 = v0
        self.v1 = v1



    def hermite_curve(self):
        t = np.linspace(0, 1, 100)  # Parâmetro t variando de 0 a 1
        curve = np.zeros((len(t), 2))  # Matriz para armazenar os pontos da curva

        for i in range(len(t)):
            ti = t[i]
            t2 = ti * ti
            t3 = t2 * ti

            h00 = 2 * t3 - 3 * t2 + 1
            h10 = t3 - 2 * t2 + ti
            h01 = -2 * t3 + 3 * t2
            h11 = t3 - t2

            x = h00 * self.p0[0] + h10 * self.v0[0] + h01 * self.p1[0] + h11 * self.v1[0]
            y = h00 * self.p0[1] + h10 * self.v0[1] + h01 * self.p1[1] + h11 * self.v1[1]

            curve[i] = [x, y]

        return curve