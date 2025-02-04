class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        """Affiche les coordonnées du point."""
        print(f"Les coordonnées du point sont : ({self.x}, {self.y})")

    def afficherX(self):
        """Affiche la coordonnée horizontale."""
        print(f"La coordonnée x est : {self.x}")

    def afficherY(self):
        """Affiche la coordonnée verticale."""
        print(f"La coordonnée y est : {self.y}")

    def changerX(self, nouveau_x):
        """Change la valeur de x."""
        self.x = nouveau_x

    def changerY(self, nouveau_y):
        """Change la valeur de y."""
        self.y = nouveau_y


# Exemple d'utilisation :
if __name__ == "__main__":
    point1 = Point(2, 3)
    point1.afficherLesPoints()
    point1.afficherX()
    point1.afficherY()
    
    # Changement des coordonnées
    point1.changerX(5)
    point1.changerY(7)
    point1.afficherLesPoints()
