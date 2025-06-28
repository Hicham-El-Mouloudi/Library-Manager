# standard libs
from collections import Counter # to count the number of repetitions of each element in an array
from datetime import datetime, timedelta
import math
# custom libs
from src.models.livresModel import LivresModel, LivreRechercheFiltre
from src.models.Livre import Livre
from src.models.membresModel import MembresModel
from src.models.historiqueModel import HistoriqueModel, LibraryActionEnum




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
        return Counter(genres).keys(), Counter(genres).values()

    def getHistogrammeData(self) : 
        # getting all history
        historyRecords = self._historiqueModel.getHistoriqueData()
        # list of all ISBN that correspond to "emprunt" action
        lesISBN = [historyRecord["ISBN"] for historyRecord in historyRecords.values() if historyRecord["action"] == LibraryActionEnum.EMPRUNT.value]
        # replace each "ISBN" with its "Author"
        lesAuteurs = []
        for isbn in lesISBN : 
            try : 
                lesAuteurs.append( self._livresModel.searchLivre(LivreRechercheFiltre.ISBN, isbn).auteur )
            except Exception as e : 
                continue # on compte seulemnt les livres valable
        # Calculating the number of oocurences of each authr and reurn top 10
        lesAuteursTop10 = Counter(lesAuteurs).most_common(10) # this is a list of tuples

        # the first list returned has authors names, the second how many borrowed book
        return [ element[0] for element in lesAuteursTop10 ], [ element[1] for element in lesAuteursTop10]

    def getTimeDiagrammeData(self) : 
        # getting all history
        historyRecords = self._historiqueModel.getHistoriqueData()
        historyRecordsTimeKeys = historyRecords.keys()
        historyRecordsActions = [ historyRecord["action"] for historyRecord in historyRecords.values() ]
        # fixing time range
        currentTime = int(datetime.now().timestamp() * 1000) # current unix timestamp in MILLISECONDS !!!
        thirtyDaysAgo = int((currentTime - timedelta(days=30)).timestamp() * 1000 )# unix timestamp for 30 days in MILLISECONDS !!!!
        # creating a zeros array with 30 elements
        data = [0 for i in range(30)] # each element contains the number of emprunts, in that day

        # starting from 'thirtyDaysAgo' , each record in this intervalle, we add 1 in the corresponding day (array elemnt)
        for time, action in zip(historyRecordsTimeKeys, historyRecordsActions) : 
            # NOTE : Here "time" is a unix timestamp in MILLISECONDS !!! used as id for each record
            if int(time) >= thirtyDaysAgo : # Check if the record is concerned 
                # selecting action = "emprunt" -> LibraryActionEnum.EMPRUNT
                if action == LibraryActionEnum.EMPRUNT.value : 

                    # Here we will find the corresponding day of the record -> the index of the day
                    index = math.floor(time / 86400000) # 86400000 is number of milli-seconds per day
                    # add to data
                    data[index] += 1
        return data




        