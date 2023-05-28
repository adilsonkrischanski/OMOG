import matplotlib.pyplot as plt

from Curves.hermite import Hemite

class Plot():
    def __init__(self):
        self.curve = []

    def plot_hermite(self, pointers, Tvectors, Cvectors):

        p0 = pointers[0].get()
        p1 = pointers[1].get()
        v0 = Tvectors[0].get()
        v1 = Tvectors[1].get()
        c0 = Cvectors[0].get()
        c1 = Cvectors[1].get()

        h = Hemite(pointers, Tvectors, Cvectors)

        curve, tangent_points, curvature_points = h.get()


        plt.plot(curve[:, 0], curve[:, 1], label='Curva Hermite de Grau 5')
        plt.scatter([p0[0], p1[0]], [p0[1], p1[1]], c='red', label='Pontos de Controle')
        plt.quiver(tangent_points[:, 0], tangent_points[:, 1], [v0[0], v1[0]], [v0[1], v1[1]], color='blue', label='Vetores Tangentes')
        plt.quiver(curvature_points[:, 0], curvature_points[:, 1], [c0[0], c1[0]], [c0[1], c1[1]], color='green', label='Vetores de Curvatura')
        plt.xlabel('Eixo x')
        plt.ylabel('Eixo y')
        plt.title('Curva Hermite de Grau 5')
        plt.legend()
        plt.grid(True)
        plt.show()



