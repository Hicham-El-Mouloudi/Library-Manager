if __name__ == "__main__":
    exit("Membre.py : Ce fichier ne peut pas être exécuté directement. Veuillez exécuter le fichier main.py.")

from enum import Enum

# ----------------------------------------------------------------------------------------
# ------------------------------------ Membre ------------------------------------
# ----------------------------------------------------------------------------------------
class Membre:
    def __init__(self, id, nom, livresEmpruntes=None):
        self.id = id
        self.nom = nom
        self.livresEmpruntes = livresEmpruntes if livresEmpruntes is not None else []

    def getValuesList(self):
        # Return a list of the member's attributes values
        return [self.id, self.nom, ', '.join([ str(livre) for livre in self.livresEmpruntes ])]
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
