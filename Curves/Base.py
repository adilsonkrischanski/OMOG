from math import sqrt

class Vector:
    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2
        self.module = sqrt((p1.get_x()-p1.get_x())**2 + (p1.get_y()-p1.get_y())**2 )


    

        
        

class Pointer:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
