from src.models.Livre import Livre
from src.models.livresModel import LivresModel
from src.models.membresModel import MembresModel


if __name__ == "__main__":
    exit("Bibliotheque.py : Ce fichier ne peut pas être exécuté directement. Veuillez exécuter le fichier main.py.")

class Bibliotheque : 
    def __init__(self) : 
        # Initialize books data
        self._livres = LivresModel()
        self._membres = MembresModel()

    def getLivresModel(self):
        # Return the LivresModel instance
        return self._livres

    def getMembresModel(self):
        # Return the MembresModel instance
        return self._membres