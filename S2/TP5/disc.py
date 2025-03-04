import lib

class Disc:
    def __init__(self, x:int, y:int, rayon:int):
        if lib.isPosInt(x) and lib.isPosInt(y) and lib.isPosInt(rayon):
            self.__x = x
            self.__y = y
            self.__rayon = rayon
        else:
            self.__x = 0
            self.__y = 0
            self.__rayon = 0

    @property
    def x(self):
        return self.__x
    
    @property 
    def y(self):
        return self.__y
    
    @property
    def rayon(self):
        return self.__rayon
    

    @x.setter
    def x(self, new_x:int):
        if lib.isPosInt(new_x):
            self.__x = new_x
    
    @y.setter 
    def y(self, new_y:int):
        if lib.isPosInt(new_y):
            self.__x = new_y
    
    @rayon.setter
    def rayon(self, new_rayon):
        if lib.isPosInt(new_rayon):
            self.__rayon = new_rayon
