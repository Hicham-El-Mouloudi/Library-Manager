from tkinter import *
import matplotlib.pyplot as plt
# custom libs
from src.models.statisticsModel import StatisticsModel

if __name__ == "__main__":
    exit("statistiquesView.py : Ce fichier ne peut pas être exécuté directement. Veuillez exécuter le fichier main.py.")

class StatistiquesView:
    def __init__(self, parent, bibliotheque):
        # Linking the model to the view
        self._model = None
        self._frame = Frame(parent)
        self.initUI()

    def initUI(self):
        return self._frame
        
    def getUI(self):
        return self._frame
    
    def getLivreParGenreDiagrammeCirculaire(self) : 
        pass

    def getHistogrammeTop10Auteur(self):
        pass

    def getCourbeTemporelle(self):
        pass
