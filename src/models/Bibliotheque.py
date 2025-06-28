from models.Livre import Livre
from models.livresModel import LivresModel
from models.membresModel import MembresModel
from models.historiqueModel import HistoriqueModel
from models.statisticsModel import StatisticsModel


if __name__ == "__main__":
    exit("Bibliotheque.py : Ce fichier ne peut pas être exécuté directement. Veuillez exécuter le fichier main.py.")

class Bibliotheque : 
    def __init__(self, empruntsQuota=3): 
        # Initialize books data
        self._empruntsQuota = empruntsQuota # Maximum number of books a member can borrow
        self._livres = LivresModel()
        self._membres = MembresModel()
        self._historique = HistoriqueModel(self._membres, self._livres, self._empruntsQuota)
        self._statistics = StatisticsModel(self._historique, self._membres, self._livres)

    def getLivresModel(self):
        # Return the LivresModel instance
        return self._livres

    def getMembresModel(self):
        # Return the MembresModel instance
        return self._membres

    def getHistoriqueModel(self):
        # Return the HistoriqueModel instance
        return self._historique

    def getStatisticsModel(self) : 
        # Return the StatisticsModel instance
        return self._statistics