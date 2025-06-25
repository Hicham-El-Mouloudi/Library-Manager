# standard library imports
from tkinter import *
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
        # TODO: 1 add frame for books visualisation at top of the view
        booksVisualisationFrame = Frame(self._frame, bg="lightblue", height=200)
        booksVisualisationFrame.pack(fill='x', padx=10, pady=10)
        # TODO: 2 add frame for books search under the visualisation frame
        searchFrame = Frame(self._frame, bg="lightgreen", height=100)
        searchFrame.pack(fill='both', padx=10, pady=10)
        # TODO: 3 add frame for books management (add) under the search frame
        managementFrame = Frame(self._frame, bg="lightcoral")
        managementFrame.pack(fill='both', padx=10, pady=10, expand=True)
        return self._frame

    def getUI(self):
        return self._frame