class Personnage:
    def __init__(self, x, y):
        """
        Constructeur qui initialise la position du personnage dans la matrice.
        x représente l'indice de ligne et y l'indice de colonne.
        """
        self.x = x
        self.y = y

    def gauche(self):
        """
        Déplace le personnage vers la gauche.
        Cela diminue l'indice de colonne (y).
        """
        self.y -= 1

    def droite(self):
        """
        Déplace le personnage vers la droite.
        Cela augmente l'indice de colonne (y).
        """
        self.y += 1

    def haut(self):
        """
        Déplace le personnage vers le haut.
        Cela diminue l'indice de ligne (x).
        """
        self.x -= 1

    def bas(self):
        """
        Déplace le personnage vers le bas.
        Cela augmente l'indice de ligne (x).
        """
        self.x += 1

    def position(self):
        """
        Renvoie les coordonnées actuelles du personnage sous forme d'un tuple.
        """
        return (self.x, self.y)

# Exemple d'utilisation :
if __name__ == "__main__":
    # Création d'un personnage positionné initialement à la position (2, 3)
    perso = Personnage(2, 3)
    print("Position initiale :", perso.position())

    # Déplacer le personnage
    perso.gauche()
    print("Après déplacement à gauche :", perso.position())

    perso.droite()
    print("Après déplacement à droite :", perso.position())

    perso.haut()
    print("Après déplacement vers le haut :", perso.position())

    perso.bas()
    print("Après déplacement vers le bas :", perso.position())
