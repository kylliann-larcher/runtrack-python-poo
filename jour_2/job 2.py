class Livre:
    def __init__(self, titre, auteur, nombre_de_page):
        self.__titre = titre
        self.__auteur = auteur 
        self.__nombre_de_page = nombre_de_page

    def get_titre(self):
        return self.__titre
    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nombre_de_page(self):
        return self.__nombre_de_page

    def set_nombre_de_page(self, nombre_de_page):
        if isinstance(nombre_de_page, int) and nombre_de_page > 0:
            self.__nombre_de_page = nombre_de_page
        else:
            print("Erreur: Le nombre de pages doit être un entier positif.")