from enum import Enum

# ----------------------------------------------------------------------------------------
# ------------------------------------ Membre ------------------------------------
# ----------------------------------------------------------------------------------------
class Membre:
    def __init__(self, id, nom, lesLivresEmpruntes=None):
        self.id = id
        self.nom = nom
        self.lesLivresEmpruntes = lesLivresEmpruntes if lesLivresEmpruntes is not None else []

    def getValuesList(self):
        # Return a list of the member's attributes values
        return [self.id, self.nom, ', '.join([ str(livre) for livre in self.lesLivresEmpruntes ])]
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
