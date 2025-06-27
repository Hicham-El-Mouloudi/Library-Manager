

# ----------------------------------------------------------------------------------------
# ------------------------------------ EmpruntsModel ------------------------------------
# ----------------------------------------------------------------------------------------
class LivreIndisponibleError(Exception):
    def __init__(self, message="Le livre est indisponible pour l'emprunt."):
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
# ------------------------------------ EmpruntsModel ------------------------------------
# ----------------------------------------------------------------------------------------
class EmpruntsModel:
    def __init__(self, membresModel, livresModel):
        self.membresModel = membresModel
        self.livresModel = livresModel
        self.emprunts = []

    def toJSON(self, listDesObjHistorique):
        # transforming a list of HistoriqueRecord objects to a list of dictionaries
        return [ record.__dict__ for record in listDesObjHistorique ]
    
    def fromJSON(self, listDesDictHistorique):
        # transforming a list of dictionaries to a list of HistoriqueRecord objects
        return [ HistoriqueRecord(record["unixTime"], record["isbn"], record["membreId"], record["action"]) for record in listDesDictHistorique ]

    def loadData(self):
        # Load data from "historique.json" file
        try:
            with open("data/historique.json", "r") as file:
                data = json.load(file)
                self.emprunts = self.fromJSON(data)
        except FileNotFoundError:
            self.emprunts = []

    def saveData(self):
        pass

    def emprunterLivre(self, isbn, membreId):
        pass

    def retournerLivre(self, isbn, membreId):
        pass