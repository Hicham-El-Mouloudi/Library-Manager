# standard library imports
from tkinter import *
from tkinter import ttk
# custom imports
from views.components.livresView import LivresView
from views.components.empruntsView import EmpruntsView
from views.components.membresView import MembresView
from views.components.statistiquesView import StatistiquesView

from models.Bibliotheque import Bibliotheque

class MainView:
    def __init__(self):
        # Initialiser la bibliothèque
        self._bibliotheque = Bibliotheque()
        # create the main window
        self._root = Tk()
        # create a Notebook widget to hold the tabs
        self._viewsContainer = ttk.Notebook(self._root)
        self._viewsContainer.pack(fill='both', expand=True)
        
        # create the different views for each tab
        self._livresView = LivresView(self._root, self._bibliotheque)
        self._empruntsView = EmpruntsView(self._root)
        self._membresView = MembresView(self._root)
        self._statistiquesView = StatistiquesView(self._root)
        # 
        self.initUI()
    def initUI(self):
        # initialize the main window
        self._root.title("Système de Gestion de Bibliothèque")
        self._root.geometry("800x600")
        # add the views to the Notebook
        self._viewsContainer.add(self._livresView.getUI(), text="Livres")
        self._viewsContainer.add(self._membresView.getUI(), text="Membres")
        self._viewsContainer.add(self._empruntsView.getUI(), text="Emprunts")
        self._viewsContainer.add(self._statistiquesView.getUI(), text="Statistiques")

    def getUI(self):
        return self._root