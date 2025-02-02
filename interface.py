import tkinter as tk
from tkinter import messagebox, simpledialog
from Bibliotheque import Bibliotheque
from Livre import Livre

class interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de la Bibliothèque")
        
        self.biblio = Bibliotheque()

        # Boutons
        tk.Button(root, text="Ajouter un livre", command=self.ajouter_livre).pack(pady=5)
        tk.Button(root, text="Supprimer un livre", command=self.supprimer_livre).pack(pady=5)
        tk.Button(root, text="Lister les livres", command=self.lister_livres).pack(pady=5)
        tk.Button(root, text="Sauvegarder les livres", command=self.sauvegarder_livres).pack(pady=5)
        tk.Button(root, text="Charger les livres", command=self.charger_livres).pack(pady=5)
        tk.Button(root, text="Quitter", command=root.quit).pack(pady=5)

        # Zone d'affichage
        self.text_area = tk.Text(root, height=10, width=50)
        self.text_area.pack(pady=10)
    
    def ajouter_livre(self):
        titre = simpledialog.askstring("Ajouter", "Titre du livre :")
        auteur = simpledialog.askstring("Ajouter", "Auteur du livre :")
        annee = simpledialog.askinteger("Ajouter", "Année de publication :")
        
        if titre and auteur and annee:
            try:
                livre = Livre(titre, auteur, annee)
                self.biblio.ajouter_livre(livre)
                messagebox.showinfo("Succès", "Livre ajouté !")
            except ValueError as e:
                messagebox.showerror("Erreur", str(e))
        else:
            messagebox.showwarning("Attention", "Veuillez remplir tous les champs.")
    
    def supprimer_livre(self):
        titre = simpledialog.askstring("Supprimer", "Titre du livre à supprimer :")
        if titre:
            try:
                self.biblio.supprimer_livre(titre)
                messagebox.showinfo("Succès", "Livre supprimé !")
            except ValueError as e:
                messagebox.showerror("Erreur", str(e))
        else:
            messagebox.showwarning("Attention", "Veuillez entrer un titre.")
    
    def lister_livres(self):
        self.text_area.delete(1.0, tk.END)
        if not self.biblio.livres:
            self.text_area.insert(tk.END, "La bibliothèque est vide.\n")
        else:
            for livre in self.biblio.livres:
                self.text_area.insert(tk.END, str(livre) + "\n")
    
    def sauvegarder_livres(self):
        fichier = simpledialog.askstring("Sauvegarder", "Nom du fichier :")
        if fichier:
            self.biblio.sauvegarder_livres(fichier)
            messagebox.showinfo("Succès", "Livres sauvegardés !")
    
    def charger_livres(self):
        fichier = simpledialog.askstring("Charger", "Nom du fichier :")
        if fichier:
            self.biblio.charger_livres(fichier)
            messagebox.showinfo("Succès", "Livres chargés !")
            self.lister_livres()

if __name__ == "__main__":
    # Crée la fenêtre principale
    root = tk.Tk()
    # Initialise l'interface
    app = interface(root)
    # Lance la boucle d'affichage et d'interaction
    root.mainloop()