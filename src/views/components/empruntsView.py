from tkinter import *

if __name__ == "__main__":
    exit("empruntsView.py : Ce fichier ne peut pas être exécuté directement. Veuillez exécuter le fichier main.py.")

class EmpruntsView:
    def __init__(self, parent, bibliotheque): 
        # Linking the model to the view
        self._model = bibliotheque.getHistoriqueModel()
        # Creating the frame for the view
        self._frame = Frame(parent)
        self.initUI()

    def initUI(self):
        #-------------------------------- Borrowing books section
        # ------------------------------------------------------------------------------------------
        empruntsFrame = Frame(self._frame, bg="lightblue")
        empruntsFrame.pack(side="left", fill='both', expand=True, padx=10, pady=10)
        # sub-components for borrowing books
        empruntsContainerFrame = Frame(empruntsFrame, bg="lightyellow", width=400, height=200)
        empruntsContainerFrame.pack(pady=10)
        # labels and entries for borrowing books
        empruntsIsbnFrame = Frame(empruntsContainerFrame, bg="lightblue")
        empruntsIsbnFrame.pack(pady=5, fill="both", expand=True)
        empruntsISBNLabel = Label(empruntsIsbnFrame, text="ISBN du livre à emprunter:", width=26)
        empruntsISBNLabel.pack(side="left", pady=5, fill="both", expand=True)
        empruntsISBNEntry = Entry(empruntsIsbnFrame, width=40)
        empruntsISBNEntry.pack(side="left", pady=5, fill="both", expand=True)
        #
        empruntsMemberFrame = Frame(empruntsContainerFrame, bg="lightblue")
        empruntsMemberFrame.pack(pady=5, fill="both", expand=True)
        empruntsMembreIdLabel = Label(empruntsMemberFrame, text="ID du membre:", width=26)
        empruntsMembreIdLabel.pack(side="left", pady=5, fill="both", expand=True)
        empruntsMembreIdEntry = Entry(empruntsMemberFrame, width=40)
        empruntsMembreIdEntry.pack(side="left", pady=5, fill="both", expand=True)
        # button to borrow a book
        empruntsButton = Button(empruntsFrame, text="Emprunter le livre", command=lambda: self._model.emprunterLivre(empruntsISBNEntry.get(), empruntsMembreIdEntry.get()))
        empruntsButton.pack(pady=5)

        # --------------------------------------Returnning books section
        # ------------------------------------------------------------------------------------------
        retourFrame = Frame(self._frame, bg="lightgreen")
        retourFrame.pack(side="left", fill='both', expand=True, padx=10, pady=10)
        return self._frame

    def getUI(self):
        return self._frame