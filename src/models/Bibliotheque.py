from src.models.Livre import Livre
from src.models.livresModel import LivresModel



class Bibliotheque : 
    def __init__(self) : 
        # Initialize books data
        self._livres = LivresModel()

    def getLivresModel(self):
        # Return the LivresModel instance
        return self._livres