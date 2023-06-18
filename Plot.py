import matplotlib.pyplot as plt
from Curves.Base import Pointer

from Curves.hermite import Hermite
from Curves.Besier import Besier

class Plot():

    def plot_hermite(self, pointers, Tvectors, Cvectors):

        h = Hermite(pointers, Tvectors, Cvectors)
        x_hermite = h.get_x()
        y_hermite = h.get_y()

        plt.plot(x_hermite, y_hermite, label='Hermite (grau 5)')

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


        pointers_h, vectors_h,amoutPointers_h = hermite
        hermite = Hermite(pointers_h, vectors_h,amoutPointers_h)

        pointers_b, amoutPointers = besier
        

        P0 = pointers_h[0].get()
        P1 = pointers_h[1].get()
        T0 = vectors_h[0].get()
        T1 = vectors_h[1].get()

        Q0 = pointers_b[0].get()
        Q1 = pointers_b[1].get()
        Q2 = pointers_b[2].get()
        Q3 = pointers_b[3].get()

        Q0_adjusted = Pointer(P1[0],P1[1])
        Q1_adjusted = Pointer(Q1[0]+P1[0],Q1[1]+P1[1])
        Q2_adjusted = Pointer(Q2[0]+P1[0],Q2[1]+P1[1])
        Q3_adjusted = Pointer(Q3[0]+P1[0],Q3[1]+P1[1])

        besier =  Besier([Q0_adjusted, Q1_adjusted, Q2_adjusted, Q3_adjusted], amoutPointers)


        x_hermite = hermite.get_x()
        y_hermite = hermite.get_y()
        x_bezier = besier.get_curve_x()
        y_bezier = besier.get_curve_y()

      

        plt.plot(x_hermite, y_hermite, label='Curva de  hermite')
        plt.plot(x_bezier, y_bezier, label='Curva de Bézier')
        
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.title('C0 - hermite Besier')
        plt.grid(True)
        plt.show()


    def G1_hermite_besier(self, hermite, besier):

        pointers_h, vectors_h,amoutPointers_h = hermite
        hermite = Hermite(pointers_h, vectors_h,amoutPointers_h)

        pointers_b, amoutPointers = besier
        

        P0 = pointers_h[0].get()
        P1 = pointers_h[1].get()
        T0 = vectors_h[0].get()
        T1 = vectors_h[1].get()

        Q0 = pointers_b[0].get()
        Q1 = pointers_b[1].get()
        Q2 = pointers_b[2].get()
        Q3 = pointers_b[3].get()


        Q0_adjusted = Pointer(P1[0], P1[1])
        Q1_adjusted = Pointer(Q1[0] + (P1[0] - T0[0])+P1[0], Q1[1] + (P1[1] - T0[1])+P1[1])
        Q2_adjusted = Pointer(Q2[0] + (P1[0] - T1[0])+P1[0], Q2[1] + (P1[1] - T1[1])+P1[1])
        Q3_adjusted = Pointer(Q3[0]+P1[0], Q3[1]+P1[1])

        besier =  Besier([Q0_adjusted, Q1_adjusted, Q2_adjusted, Q3_adjusted], amoutPointers)


        x_hermite = hermite.get_x()
        y_hermite = hermite.get_y()
        x_bezier = besier.get_curve_x()
        y_bezier = besier.get_curve_y()

        plt.plot(x_hermite, y_hermite, label='Hermite (grau 5)')
        plt.plot(x_bezier, y_bezier, label='Bezier (grau 3)')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)
        plt.axis('equal')
        plt.title(' G1 entre Curvas Hermite e Bezier')

        plt.show()        

    def G2_hermite_besier(self, hermite, besier):
        pointers_h, vectors_h, amoutPointers_h = hermite
        hermite = Hermite(pointers_h, vectors_h,amoutPointers_h)

        pointers_b, amoutPointers = besier
        

        P0 = pointers_h[0].get()
        P1 = pointers_h[1].get()
        T0 = vectors_h[0].get()
        T1 = vectors_h[1].get()

        Q0 = pointers_b[0].get()
        Q1 = pointers_b[1].get()
        Q2 = pointers_b[2].get()
        Q3 = pointers_b[3].get()

        Q0_adjusted = Pointer(P1[0], P1[1])
        Q1_adjusted = Pointer(P1[0] + (T0[0] - P0[0]) / 3, P1[1] + (T0[1] - P0[1]) / 3)
        Q2_adjusted = Pointer(P1[0] + (T1[0] - P1[0]) / 3, P1[1] + (T1[1] - P1[1]) / 3)
        Q3_adjusted = Pointer(Q3[0] + P1[0], Q3[1] + P1[1])
       
        besier = Besier([Q0_adjusted, Q1_adjusted, Q2_adjusted, Q3_adjusted],amoutPointers)

        x_hermite = hermite.get_x()
        y_hermite = hermite.get_y()
        x_bezier = besier.get_curve_x()
        y_bezier = besier.get_curve_y()

        # Plotar as curvas conectadas
        plt.plot(x_hermite, y_hermite, label='Hermite (grau 5)')
        plt.plot(x_bezier, y_bezier, label='Bezier (grau 3)')


        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)
        plt.axis('equal')
        plt.title('G2 entre Curvas Hermite e Bezier')


        plt.show()

        



        


   



