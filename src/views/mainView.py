# standard library imports
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
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
        # Initializing style for the app
        self._style = ttk.Style()
        self._style.theme_use("default")
        self.initStyle()
        # create a Notebook widget to hold the tabs
        self._viewsContainer = ttk.Notebook(self._root)
        self._viewsContainer.pack(fill='both', expand=True)
        
        # create the different views for each tab
        self._livresView = LivresView(self._root, self._bibliotheque)
        self._membresView = MembresView(self._root, self._bibliotheque)
        self._empruntsView = EmpruntsView(self._root, self._bibliotheque, self._livresView, self._membresView)
        self._statistiquesView = StatistiquesView(self._root, self._bibliotheque)
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

    def initStyle(self) : 
        # Notebook style
        tabFont = tkFont.Font(family="Calibri", size=12)
        self._style.configure("TNotebook.Tab", font=tabFont, background="#0096c7", foreground="#03045e")
        self._style.configure("TNotebook", background="#0096c7", borderwidth=0)
        self._style.map("TNotebook.Tab",
            background=[
                ("selected", "#00b4d8"),
                ("active", "#0077b6")
            ],#style background
            foreground=[
                ("selected", "#caf0f8"),
                ("active", "#caf0f8")
            ] #style text
        )

        # treeView style
        header_font = tkFont.Font(family="Lucida Console", size=14, weight="bold")
        tree_font = tkFont.Font(family="Maiandra GD", size=12)
        self._style.configure("Treeview.Heading", 
                            font=header_font,
                            foreground="#ffffff",    # text color
                            background="#0077b6")    # background color

        self._style.configure("Treeview", 
                            font=tree_font,
                            foreground="#03045e",    # text color
                            background="#caf0f8")    # background color

        # styling buttons
        button_font = tkFont.Font(family="Helvetica", size=14)
        self._style.configure("TButton",
                            font=button_font,
                            foreground="#023e8a",
                            background="#48cae4")

        self._style.map("TButton",
                        foreground=[('active', '#023e8a')],
                        background=[('active', '#90e0ef')])
        # stylling labels
        label_font = tkFont.Font(family="Helvetica", size=14)
        self._style.configure("TLabel", font=label_font, foreground="darkgreen")