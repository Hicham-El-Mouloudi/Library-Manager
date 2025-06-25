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
        # TODO: 

        return self._frame

    def getUI(self):
        return self._frame