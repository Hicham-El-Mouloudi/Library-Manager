# standard imports
from enum import Enum
import json
import time
# custom imports
from models.livresModel import LivresModel, LivreRechercheFiltre, LivreInexistantError
from models.membresModel import MembresModel, MembreRechercheFiltre, MembreInexistantError
from models.Livre import Livre, StatutLivreEnum

# ----------------------------------------------------------------------------------------
# ------------------------------------ LivreIndisponibleError ------------------------------------
# ----------------------------------------------------------------------------------------
class LivreIndisponibleError(Exception):
    def __init__(self, message="Le livre est indisponible pour l'emprunt."):
        self.message = message
        super().__init__(self.message)
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------
# ------------------------------------ LivreDisponibleError ------------------------------------
# ----------------------------------------------------------------------------------------
class LivreDisponibleError(Exception):
    def __init__(self, message="Le livre est déjà disponible. Il ne peut pas être retourner."):
        self.message = message
        super().__init__(self.message)
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------




# ----------------------------------------------------------------------------------------
# ------------------------------------ QuotaEmpruntDepasseError ------------------------------------
# ----------------------------------------------------------------------------------------
class QuotaEmpruntDepasseError(Exception):
    def __init__(self, message="Le quota d'emprunt a été dépassé pour ce membre."):
        self.message = message
        super().__init__(self.message)
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------




# ----------------------------------------------------------------------------------------
# ------------------------------------ LibraryActionEnum ------------------------------------
# ----------------------------------------------------------------------------------------
# This enum defines the operations of borrow/return
class LibraryActionEnum(Enum):
    EMPRUNT = "emprunt"
    RETOUR = "retour"
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------




# ----------------------------------------------------------------------------------------
# ------------------------------------ EmpruntsModel ------------------------------------
# ----------------------------------------------------------------------------------------
class HistoriqueModel:
    def __init__(self, membresModel : MembresModel, livresModel: LivresModel, borrowingQuota):
        self.membresModel = membresModel
        self.livresModel = livresModel
        self.borrowingQuota = borrowingQuota  # Maximum number of books a member can borrow
        self._emprunts = None
        # 
        self.loadData()

    def loadData(self):
        # Load data from "historique.json" file
        try:
            with open("data/historique.json", "r") as file:
                data = json.load(file)
                self._emprunts = data
        except FileNotFoundError:
            self._emprunts = {}

    def saveData(self):
        # saving data in livresModel and membresModel
        self.livresModel.saveData()
        self.membresModel.saveData()
        # Save data to "historique.json" file
        with open("data/historique.json", "w") as file:
            # Write the dictionary in "historique.json"
            json.dump(self._emprunts, file, indent=4)

    def emprunterLivre(self, isbn, membreId):
        # search for the book in the books model
        try : 
            livre = self.livresModel.searchLivre(LivreRechercheFiltre.ISBN, isbn)
            # check if the book is not borrewed
            if livre.statut == StatutLivreEnum.EMPRUNTE.value :
                raise LivreIndisponibleError(f"Le livre {livre.titre} est déjà emprunté.")
            
            # check if the member exists
            try : 
                membre = self.membresModel.searchMembre(MembreRechercheFiltre.Id, membreId)
                # check if the member has not exceeded the borrowing quota
                if len(membre.livresEmpruntes) + 1 > self.borrowingQuota:
                    raise QuotaEmpruntDepasseError(f"Le membre {membre.nom} ne peut pas dépasser le quota d'emprunt de {self.borrowingQuota} livres.")
                
                # # # # ------>  Borrow the book
                livre.statut = StatutLivreEnum.EMPRUNTE.value
                # # # # ------> Add the book to the member's borrowed books list
                membre.livresEmpruntes.append(livre)
                # # # # --------------> Recording the borrow
                self.addNewRecord(livre.isbn, membre.id, LibraryActionEnum.EMPRUNT.value)

            except MembreInexistantError as e:
                raise e # the error captured will be forwarded to the caller

        except LivreInexistantError as e: 
            raise e # the error captured will be forwarded to the caller

    def retournerLivre(self, isbn, membreId):
        # search for the book in the books model
        try : 
            livre = self.livresModel.searchLivre(LivreRechercheFiltre.ISBN, isbn)
            # check if the book is borrowed
            if livre.statut == StatutLivreEnum.DISPONIBLE.value :
                raise LivreDisponibleError(f"Le livre {livre.titre} est déjà disponible. Il ne peut pas être retourné.")
            
            # check if the member exists
            try : 
                membre = self.membresModel.searchMembre(MembreRechercheFiltre.Id, membreId)
                
                # # # # ------>  Return the book
                livre.statut = StatutLivreEnum.DISPONIBLE.value
                # # # # ------> remove the book from the member's borrowed books list
                if livre in membre.livresEmpruntes:
                    membre.livresEmpruntes.remove(livre) # removing the book from the member's borrowed books list
                else:
                    raise LivreInexistantError(f"Le livre {livre.titre} n'est pas dans la liste des livres empruntés par le membre {membre.nom}.")
                # # # # --------------> Recording the return
                self.addNewRecord(livre.isbn, membre.id, LibraryActionEnum.RETOUR.value)

            except MembreInexistantError as e:
                raise e # the error captured will be forwarded to the caller

        except LivreInexistantError as e: 
            raise e # the error captured will be forwarded to the caller
    
    # This function adds a new record to the historique.json
    def addNewRecord(self, isbn, membreId, action = LibraryActionEnum.EMPRUNT.value) :
        self._emprunts[int(time.time() * 1000)] = { # int(time.time() * 1000)  is time stamp in miliseconds
            "ISBN" : isbn,
            "idMembre" : membreId,
            "action" : action
        }