from Livre import Livre

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        if not livre.titre or not livre.auteur:
            raise ValueError("Le livre doit avoir un titre et un auteur.")
        self.livres.append(livre)
        print(f"Livre ajouté : {livre}")

    def supprimer_livre(self, titre):
        livre_trouve = None
        for livre in self.livres:
            if livre.titre == titre:
                livre_trouve = livre
                break

        if livre_trouve:
            self.livres.remove(livre_trouve)
            print(f"Livre supprimé : {livre_trouve}")
        else:
            raise ValueError(f"Le livre avec le titre '{titre}' n'existe pas.")

    def lister_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
        else:
            for livre in self.livres:
                print(livre)

    def sauvegarder_livres(self, fichier):
        try:
            with open(fichier, 'w') as f:
                for livre in self.livres:
                    f.write(f"{livre.titre},{livre.auteur},{livre.annee_publication}\n")
            print(f"Les livres ont été sauvegardés dans {fichier}.")
        except IOError as e:
            print(f"Erreur lors de la sauvegarde des livres : {e}")

    def charger_livres(self, fichier):
        try:
            with open(fichier, 'r') as f:
                self.livres = []
                for ligne in f:
                    titre, auteur, annee = ligne.strip().split(',')
                    livre = Livre(titre, auteur, annee)
                    self.livres.append(livre)
            print(f"Les livres ont été chargés depuis {fichier}.")
        except IOError as e:
            print(f"Erreur lors du chargement des livres : {e}")