from tkinter import *


if __name__ == "__main__":
    exit("membresView.py : Ce fichier ne peut pas être exécuté directement. Veuillez exécuter le fichier main.py.")

class MembresView:
    def __init__(self, parent):
        self._frame = Frame(parent)
        self.initUI()

    def initUI(self): 
        return self._frame

    def getUI(self):
        return self._frame