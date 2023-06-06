from Curves.Base import Pointer, Vector
from Curves.hermite import Hemite

from Plot import Plot

if __name__=="__main__":

    p1 = Pointer(0,0)
    p2 = Pointer(3,3)
    tv0 = Vector(1,2)
    tv1 = Vector(2,1)
    cv0 = Vector(1,1)
    cv1 = Vector(1,2)
    p = Plot()
    # p.plot_hermite([p1,p2],[tv0,tv1],[cv0,cv1])


    p0_b = Pointer(0, 0)
    p1_b = Pointer(2, 4)
    p2_b = Pointer(6, 6)
    p3_b = Pointer(8, 2)
    # p.plot_Besier([p0,p1,p2,p3],100)

    p.C0_hermite_besier(([p1,p2],[tv0,tv1],[cv0,cv1]),([p0_b,p1_b,p2_b,p3_b],100))


    

