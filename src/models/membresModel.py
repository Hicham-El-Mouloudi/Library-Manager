# standard libs
from json import load, dump
from enum import Enum
# custom imports
from models.Membre import Membre
from models.Livre import Livre, StatutLivreEnum


# ----------------------------------------------------------------------------------------
# ------------------------------------ MembreInexistantError ------------------------------------
# ----------------------------------------------------------------------------------------
# Custom exception for handling cases where a member does not exist
class MembreInexistantError(Exception):
    def __init__(self, message="Le membre n'existe pas dans les données disponibles."):
        self.message = message
        super().__init__(self.message)
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
# ------------------------------------ MembreRechercheFiltre ------------------------------------
# ----------------------------------------------------------------------------------------
# Enum to define the different filters for searching members
class MembreRechercheFiltre(Enum): # C'est pas encore utilisé !!!!!!!!
    Id = "id"
    Nom = "nom"
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

    def loadData(self):
        # Load the members from "membres.json"
        try:
            with open('data/membres.json', 'r', encoding="utf-8") as file:
                self._membres = load(file)
                self._membres = self.fromJSON(self._membres) # converting the list of dictionaries to a list of Membre objects
        except FileNotFoundError:
            self._membres = []

    def fromJSON(self, listDesDictMembres):
        # transforming a list of dictionaries to a list of Membre objects
        membres = []
        for m in listDesDictMembres:
            membres.append(
                Membre(
                    m['id'], 
                    m['nom'], 
                    [ # List of borrowed books, each represented as a Livre object
                        Livre(
                            livre["ISBN"], 
                            livre["titre"],
                            livre["auteur"],
                            livre["annee"],
                            livre["genre"],
                            livre["statut"],
                            ) for livre in m['lesLivresEmpruntes']
                    ] )
                )
        return membres

    def toJSON(self, listDesObjMembres):
        # transforming a list of Membre objects to a list of dictionaries
        return [
            {
                "id": membre.id,
                "nom": membre.nom,
                "lesLivresEmpruntes": [
                    {
                        "ISBN" : livre.ISBN,
                        "titre": livre.titre,
                        "auteur": livre.auteur,
                        "annee": livre.annee,
                        "genre": livre.genre,
                        "statut": livre.statut
                    } for livre in membre.lesLivresEmpruntes # List of borrowed books, each represented as a dictionary
                ]
            } for membre in listDesObjMembres # List of Membre objects, each represented as a dictionary
        ]

    def searchMembre(self, filter=MembreRechercheFiltre.Id, value=None): # cette fct est utilisées dans la vue empruntsView.py pour rechercher un membre par son ID ou nom.
        # Cette fonction n'est pas utilisée encore, mais elle est prête pour une utilisation future.
        match(filter):
            case MembreRechercheFiltre.Id:
                for membre in self._membres:
                    if membre.id.lower() == value.lower():
                        return membre
                raise MembreInexistantError(f"Le membre avec l'ID '{value}' n'existe pas dans les données disponibles.")
            case MembreRechercheFiltre.Nom:
                for membre in self._membres:
                    if membre.nom.lower() == value.lower():
                        return membre
                raise MembreInexistantError(f"Le membre avec le nom '{value}' n'existe pas dans les données disponibles.")
            case _:
                raise ValueError("Invalid filter type provided.")

    def addMembre(self, id, nom):
        self._membres.append(Membre(id, nom))

    def deleteMembres(self, lesIndiceDesMembresASupprimer):
        lesIndiceDesMembresASupprimer = sorted(lesIndiceDesMembresASupprimer, reverse=True)
        for index in lesIndiceDesMembresASupprimer:
            if 0 <= index < len(self._membres):
                self._membres.pop(index)
            else:
                raise IndexError(f"Index {index} is out of range for the members list.")
        return self._membres

    def listerMembres(self):
        # Return a list of members
        return self._membres

    def saveData(self):
        # Convert the list of Membre objects to a list of dictionaries
        self._membres = self.toJSON(self._membres)
        # Save the members to "membres.json"
        with open('data/membres.json', 'w', encoding="utf-8") as file:
            dump(self._membres, file, ensure_ascii=False, indent=4)
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
