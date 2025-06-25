# standard libs
from json import *
from enum import Enum



# ----------------------------------------------------------------------------------------
# ------------------------------------ LivreRechercheFiltre ------------------------------------
# ----------------------------------------------------------------------------------------
# Enum to define the different filters for searching books
class LivreRechercheFiltre(Enum):
    Titre = "titre"
    Auteur = "auteur"
    Annee = "annee"
    Genre = "genre"
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------
# ------------------------------------ Livre ------------------------------------
# ----------------------------------------------------------------------------------------
class Livre : 
    def __init__(self, isbn, titre, auteur, annee, genre, statut) : 
        # Initialize a book with its attributes
        pass
    # TODO : Implementing getters and setters for the attributes
    pass
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
    



# ----------------------------------------------------------------------------------------
# ------------------------------------ LivresModel ------------------------------------
# ----------------------------------------------------------------------------------------
class LivresModel:

    def __init__(self) :
        # Initialize the model with an empty list of books
        self._livres = None
        self.loadData()

    def loadData(self):
        # TODO : Load the books from a JSON file "livres.json"
        pass
    
    def searchLivre(self, filter = LivreRechercheFiltre.Titre, value=None):
        # TODO : Search for a book by its ISBN
        pass

    def addLivre(self, livre):
        # TODO : Add a book to the list of books
        pass

    def deleteLivre(self, livre):
        # TODO : Delete a book from the list of books
        pass

    def listerLivres(self, filter=None, value=None): # if filter is None, list all books other
        # TODO : List all the books in the list of books
        pass
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------