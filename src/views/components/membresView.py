if __name__ == "__main__":
    exit("membresView.py : Ce fichier ne peut pas être exécuté directement. Veuillez exécuter le fichier main.py.")

# standard library imports
from tkinter import *
from tkinter import ttk, messagebox
# custom imports
from models.membresModel import MembresModel
from models.Membre import Membre



class MembresView:
    def __init__(self, parent, bibliotheque):
        # Linking the model to the view
        self._model = bibliotheque.getMembresModel() # get the LivresModel instance from the Bibliotheque
        self._model.loadData()
        # the container frame for all UI components of this view
        self._frame = Frame(parent)
        self.initUI()

    def initUI(self): 
        # ---------------- lister les membres
        membersVisualisationFrame = Frame(self._frame, bg="#caf0f8")
        membersVisualisationFrame.pack(fill='both', expand=True, padx=10, pady=10)
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
        deleteFrame = Frame(self._frame, bg="white", height=100)
        deleteFrame.pack(fill='both', padx=10, pady=10)
        deleteButton = ttk.Button(deleteFrame, width=36, text=" Supprimer ", command=lambda: self.validerSuppression(tableMembres))
        deleteButton.pack()

        # ---------------- adding a member
        memberAddFrame = Frame(self._frame, bg="white")
        memberAddFrame.pack(fill='both', padx=10, pady=10, expand=True)
        labels = ['ID', 'Nom']
        self._entries = {}
        for label in labels:
            f = Frame(memberAddFrame, bg="white")
            f.pack(side='top', padx=5, pady=5)
            lbl = ttk.Label(f, text=label, width=10)
            lbl.pack(side='left', padx=5, pady=5)
            entry = Entry(f, width=40)
            entry.pack(side='left', padx=5, pady=5)
            self._entries[label] = entry
        addButton = ttk.Button(
            memberAddFrame,
            width=36,
            text=" Ajouter ",
            command=lambda: self.validerAjoutMembre(tableMembres, self._entries.values())
        )
        addButton.pack(side='top', padx=5, pady=5)
        saveButton = ttk.Button(
            memberAddFrame,
            width=36,
            text=" Enregistrer ",
            command=lambda: (self._model.saveData(), messagebox.showinfo("Membres", "Les membres ont été sauvegardés avec succès !"))
        )
        saveButton.pack(side='right', padx=5, pady=5)
        return self._frame

    def getUI(self):
        return self._frame

    def afficherMembres(self, tableMembres):
        tableMembres.set_children("") # clear the table first
        for membre in self._model.listerMembres():
            # Format the list of borrowed books as a comma-separated string
            tableMembres.insert("", "end", values=membre.getValuesList())

    def validerSuppression(self, tableMembres):
        selected = tableMembres.selection()  # liste des ID des lignes selectionnées
        if len(selected) == 0:
            messagebox.showerror("Erreur", "Vous devez selectionner des membres à supprimer")
            return
        response = messagebox.askyesno("Confirmation De Suppression", "Est-ce que vous voulez vraiment supprimer les membres selectionnés ?")
        if response:
            indicesASupprimer = [tableMembres.index(indx) for indx in selected] # obtenir les indices des lignes selectionées, à partir des ID obtnue par 'selected'
            self._model.deleteMembres(indicesASupprimer)
            self.afficherMembres(tableMembres) # re-afficher apres suppression 
        # sinon ignorer

    #entries : liste of Entry widgets
    #tableMembres : Treeview widget
    def validerAjoutMembre(self, tableMembres, entries):
        if any(entry.get() == "" for entry in self._entries.values()):
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis")
            return
        # Ajouter le membre
        self._model.addMembre(self._entries["ID"].get().strip(), self._entries["Nom"].get().strip())
        messagebox.showinfo("Succès", "Membre ajouté avec succès")
        # vider les champs
        for entry in entries:
            entry.delete(0, "end")
        self.afficherMembres(tableMembres)  # re-afficher apres ajout