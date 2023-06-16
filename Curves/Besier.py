import numpy as np

from .Base import Pointer

class Besier():
    def __init__(self, pointers, amoutPointers) -> None:
        self.amoutPointers = amoutPointers
        self.p = pointers

        self.curve_x  = []
        self.curve_y = []

        self.bezier_curve()

    def bezier_curve(self):
        t = np.linspace(0, 1, self.amoutPointers)
        self.curve_x = ((1 - t)**3 * self.p[0].get_x() +
            3 * (1 - t)**2 * t * self.p[1].get_x() +
            3 * (1 - t) * t**2 * self.p[2].get_x() +
            t**3 * self.p[3].get_x())

        self.curve_y = ((1 - t)**3 * self.p[0].get_y()  +
            3 * (1 - t)**2 * t * self.p[1].get_y()  +
            3 * (1 - t) * t**2 * self.p[2].get_y()  +
            t**3 * self.p[3].get_y() )
        

    def rotation(self,pointerBaseX, pointerBaseY):
        for pointer in self.p:
            pointer.translate(pointerBaseX, pointerBaseY)
        self.bezier_curve()
        
        
    def get_curve_x(self):
        return self.curve_x
    
    def get_curve_y(self):
        return self.curve_y
    
    

