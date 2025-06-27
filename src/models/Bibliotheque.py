from src.models.Livre import Livre
from src.models.livresModel import LivresModel
from src.models.membresModel import MembresModel
from src.models.historiqueModel import HistoriqueModel


if __name__ == "__main__":
    exit("Bibliotheque.py : Ce fichier ne peut pas être exécuté directement. Veuillez exécuter le fichier main.py.")

class Bibliotheque : 
    def __init__(self, empruntsQuota=3): 
        # Initialize books data
        self._empruntsQuota = empruntsQuota # Maximum number of books a member can borrow
        self._livres = LivresModel()
        self._membres = MembresModel()
        self._historique = HistoriqueModel(self._membres, self._livres, self._empruntsQuota)

    def getLivresModel(self):
        # Return the LivresModel instance
        return self._livres

    def getMembresModel(self):
        # Return the MembresModel instance
        return self._membres

    def getHistoriqueModel(self):
        # Return the HistoriqueModel instance
        return self._historique