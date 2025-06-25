# standard library imports
from tkinter import *
from tkinter import ttk
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
        # lister les livres
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
        for livre in self._model.listerLivres() : 
            tableLivres.insert("", "end", values = list(livre.values()))
        # # # # Add scrollbar
        scrollbar = ttk.Scrollbar(booksVisualisationFrame, orient="vertical", command=tableLivres.yview)
        tableLivres.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        # # packing table des livres
        tableLivres.pack(fill="both", expand=True)


        # TODO: 2 add frame for books search under the visualisation frame
        searchFrame = Frame(self._frame, bg="lightgreen", height=100)
        searchFrame.pack(fill='both', padx=10, pady=10)


        # TODO: 3 add frame for books management (add) under the search frame
        managementFrame = Frame(self._frame, bg="lightcoral")
        managementFrame.pack(fill='both', padx=10, pady=10, expand=True)
        return self._frame

    def getUI(self):
        return self._frame