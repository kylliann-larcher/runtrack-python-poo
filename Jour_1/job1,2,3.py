#Job1,job2,job3

class Operation:
    def __init__(self, number1 = 12,number2 = 3):
        self.number1 = number1
        self.number2 = number2

    def display_number2(self):
        print(f'Le nombre1 est : {self.number1}')
        print(f'Le nombre2 est : {self.number2}')


    def addition(self):
        resultat = self.number1 + self.number2
        print(f'Le resultat de l\'addition est : {resultat}')
    

operation = Operation().addition()
