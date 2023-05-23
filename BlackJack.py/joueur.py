class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []
    
    def ajouter_carte(self, carte):
        self.main.append(carte)
    
    def total_points(self):
        valeurs = {'As': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valet': 10, 'Dame': 10, 'Roi': 10}
        total = sum(valeurs[carte.valeur] for carte in self.main)
        # Gérer le cas où le joueur a un As (1 ou 11 points)
        if 'As' in [carte.valeur for carte in self.main] and total + 10 <= 21:
            total += 10
        return total

    def __str__(self):
        return f"{self.nom} : {', '.join(str(carte) for carte in self.main)} ({self.total_points()})"
