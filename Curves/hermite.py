
import numpy as np
import matplotlib.pyplot as plt


from .Base import Pointer
from .Base import Vector


class Hermite():
    def __init__(self, pointers, vectors, n_points):

        self.p = pointers
        self.v = vectors
        self.num_points = n_points
   
        self.curve_x = []
        self.curve_y = []

        self.hermite_curve()

        
    def hermite_curve(self):
        t = np.linspace(0, 1, self.num_points)
        t2 = t * t
        t3 = t2 * t
        h00 = 2*t3 - 3*t2 + 1
        h01 = -2*t3 + 3*t2
        h02 = t3 - 2*t2 + t
        h03 = t3 - t2
        h04 = -2*t3 + 3*t2 - t
        h05 = t3 - t2

        self.curve_x = h00 * self.p[0].get_x() + h01 * self.p[1].get_x() + h02 * self.v[0].get_x() + h03 * self.v[1].get_x() + h04 * self.v[0].get_x() + h05 * self.v[1].get_x()

        self.curve_y = h00 * self.p[0].get_y() + h01 * self.p[1].get_y() + h02 * self.v[0].get_y() + h03 * self.v[1].get_y() + h04 * self.v[0].get_y() + h05 * self.v[1].get_y() 

    
    def get_pointers(self):
        return self.p

    def get(self):
        return self.curve_x, self.curve_y
    
    def get_x(self):
        return self.curve_x

    def get_y(self):
        return self.curve_y
    
    def last_pointer(self):
        return self.curve_x[len(self.curve_x)-1], self.curve_y[len(self.curve_y)-1]
    

    
    

    