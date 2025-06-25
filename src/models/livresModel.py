# standard libs
from json import load, dump
from enum import Enum
# custom imports



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
        self._isbn = isbn
        self._titre = titre
        self._auteur = auteur
        self._annee = annee
        self._genre = genre
        self._statut = statut # disponible ou emprunté

    # getters and setters for the attributes
    @property
    def isbn(self):
        return self._isbn
    @isbn.setter
    def isbn(self, value):
        self._isbn = value

    @property
    def titre(self):
        return self._titre
    @titre.setter
    def titre(self, value):
        self._titre = value
    
    @property
    def auteur(self):
        return self._auteur
    @auteur.setter
    def auteur(self, value):
        self._auteur = value
    
    @property
    def annee(self):
        return self._annee
    @annee.setter
    def annee(self, value):
        self._annee = value
    
    @property
    def genre(self):
        return self._genre
    @genre.setter
    def genre(self, value):
        self._genre = value
    
    @property
    def statut(self):
        return self._statut
    @statut.setter
    def statut(self, value):
        self._statut = value
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
        # Load the books from "livres.jsonn"
        try:
            with open('data/livres.json', 'r') as file:
                self._livres = load(file)
        except FileNotFoundError:
            self._livres = []
    
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

    def saveData(self):
        # Save the books to "livres.json"
        with open('data/livres.json', 'w') as file:
            dump(self._livres, file, indent=4)
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------