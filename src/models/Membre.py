from enum import Enum

# ----------------------------------------------------------------------------------------
# ------------------------------------ Membre ------------------------------------
# ----------------------------------------------------------------------------------------
class Membre:
    def __init__(self, id, nom, lesLivresEmpruntes=None):
        self.id = id
        self.nom = nom
        self.lesLivresEmpruntes = lesLivresEmpruntes if lesLivresEmpruntes is not None else []
    
    # def __str__(self): # This method is used when displaying each member along with the books he has borrowed
    #     # Return a string representation of the member
    #     return f"nom : {self.nom}, lesLivresEmpruntes={self.lesLivresEmpruntes})"

    def getValuesList(self):
        # Return a list of the member's attributes values
        return [self.id, self.nom, '\n'.join([ str(livre) for livre in self.lesLivresEmpruntes ])]
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
