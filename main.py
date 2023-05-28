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
    p.plot_hermite([p1,p2],[tv0,tv1],[cv0,cv1])