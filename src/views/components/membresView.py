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
        self._frame = Frame(parent)
        self.initUI()

    def initUI(self): 
        # TODO: Add frame for members visualisation (Treeview)
        # TODO: Add frame for deleting a member
        # TODO: Add frame for adding a member
        return self._frame

    def getUI(self):
        return self._frame

    # TODO: Display all members in the Treeview
    def afficherMembres(self, tableMembres):
        pass

    # TODO: Validate and process member deletion
    def validerSuppression(self, tableMembres):
        pass

    # TODO: Validate and process member addition
    def validerAjoutMembre(self, tableMembres, entries):
        pass