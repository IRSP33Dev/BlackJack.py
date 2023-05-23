class Carte:
    def __init__(self, valeur, enseigne):
        self.valeur = valeur
        self.enseigne = enseigne

    def __str__(self):
        return f"{self.valeur} de {self.enseigne}"
