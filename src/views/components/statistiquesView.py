from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# custom libs
from models.statisticsModel import StatisticsModel

if __name__ == "__main__":
    exit("statistiquesView.py : Ce fichier ne peut pas être exécuté directement. Veuillez exécuter le fichier main.py.")

class StatistiquesView:
    def __init__(self, parent, bibliotheque):
        # Setting color palette
        plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#3498db", "#e74c3c", "#2ecc71", "#f1c40f", "#9b59b6"]) 
        # Linking the model to the view
        self._model = bibliotheque.getStatisticsModel()
        self._frame = Frame(parent)
        self.initUI()

    def initUI(self):
        # This frame contains all our charts
        outerFrame = Frame(self._frame, bg="lightblue")
        outerFrame.pack(fill='both', expand=True, padx=10, pady=10)
        # Setting up UI
        self.initLivreParGenreDiagrammeCirculaire(outerFrame)
        self.initHistogrammeTop10Auteur(outerFrame)
        self.initCourbeTemporelle(outerFrame)

        return self._frame
        
    def getUI(self):
        return self._frame
    
    def initLivreParGenreDiagrammeCirculaire(self, parent) : 
        labels, sizes = self._model.getPieDiagrammeData()
        fig, axe = plt.subplots()
        axe.pie(sizes, labels=labels, autopct='%1.1f%%')
        axe.set_title("Répartition des livres par genre")
        # 
        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()
        canvas.get_tk_widget().pack(side="left" ,fill="both", expand=True)

    def initHistogrammeTop10Auteur(self, parent):
        authors, counts = self._model.getHistogrammeData()
        fig, axe = plt.subplots()
        axe.bar(authors, counts, color='skyblue')
        axe.set_title("Top 10 des auteurs les plus populaires")
        axe.set_xlabel("Auteur")
        axe.set_ylabel("Nombre d'emprunts")
        # 
        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()
        canvas.get_tk_widget().pack(side="left" ,fill="both", expand=True)

    def initCourbeTemporelle(self, parent):
        activity = self._model.getTimeDiagrammeData()
        fig, axe = plt.subplots()
        axe.plot(range(1, 31), activity, marker='o')
        axe.set_title("Activité des emprunts (30 derniers jours)")
        axe.set_xlabel("Jours (du passé à aujourd'hui)")
        axe.set_ylabel("Nombre d'emprunts")
        # 
        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()
        canvas.get_tk_widget().pack(side="left" ,fill="both", expand=True)
