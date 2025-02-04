class Animal():
    def __init__(self, age=0, name="Inconnu"):
        self.age = age
        self.name = name
    
    def grow_old(self):
        print(f"L'âge de l'animal est de {self.age}")
        self.age += 1

    def nommer(self, nouveau_nom):
        self.name = nouveau_nom
        print(f"Le nom de l'animal est {self.name}")

# Création d'une instance de Animal
mon_animal = Animal()

# Affichage de l'âge initial
print("Âge initial :", mon_animal.age)

# Vieillissement de l'animal
mon_animal.grow_old()

# Affichage de l'âge mis à jour
print("Âge après vieillissement :", mon_animal.age)

# Nommer l'animal
mon_animal.nommer("Bobby")
