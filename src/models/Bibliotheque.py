from src.models.Livre import Livre
from src.models.livresModel import LivresModel


if __name__ == "__main__":
    exit("Bibliotheque.py : Ce fichier ne peut pas être exécuté directement. Veuillez exécuter le fichier main.py.")

class Bibliotheque : 
    def __init__(self) : 
        # Initialize books data
        self._livres = LivresModel()

    def getLivresModel(self):
        # Return the LivresModel instance
        return self._livres