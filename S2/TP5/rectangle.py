import lib

class Rectangle:
    def __init__(self, hauteur:int = 0, largeur:int = 0) -> None:
        if lib.isPosInt(hauteur) and lib.isPosInt(largeur):
            self.__hauteur = hauteur
            self.__largeur = largeur
        else:
            self.__largeur = 0
            self.__hauteur = 0

    def surface(self) -> int:
        return self.__hauteur * self.__largeur
    
    def perimetre(self) -> int:
        return (self.__largeur + self.__hauteur)*2

    def square(self):
        return True if self.__largeur == self.__hauteur else False
