from tkinter import *
import matplotlib.pyplot as plt
# custom libs
from src.models.statisticsModel import StatisticsModel

if __name__ == "__main__":
    exit("statistiquesView.py : Ce fichier ne peut pas être exécuté directement. Veuillez exécuter le fichier main.py.")

class StatistiquesView:
    def __init__(self, parent, bibliotheque):
        # Linking the model to the view
        self._model = bibliotheque.getStatisticsModel()
        self._frame = Frame(parent)
        self.initUI()

    def initUI(self):
        return self._frame
        
    def getUI(self):
        return self._frame
    
    def getLivreParGenreDiagrammeCirculaire(self) : 
        labels, sizes = stats_model.getPieDiagrammeData()
        fig, axe = plt.subplots()
        axe.pie(sizes, labels=labels, autopct='%1.1f%%')
        axe.set_title("Répartition des livres par genre")

    def getHistogrammeTop10Auteur(self):
        authors, counts = self._model.getHistogrammeData()
        fig, axe = plt.subplots()
        axe.bar(authors, counts, color='skyblue')
        axe.set_title("Top 10 des auteurs les plus populaires")
        axe.set_xlabel("Auteur")
        axe.set_ylabel("Nombre d'emprunts")

    def getCourbeTemporelle(self):
        pass
