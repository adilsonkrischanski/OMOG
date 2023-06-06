import matplotlib.pyplot as plt

from Curves.hermite import Hemite
from Curves.Besier import Besier

class Plot():

    def plot_hermite(self, pointers, Tvectors, Cvectors):

        p0 = pointers[0].get()
        p1 = pointers[1].get()
        v0 = Tvectors[0].get()
        v1 = Tvectors[1].get()
        c0 = Cvectors[0].get()
        c1 = Cvectors[1].get()

        h = Hemite(pointers, Tvectors, Cvectors)
        

        curve, tangent_points, curvature_points = h.get()


        plt.plot(curve[:, 0], curve[:, 1], label='Curva')
        plt.scatter([p0[0], p1[0]], [p0[1], p1[1]], c='red', label='Pontos de Controle')
        plt.quiver(tangent_points[:, 0], tangent_points[:, 1], [v0[0], v1[0]], [v0[1], v1[1]], color='blue', label='Vetores Tangentes')
        plt.quiver(curvature_points[:, 0], curvature_points[:, 1], [c0[0], c1[0]], [c0[1], c1[1]], color='green', label='Vetores de Curvatura')
        plt.xlabel('Eixo x')
        plt.ylabel('Eixo y')
        plt.title('Curva Hermite Grau 5')
        plt.legend()
        plt.grid(True)
        plt.show()

    def plot_Besier(self, pointers, amoutPointers):
        b = Besier(pointers, amoutPointers)
        curve_x = b.get_curve_x()
        curve_y = b.get_curve_y()
        print(curve_x , curve_y )

        p0 = pointers[0].get()
        p1 = pointers[1].get()
        p2 = pointers[2].get()
        p3 = pointers[3].get()
    

        plt.plot(curve_x, curve_y, label='Curva de Bézier')
        plt.scatter([p0[0], p1[0], p2[0], p3[0]], [p0[1], p1[1], p2[1], p3[1]], c='red', label='Pontos de Controle')
        plt.legend()
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Curva de Bézier de Grau 3')
        plt.grid(True)
        plt.show()


    def C0_hermite_besier(self, hermite, besier):

        pointers_h, Tvectors, Cvectors = hermite
        hermite = Hemite(pointers_h, Tvectors, Cvectors)

        pointers_b, amoutPointers = besier
        besier =  Besier(pointers_b, amoutPointers)

        basepointer = hermite.last_poiter()
        besier.rotation(basepointer[0],basepointer[1])

        p0 = pointers_h[0].get()
        p1 = pointers_h[1].get()
        v0 = Tvectors[0].get()
        v1 = Tvectors[1].get()
        c0 = Cvectors[0].get()
        c1 = Cvectors[1].get()


        curve, tangent_points, curvature_points = hermite.get()


        plt.plot(curve[:, 0], curve[:, 1], label='Curva de  hermite')
        

        curve_x = besier.get_curve_x()
        curve_y = besier.get_curve_y()


        p0 = pointers_b[0].get()
        p1 = pointers_b[1].get()
        p2 = pointers_b[2].get()
        p3 = pointers_b[3].get()


        plt.plot(curve_x, curve_y, label='Curva de Bézier')
        
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.title('C0 - hermite Besier')
        plt.grid(True)
        plt.show()

        


   



