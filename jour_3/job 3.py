class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants
    
    def get_nom(self):
        return self.__nom
    
    def set_nom(self, nom):
        self.__nom = nom

    def get_nombre_habitants(self):
        return self.__nombre_habitants
    
    def set_nombre_habitants(self, nombre_habitants):
        if isinstance(nombre_habitants, int) and nombre_habitants >=0:
            self.__nombre_habitants = nombre_habitants
        else:
            print("Erreur: Le nombre d'habitants doit être un entier positif.")

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
    
    def get_nom(self):
        return self.__nom
    
    def set_nom(self, nom):
        self.__nom = nom
    
    def get_age(self):
        return self.__age
    
    def get_ville(self):
        return self.__ville
    
    def ajouterPopulation (self):
        self.__ville.set_nombre_habitants(self.__ville.get_nombre_habitants() + 1)
                 
                 
paris = Ville("Paris", 1000000)
john = Personne("John", 25, paris)

print(paris.get_nombre_habitants())
john.ajouterPopulation()
print(paris.get_nombre_habitants())
 