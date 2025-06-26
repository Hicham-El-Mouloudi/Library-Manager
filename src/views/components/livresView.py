# standard library imports
from tkinter import *
from tkinter import ttk, messagebox
# custom imports
from models.livresModel import LivresModel


if __name__ == "__main__":
    exit("livresView.py : Ce fichier ne peut pas être exécuté directement. Veuillez exécuter le fichier main.py.")

class LivresView : 
    def __init__(self, parent): 
        # Linking the model to the view
        self._model = LivresModel()
        self._model.loadData() # Load the data from the JSON file 'livres.json'
        # the container frame for all UI components of this view
        self._frame = Frame(parent)
        self.initUI()

    def initUI(self):
        # ---------------- lister les livres
        booksVisualisationFrame = Frame(self._frame, bg="lightblue", height=200)
        booksVisualisationFrame.pack(fill='x', padx=10, pady=10)
        # # adding a treeView to list books
        _columns = ['ISBN', 'Titre', 'Auteur', 'Année', 'Genre', 'Statut']
        tableLivres = ttk.Treeview(booksVisualisationFrame, columns=_columns, show='headings')
        # # # config columns
        for clmn in _columns :
            tableLivres.heading(clmn, text=clmn) # adding labels to columns
            tableLivres.column(clmn, width=100) # confihuring each column
        # # # adding books to the treeView
        self.afficherLivres(tableLivres)
        # # # # Add scrollbar
        scrollbar = ttk.Scrollbar(booksVisualisationFrame, orient="vertical", command=tableLivres.yview)
        tableLivres.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        # # packing table des livres
        tableLivres.pack(fill="both", expand=True)


        # ---------------- deleting a book
        deleteFrame = Frame(self._frame, bg="lightgreen", height=100)
        deleteFrame.pack(fill='both', padx=10, pady=10)
        # the button to del -> binding it to delete the selected livres
        deleteButton = Button(deleteFrame, width=36, text="Supprimer Les Elements Selectionnés", command= lambda : self.validerSuppression(tableLivres))
        deleteButton.pack()


        # TODO: 3 add frame for books management (add) under the search frame
        managementFrame = Frame(self._frame, bg="lightcoral")
        managementFrame.pack(fill='both', padx=10, pady=10, expand=True)
        return self._frame

    def getUI(self):
        return self._frame
    
    # 
    def afficherLivres(self, tableLivres):
        tableLivres.set_children("")
        for livre in self._model.listerLivres() : 
            tableLivres.insert("", "end", values = list(livre.values()))

    def validerSuppression(self,tableLivres) :
        selected = tableLivres.selection() # liste des ID des lignes selectionnée
        if len(selected) == 0 : # the user does not select any -> show alert
            messagebox.showerror("Erreur","Vous devez selectionner des entrées a supprimer")
            return
        #verifier si l'utilisateur veut vraiment la supprimmer
        response = messagebox.askyesno("Confirmation De Suppression", "Est-ce que vous voulez vraiment supprimer les livres selectionnés ?")
        if response : 
            lesIndiceDesLivreASupprimer = [tableLivres.index(indx) for indx in selected] # obtenir les indices des lignes selectionées, à partir des ID obtnue par 'selected'
            self._model.deleteLivres(lesIndiceDesLivreASupprimer)
            self.afficherLivres(tableLivres) # re-afficher apres suppression 
        # sinon ignoreer