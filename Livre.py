class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

    def __str__(self):
        return f"{self.titre} par {self.auteur} ({self.annee_publication})" 