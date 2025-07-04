if __name__ == "__main__":
    exit("livresView.py : Ce fichier ne peut pas être exécuté directement. Veuillez exécuter le fichier main.py.")

# standard library imports
from tkinter import *
from tkinter import ttk, messagebox
# custom imports
from models.livresModel import LivresModel
from models.Livre import Livre, StatutLivreEnum



class LivresView : 
    def __init__(self, parent, bibliotheque): 
        # Linking the model to the view
        self._model = bibliotheque.getLivresModel() # get the LivresModel instance from the Bibliotheque
        self._model.loadData() # Load the data from the JSON file 'livres.json'
        # the container frame for all UI components of this view
        self._frame = Frame(parent)
        # TreeView listing books
        # # adding a treeView to list books
        self.booksVisualisationFrame = Frame(self._frame, bg="#caf0f8")
        self._columns = ['ISBN', 'Titre', 'Auteur', 'Année', 'Genre', 'Statut']
        self.tableLivres = ttk.Treeview(self.booksVisualisationFrame, columns=self._columns, show='headings')
        # 
        self.initUI()

    def initUI(self):
        # ---------------- lister les livres
        self.booksVisualisationFrame.pack(fill='both', expand=True, padx=10, pady=10)
        # # # config columns
        for clmn in self._columns :
            self.tableLivres.heading(clmn, text=clmn) # adding labels to columns
            self.tableLivres.column(clmn, width=100) # confihuring each column
        # # # adding books to the treeView
        self.afficherLivres()
        # # # # Add scrollbar
        scrollbar = ttk.Scrollbar(self.booksVisualisationFrame, orient="vertical", command=self.tableLivres.yview)
        self.tableLivres.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        # # packing table des livres
        self.tableLivres.pack(fill="both", expand=True)


        # ---------------- deleting a book
        deleteFrame = Frame(self._frame, bg="white", height=100)
        deleteFrame.pack(fill='both', padx=10, pady=10)
        # the button to del -> binding it to delete the selected livres
        deleteButton = ttk.Button(deleteFrame, width=36, text=" Supprimer ", command= lambda : self.validerSuppression())
        deleteButton.pack()


        # ---------------- adding a book
        bookAddFrame = Frame(self._frame, bg="white")
        bookAddFrame.pack(fill='both', padx=10, pady=10, expand=True)
        # the labels and entries for adding a book
        labels = ['ISBN', 'Titre', 'Auteur', 'Année', 'Genre']
        self._entries = {}
        for label in labels:
            f = Frame(bookAddFrame, bg="white")
            f.pack(side='top', padx=5, pady=5)
            lbl = ttk.Label(f, text=label, width=10)
            lbl.pack(side='left', padx=5, pady=5)
            entry = Entry(f, width=40)
            entry.pack(side='left', padx=5, pady=5)
            self._entries[label] = entry
        # the button to add a book
        addButton = ttk.Button(
            bookAddFrame,
            width=36,
            text=" Ajouter ",
            command= lambda: self.validerAjoutLivre(self._entries.values())
        )
        addButton.pack(side='top', padx=5, pady=5)
        # # saving the books to the JSON file
        saveButton = ttk.Button(
            bookAddFrame,
            width=36,
            text=" Enregistrer ",
            command=lambda: (self._model.saveData(), messagebox.showinfo("Livres", "Les livres ont été sauvegardés avec succès !"))
        )
        saveButton.pack(side='right', padx=5, pady=5)
        return self._frame

    def getUI(self):
        return self._frame
    
    # 
    def afficherLivres(self):
        self.tableLivres.set_children("") # clear the table first
        for livre in self._model.listerLivres() : 
            self.tableLivres.insert("", "end", values = livre.getValuesList())

    def validerSuppression(self) :
        selected = self.tableLivres.selection() # liste des ID des lignes selectionnée
        if len(selected) == 0 : # the user does not select any -> show alert
            messagebox.showerror("Erreur","Vous devez selectionner des entrées a supprimer")
            return
        #verifier si l'utilisateur veut vraiment la supprimmer
        response = messagebox.askyesno("Confirmation De Suppression", "Est-ce que vous voulez vraiment supprimer les livres selectionnés ?")
        if response : 
            lesIndiceDesLivreASupprimer = [self.tableLivres.index(indx) for indx in selected] # obtenir les indices des lignes selectionées, à partir des ID obtnue par 'selected'
            self._model.deleteLivres(lesIndiceDesLivreASupprimer)
            self.afficherLivres() # re-afficher apres suppression 
        # sinon ignoreer

    def validerAjoutLivre(self, _entries):
        if any(entry.get() == "" for entry in self._entries.values()):
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis")
            return
        self._model.addLivre(
            self._entries['ISBN'].get().strip(),
            self._entries['Titre'].get().strip(),
            self._entries['Auteur'].get().strip(),
            self._entries['Année'].get().strip(),
            self._entries['Genre'].get().strip() # statut = StatutLivreEnum.DISPONIBLE.value (default)
        )
        messagebox.showinfo("Succès", "Livre ajouté avec succès")
        # vider les champs
        for entry in _entries:
            entry.delete(0, "end")
        self.afficherLivres()  # re-afficher apres ajout