# standard libs
from json import load, dump
from enum import Enum
# custom imports
from models.Livre import Livre


# ----------------------------------------------------------------------------------------
# ------------------------------------ LivreInexistantError ------------------------------------
# ----------------------------------------------------------------------------------------
# Custom exception for handling cases where a book does not exist
class LivreInexistantError(Exception):
    def __init__(self, message="Le livre n'existe pas dans les données disponible."):
        self.message = message
        super().__init__(self.message)
# ----------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------
# ------------------------------------ LivreRechercheFiltre ------------------------------------
# ----------------------------------------------------------------------------------------
# Enum to define the different filters for searching books
class LivreRechercheFiltre(Enum): # C'est pas encore utilisé !!!!!!!!
    ISBN = "isbn"  # This is used to search by index in the list of books
    # Other filters
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
    
    def searchLivre(self, filter = LivreRechercheFiltre.Titre, value=None): # cette fct est utilisées dans la vue empruntsView.py pour rechercher un livre par son titre, isbn.
        match(filter):
            # par titre
            case LivreRechercheFiltre.ISBN:
                for livre in self._livres:
                    if livre['ISBN'].lower() == value.lower():
                        return livre
                raise LivreInexistantError(f"Le livre avec l'ISBN '{value}' n'existe pas dans les données disponibles.")
            case LivreRechercheFiltre.Titre:
                for livre in self._livres:
                    if livre['titre'].lower() == value.lower():
                        return livre
                raise LivreInexistantError(f"Le livre avec le titre '{value}' n'existe pas dans les données disponibles.")
            # par auteur
            case LivreRechercheFiltre.Auteur:
                for livre in self._livres:
                    if livre['auteur'].lower() == value.lower():
                        return livre
                raise LivreInexistantError(f"Le livre avec l'auteur '{value}' n'existe pas dans les données disponibles.")
            # par annee
            case LivreRechercheFiltre.Annee:
                for livre in self._livres:
                    if livre['annee'] == value:
                        return livre
                raise LivreInexistantError(f"Le livre publié en l'année '{value}' n'existe pas dans les données disponibles.")
            # par genre
            case LivreRechercheFiltre.Genre:
                for livre in self._livres:
                    if livre['genre'].lower() == value.lower():
                        return livre
                raise LivreInexistantError(f"Le livre du genre '{value}' n'existe pas dans les données disponibles.")
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
        print(f"Book added: {livre.titre} by {livre.auteur}")

    def deleteLivres(self, lesIndiceDesLivreASupprimer): # supprimer a partir d'un intervalle de lignes
        lesIndiceDesLivreASupprimer = sorted(lesIndiceDesLivreASupprimer, reverse=True)
        for indice in lesIndiceDesLivreASupprimer : 
            if not(indice < 0 or indice >= len(self._livres)):
                self._livres.pop(indice)
            else:
                raise IndexError(f"Index {indice} is out of range for the books list.")
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