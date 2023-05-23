from joueur import Joueur
from paquet import Paquet

class Blackjack:
    def __init__(self):
        self.paquet = Paquet()
        self.joueur = Joueur("Joueur")
        self.croupier = Joueur("Croupier")
    
    def jouer(self):
        while True:
            self.paquet.melanger()
            self.joueur.main = []
            self.croupier.main = []

            self.joueur.ajouter_carte(self.paquet.distribuer())
            self.croupier.ajouter_carte(self.paquet.distribuer())
            self.joueur.ajouter_carte(self.paquet.distribuer())
            self.croupier.ajouter_carte(self.paquet.distribuer())

            print("Main du joueur:")
            print(self.joueur)
            print("Main du croupier:")
            print(self.croupier)

            while True:
                choix = input("Voulez-vous tirer une carte ? (o/n) ")
                if choix.lower() == 'o':
                    self.joueur.ajouter_carte(self.paquet.distribuer())
                    print("Main du joueur:")
                    print(self.joueur)
                    if self.joueur.total_points() > 21:
                        print("Vous avez depasse 21 ! Vous avez perdu.")
                        break
                else:
                    while self.croupier.total_points() < 17:
                        self.croupier.ajouter_carte(self.paquet.distribuer())
                    print("Main du croupier:")
                    print(self.croupier)
                    if self.croupier.total_points() > 21 or self.croupier.total_points() < self.joueur.total_points():
                        print("Vous avez gagne !")
                    elif self.croupier.total_points() > self.joueur.total_points():
                        print("Vous avez perdu.")
                    else:
                        print("Egalite !")
                    break

            choix_rejouer = input("Voulez-vous rejouer ? (o/n) ")
            if choix_rejouer.lower() != 'o':
                break

if __name__ == '__main__':
    jeu = Blackjack()
    jeu.jouer()
