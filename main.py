from Bibliotheque import Bibliotheque  as biblio
from Livre import Livre

def main():  # Créer une instance de la classe Bibliotheque

    while True:
        print("\n--- Gestion de la Bibliothèque ---")
        print("1. Ajouter un livre")
        print("2. Supprimer un livre")
        print("3. Lister tous les livres")
        print("4. Sauvegarder les livres dans un fichier")
        print("5. Charger les livres depuis un fichier")
        print("6. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            titre = input("Titre du livre : ")
            auteur = input("Auteur du livre : ")
            annee = input("Année de publication : ")
            try:
                livre = Livre(titre, auteur, int(annee))
                biblio.ajouter_livre(livre)
            except ValueError as e:
                print(f"Erreur : {e}")

        elif choix == "2":
            titre = input("Titre du livre à supprimer : ")
            try:
                biblio.supprimer_livre(titre)
            except ValueError as e:
                print(f"Erreur : {e}")

        elif choix == "3":
            biblio.lister_livres()

        elif choix == "4":
            fichier = input("Nom du fichier pour sauvegarder : ")
            biblio.sauvegarder_livres(fichier)

        elif choix == "5":
            fichier = input("Nom du fichier pour charger : ")
            biblio.charger_livres(fichier)

        elif choix == "6":
            print("Au revoir !")
            break

        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()