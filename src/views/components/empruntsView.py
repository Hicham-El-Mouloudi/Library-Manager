from tkinter import *

if __name__ == "__main__":
    exit("empruntsView.py : Ce fichier ne peut pas être exécuté directement. Veuillez exécuter le fichier main.py.")

class EmpruntsView:
    def __init__(self, parent, bibliotheque): 
        # Linking the model to the view
        self._model = None
        self._frame = Frame(parent)
        self.initUI()

    def initUI(self):
        return self._frame

    def getUI(self):
        return self._frame