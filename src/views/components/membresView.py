# standard library imports
from tkinter import *
from tkinter import ttk, messagebox
# custom imports
from models.membresModel import MembresModel


if __name__ == "__main__":
    exit("membresView.py : Ce fichier ne peut pas être exécuté directement. Veuillez exécuter le fichier main.py.")

class MembresView:
    def __init__(self, parent, bibliotheque):
        # Linking the model to the view
        self._model = bibliotheque.getLivresModel() # get the LivresModel instance from the Bibliotheque
        self._model.loadData()
        # the container frame for all UI components of this view
        self._frame = Frame(parent)
        self.initUI()

    def initUI(self): 
        # ---------------- lister les membres
        membersVisualisationFrame = Frame(self._frame, bg="lightblue", height=200)
        membersVisualisationFrame.pack(fill='x', padx=10, pady=10)
        # adding a treeView to list members
        _columns = ['ID', 'Nom', 'Livres Empruntés']
        tableMembres = ttk.Treeview(membersVisualisationFrame, columns=_columns, show='headings')
        for clmn in _columns:
            tableMembres.heading(clmn, text=clmn)
            tableMembres.column(clmn, width=150)
        self.afficherMembres(tableMembres)
        scrollbar = ttk.Scrollbar(membersVisualisationFrame, orient="vertical", command=tableMembres.yview)
        tableMembres.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        tableMembres.pack(fill="both", expand=True)

        # ---------------- deleting a member
        deleteFrame = Frame(self._frame, bg="lightgreen", height=100)
        deleteFrame.pack(fill='both', padx=10, pady=10)
        deleteButton = Button(deleteFrame, width=36, text="Supprimer Les Membres Selectionnés", command=lambda: self.validerSuppression(tableMembres))
        deleteButton.pack()

        # ---------------- adding a member
        memberAddFrame = Frame(self._frame, bg="lightcoral")
        memberAddFrame.pack(fill='both', padx=10, pady=10, expand=True)
        labels = ['ID', 'Nom']
        self._entries = {}
        for label in labels:
            f = Frame(memberAddFrame, bg="lightcoral")
            f.pack(side='top', padx=5, pady=5)
            lbl = Label(f, text=label, width=10)
            lbl.pack(side='left', padx=5, pady=5)
            entry = Entry(f, width=40)
            entry.pack(side='left', padx=5, pady=5)
            self._entries[label] = entry
        addButton = Button(
            memberAddFrame,
            width=36,
            text="Ajouter Un Membre",
            command=lambda: self.validerAjoutMembre(tableMembres, self._entries.values())
        )
        addButton.pack(side='top', padx=5, pady=5)
        saveButton = Button(
            memberAddFrame,
            width=36,
            text="Enregistrer Les Membres",
            command=lambda: (self._model.saveData(), messagebox.showinfo("Membres", "Les membres ont été sauvegardés avec succès !"))
        )
        saveButton.pack(side='right', padx=5, pady=5)
        return self._frame

    def getUI(self):
        return self._frame

    def afficherMembres(self, tableMembres):
        tableLivres.set_children("") # clear the table first
        for membre in self._model.listerMembres():
            # Format the list of borrowed books as a comma-separated string
            livresEmpruntes = ', '.join(membre.get('lesLivresEmpruntes', []))
            tableMembres.insert("", "end", values=(membre.get('id', ''), membre.get('nom', ''), livresEmpruntes))

    # TODO: Validate and process member deletion
    def validerSuppression(self, tableMembres):
        pass

    # TODO: Validate and process member addition
    def validerAjoutMembre(self, tableMembres, entries):
        pass