

# ----------------------------------------------------------------------------------------
# ------------------------------------ Livre ------------------------------------
# ----------------------------------------------------------------------------------------
class Livre : 
    def __init__(self, isbn, titre, auteur, annee, genre, statut) : 
        # Initialize a book with its attributes
        self._isbn = isbn
        self._titre = titre
        self._auteur = auteur
        self._annee = annee
        self._genre = genre
        self._statut = statut # disponible ou emprunté

    # getters and setters for the attributes
    @property
    def isbn(self):
        return self._isbn
    @isbn.setter
    def isbn(self, value):
        self._isbn = value

    @property
    def titre(self):
        return self._titre
    @titre.setter
    def titre(self, value):
        self._titre = value
    
    @property
    def auteur(self):
        return self._auteur
    @auteur.setter
    def auteur(self, value):
        self._auteur = value
    
    @property
    def annee(self):
        return self._annee
    @annee.setter
    def annee(self, value):
        self._annee = value
    
    @property
    def genre(self):
        return self._genre
    @genre.setter
    def genre(self, value):
        self._genre = value
    
    @property
    def statut(self):
        return self._statut
    @statut.setter
    def statut(self, value):
        self._statut = value
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------