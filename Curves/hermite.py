
import numpy as np
import matplotlib.pyplot as plt


from .Base import Pointer
from .Base import Vector


class Hemite:
    def __init__(self, pointers, Tvectors, Cvectors):
        self.p = pointers
        self.tv = Tvectors
        self.cv = Cvectors

        self.curve = []
        self.tangent_points = []
        self.curvature_points = []

        self.hermite_curve()

        
    def H(self, t, p0, p1, v0, v1, c0, c1):
        a = -6 * p0 + 6 * p1 - 3 * v0 - 3 * v1 + c0 + c1
        b = 15 * p0 - 15 * p1 + 8 * v0 + 7 * v1 - 3 * c0 - 2 * c1
        c = -10 * p0 + 10 * p1 - 6 * v0 - 4 * v1 + 3 * c0 + c1
        d = 0.5 * v0
        e = p0
        
        result = a * t**5 + b * t**4 + c * t**3 + d * t**2 + e * t
        
        return result


    def hermite_curve(self):
        t = np.linspace(0, 1, 100)
        p0 = self.p[0].get()
        p1 = self.p[1].get()
        v0 = self.tv[0].get()
        v1 = self.tv[1].get()
        c0 = self.cv[0].get()
        c1 = self.cv[1].get()

        self.curve = np.array([self.H(t_i, p0, p1, v0, v1, c0, c1) for t_i in t])

        tangent_start = p0
        tangent_end = p0 + v0
        self.tangent_points = np.array([tangent_start, tangent_end])

        curvature_start = p0
        curvature_end = p0 + c0
        self.curvature_points = np.array([curvature_start, curvature_end])

    
    def get(self):
        return self.curve, self.tangent_points,self.curvature_points
    
    def last_poiter(self):
        return self.curve[len(self.curve)-1]


