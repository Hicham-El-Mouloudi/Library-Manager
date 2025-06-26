from tkinter import *

if __name__ == "__main__":
    exit("statistiquesView.py : Ce fichier ne peut pas être exécuté directement. Veuillez exécuter le fichier main.py.")

class StatistiquesView:
    def __init__(self, parent, bibliotheque):
        # Linking the model to the view
        self._model = bibliotheque.getLivresModel() # get the LivresModel instance from the Bibliotheque
        self._frame = Frame(parent)
        self.initUI()

    def initUI(self):
        return self._frame
        
    def getUI(self):
        return self._frame