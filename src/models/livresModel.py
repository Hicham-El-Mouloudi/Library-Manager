# standard libs
from json import load, dump
from enum import Enum
# custom imports
from src.models.Livre import Livre, StatutLivreEnum


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
    ISBN = "ISBN"  # This is used to search by index in the list of books
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
                self._livres = load(file) # contains a list of dictionaries, each representing a book
                self._livres = self.fromJSON(self._livres) # converting the list of dictionaries to a list of Livre objects
        except FileNotFoundError:
            self._livres = []
    
    def toJSON(self, listDesObjLivres):
        # transforming a list of Livre objects to a list of dictionaries
        return [ livre.__dict__ for livre in listDesObjLivres ]
    
    def fromJSON(self, listDesDictLivres):
        # transforming a list of dictionaries to a list of Livre objects
        return [ Livre(livre["ISBN"], livre["titre"], livre["auteur"], livre["annee"], livre["genre"], livre["statut"]) for livre in listDesDictLivres]
    
    def searchLivre(self, filter = LivreRechercheFiltre.ISBN, value=""): # cette fct est utilisées dans la vue empruntsView.py pour rechercher un livre par son titre, ISBN.
        print("type(filter):", type(filter), "value:", filter)
        print("type(LivreRechercheFiltre.ISBN):", type(LivreRechercheFiltre.ISBN), "value:", LivreRechercheFiltre.ISBN)
        print("searchLivre : called with value : " + filter.value + "\t check : " + str(filter == LivreRechercheFiltre.ISBN))
        match(filter):
            # par titre
            case LivreRechercheFiltre.ISBN:
                for livre in self._livres:
                    if livre.ISBN.lower() == value.lower():
                        return livre
                raise LivreInexistantError(f"Le livre avec l'ISBN '{value}' n'existe pas dans les données disponibles.")
            case LivreRechercheFiltre.Titre:
                for livre in self._livres:
                    if livre.titre.lower() == value.lower():
                        return livre
                raise LivreInexistantError(f"Le livre avec le titre '{value}' n'existe pas dans les données disponibles.")
            # par auteur
            case LivreRechercheFiltre.Auteur:
                for livre in self._livres:
                    if livre.auteur.lower() == value.lower():
                        return livre
                raise LivreInexistantError(f"Le livre avec l'auteur '{value}' n'existe pas dans les données disponibles.")
            # par annee
            case LivreRechercheFiltre.Annee:
                for livre in self._livres:
                    if livre.annee == value:
                        return livre
                raise LivreInexistantError(f"Le livre publié en l'année '{value}' n'existe pas dans les données disponibles.")
            # par genre
            case LivreRechercheFiltre.Genre:
                for livre in self._livres:
                    if livre.genre.lower() == value.lower():
                        return livre
                raise LivreInexistantError(f"Le livre du genre '{value}' n'existe pas dans les données disponibles.")
            case _:
                raise ValueError("Invalid filter type provided.")

    def addLivre(self, ISBN, titre, auteur, annee, genre): # statut is not included because, a new book is always "disponible"
        self._livres.append(Livre(ISBN, titre, auteur, annee, genre, statut=StatutLivreEnum.DISPONIBLE.value))

    def deleteLivres(self, lesIndiceDesLivreASupprimer): # supprimer a partir d'un intervalle de lignes
        lesIndiceDesLivreASupprimer = sorted(lesIndiceDesLivreASupprimer, reverse=True) # to avoid index shifting when removing items
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
        # Convert the list of Livre objects to a list of dictionaries
        self._livres = self.toJSON(self._livres)
        # Save the books to "livres.json"
        with open('data/livres.json', 'w') as file:
            dump(self._livres, file, indent=4)
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------