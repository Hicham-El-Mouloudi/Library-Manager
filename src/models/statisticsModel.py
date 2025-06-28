# standard libs
from collections import Counter # to count the number of repetitions of each element in an array
# custom libs
from src.models.livresModel import LivresModel
from src.models.membresModel import MembresModel
from src.models.historiqueModel import HistoriqueModel




# ----------------------------------------------------------------------------------------
# ------------------------------------ StatisticsModel ------------------------------------
# ----------------------------------------------------------------------------------------
class StatisticsModel :
    def __init__(self, historiqueModel : HistoriqueModel, membresModel : MembresModel, livresModel : LivresModel) : 
        self._historiqueModel = historiqueModel
        self._membresModel = membresModel
        self._livresModel = livresModel
    
    def getPieDiagrammeData(self) : 
        # getting all books
        livresList = self._livresModel.getLivresList()
        # getting all "genre" of books
        genres = [livre.genre for livre in livresList]
        return Counter(genres)

    def getHistogrammeData(self) : 
        # getting all history
        history = self._historiqueModel.getHistoriqueData()
        