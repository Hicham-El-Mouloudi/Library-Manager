from enum import Enum

# ----------------------------------------------------------------------------------------
# ------------------------------------ Enum StatutLivre ------------------------------------
# ----------------------------------------------------------------------------------------
class StatutLivreEnum(Enum):
    DISPONIBLE = "disponible"
    EMPRUNTE = "emprunté"
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------
# ------------------------------------ Livre ------------------------------------
# ----------------------------------------------------------------------------------------
class Livre : 
    def __init__(self, isbn, titre, auteur, annee, genre, statut = StatutLivreEnum.DISPONIBLE.value) : 
        # Initialize a book with its attributes
        self.ISBN = isbn
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.genre = genre
        self.statut = statut # disponible ou emprunté
    
    def __str__(self): # This method is used to when printing the list of books borrowed by a member
        # Return a string representation of the book
        return f"- Titre: {self.titre}"

    def getValuesList(self):
        # Return a list of the book's attributes values
        return [self.ISBN, self.titre, self.auteur, self.annee, self.genre, self.statut]
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------