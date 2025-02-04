class Personne():
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter( nom, prenom):
        print(f'Je suis {prenom} {nom}')


personne_1= Personne.se_presenter("jean", "dupont")
print (personne_1)




