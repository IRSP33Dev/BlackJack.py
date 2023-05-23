from carte import Carte
import random

class Paquet:
    def __init__(self):
        enseignes = ['Coeur', 'Carreau', 'Trefle', 'Pique']
        valeurs = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
        self.paquet = [Carte(v, e) for e in enseignes for v in valeurs]
    
    def melanger(self):
        random.shuffle(self.paquet)
    
    def distribuer(self):
        return self.paquet.pop()

    def __str__(self):
        return '\n'.join([str(carte) for carte in self.paquet])
