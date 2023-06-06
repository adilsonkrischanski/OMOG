import numpy as np

class Vector:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def get(self):
        return np.array([self.x, self.y])


    

class Pointer:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        self.POX = 0
        self.POY = 0


    def translate(self, dx,dy):
        self.POX = dx
        self.POY = dy
        self.x += self.POX
        self.y += self.POY


    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def get(self):
        return np.array([self.x, self.y])
