from Curves.Base import Pointer, Vector
from Curves.hermite import Hermite

from Plot import Plot

if __name__=="__main__":

    p1 = Pointer(0,0)
    p2 = Pointer(2, 4)
    v0 = Vector(1, 1)
    v1 = Vector(3, 2)
    p = Plot()
    p.plot_hermite([p1,p2],[v0,v1],100)


    p0_b = Pointer(3, 2)
    p1_b = Pointer(4, 1)
    p2_b = Pointer(6, 3)
    p3_b = Pointer(7, 0)
    p.plot_Besier([p0_b,p1_b,p2_b,p3_b],100)


    p.C0_hermite_besier(([p1,p2],[v0,v1],100),([p0_b,p1_b,p2_b,p3_b],100))

    p.G1_hermite_besier(([p1,p2],[v0,v1],100),([p0_b,p1_b,p2_b,p3_b],100))

    p.G2_hermite_besier(([p1,p2],[v0,v1],100),([p0_b,p1_b,p2_b,p3_b],100))

    

