# standard libs
from json import load, dump
from enum import Enum
# custom imports
from models.Membre import Membre


# ----------------------------------------------------------------------------------------
# ------------------------------------ MembreRechercheFiltre ------------------------------------
# ----------------------------------------------------------------------------------------
# Enum to define the different filters for searching members
class MembreRechercheFiltre(Enum): # C'est pas encore utilisé !!!!!!!!
    Id = "id"
    Nom = "nom"
    # TODO: Add more filters if needed
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------




# ----------------------------------------------------------------------------------------
# ------------------------------------ MembresModel ------------------------------------
# ----------------------------------------------------------------------------------------
class MembresModel:
    def __init__(self):
        self._membres = None
        self.loadData()  # Load members from "membres.json"

    def searchMembre(self, filter=MembreRechercheFiltre.Id, value=None):
        # TODO: Implement search logic for members based on filter
        pass

    def loadData(self):
        # Load the members from "membres.json"
        try:
            with open('data/membres.json', 'r', encoding="utf-8") as file:  # utf-8 for special characters
                self._membres = load(file)
        except FileNotFoundError:
            self._membres = []

    def addMembre(self, membre):
        self._membres.append(
            {
                "id": membre.id,
                "nom": membre.nom,
                "emprunts": [] # the "emrunts" are not added when adding a new member
            }
        )

    def deleteMembre(self, lesIndiceDesLivreASupprimer):
        lesIndiceDesLivreASupprimer = sorted(lesIndiceDesLivreASupprimer, reverse=True)
        for index in lesIndiceDesLivreASupprimer:
            if 0 <= index < len(self._membres):
                self._membres.pop(index)
            else:
                raise IndexError(f"Index {index} is out of range for the members list.")
        return self._membres

    def listerMembres(self):
        # Return a list of members
        return self._membres

    def saveData(self):
        # Save the members to "membres.json"
        with open('data/membres.json', 'w', encoding="utf-8") as file:
            dump(self._membres, file, ensure_ascii=False, indent=4)
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
