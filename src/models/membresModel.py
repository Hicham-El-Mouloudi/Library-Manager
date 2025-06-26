# standard libs
from json import load, dump
# custom imports
from models.Membre import Membre







# ----------------------------------------------------------------------------------------
# ------------------------------------ MembresModel ------------------------------------
# ----------------------------------------------------------------------------------------
class MembresModel:
    def __init__(self):
        self._membres = None
        self.loadData()  # Load members from "membres.json"

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

    def deleteMembre(self, membre):
        # TODO: Delete a member from the list
        pass

    def listerMembres(self):
        # TODO: Return a list of all members
        pass

    def saveData(self):
        # TODO: Save the members to "membres.json"
        pass
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
