# standard libs
from json import load, dump
from enum import Enum
# custom imports
from models.Livre import Livre



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
            with open('data/livres.json', 'r', encoding="utf-8") as file: # utf-8 pour afficher correctement des characters spec (é...etc)
                self._livres = load(file)
        except FileNotFoundError:
            self._livres = []
    
    def searchLivre(self, filter = LivreRechercheFiltre.Titre, value=None):
        match(filter):
            # par titre
            case LivreRechercheFiltre.Titre:
                for livre in self._livres:
                    if livre['titre'].lower() == value.lower():
                        return livre
                return False
            # par auteur
            case LivreRechercheFiltre.Auteur:
                for livre in self._livres:
                    if livre['auteur'].lower() == value.lower():
                        return livre
                return False
            # par annee
            case LivreRechercheFiltre.Annee:
                for livre in self._livres:
                    if livre['annee'] == value:
                        return livre
                return False
            # par genre
            case LivreRechercheFiltre.Genre:
                for livre in self._livres:
                    if livre['genre'].lower() == value.lower():
                        return livre
                return False
            case _:
                raise ValueError("Invalid filter type provided.")

    def addLivre(self, livre):
        self._livres.append({
            'isbn': livre.isbn,
            'titre': livre.titre,
            'auteur': livre.auteur,
            'annee': livre.annee,
            'genre': livre.genre,
            'statut': livre.statut
        })

    def deleteLivres(self, lesIndiceDesLivreASupprimer): # supprimer a partir d'un intervalle de lignes
        for indice in lesIndiceDesLivreASupprimer : 
            if not(indice < 0 or indice >= len(self._livres)):
                self._livres.pop(indice)
            else:
                raise ValueError("Livre not found in the list.")
        return self._livres

    def listerLivres(self):
        # Return a list of all books
        return self._livres

    def saveData(self):
        # Save the books to "livres.json"
        with open('data/livres.json', 'w') as file:
            dump(self._livres, file, indent=4)
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------