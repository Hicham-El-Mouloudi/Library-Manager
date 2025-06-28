# standard libs
from collections import Counter # to count the number of repetitions of each element in an array
# custom libs
from src.models.livresModel import LivresModel, LivreRechercheFiltre
from src.models.Livre import Livre
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
        historyRecords = self._historiqueModel.getHistoriqueData()
        # list of all ISBN
        lesISBN = [historyRecord["ISBN"] for historyRecord in historyRecords.values()]
        # replace each "ISBN" with its "Author"
        lesAuteurs = []
        for isbn in lesISBN : 
            try : 
                lesAuteurs.append( self._livresModel.searchLivre(LivreRechercheFiltre.ISBN, isbn).auteur )
            except Exception as e : 
                continue # on compte seulemnt les livres valable
        # Calculating the number of oocurences of each authr and reurn top 10
        lesAuteursTop10 = Counter(lesAuteurs).most_common(10) # this is a list of tuples
        
        return lesAuteursTop10
        