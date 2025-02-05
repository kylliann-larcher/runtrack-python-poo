class Rectangle:
    def __init__(self, longueur , largeur ):
        self.__longueur = longueur #attribut prive
        self.__largeur = largeur

    def get_longueur(self): #RECUPERE LA LONGUEUR
        return self.__longueur
    
    def get_largeur(self): #---------LA LARGEUR
        return self.__largeur
    
    def set_longueur(self,nouvelle_longueur): #REGLE LA LONGUEUR
        self.__longueur = nouvelle_longueur #REGLE LA LARGEUR

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

r = Rectangle(10, 5)
print(r.get_longueur())
r.set_largeur(6)
print(r.get_largeur())


        