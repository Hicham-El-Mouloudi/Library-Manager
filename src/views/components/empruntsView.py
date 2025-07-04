if __name__ == "__main__":
    exit("empruntsView.py : Ce fichier ne peut pas être exécuté directement. Veuillez exécuter le fichier main.py.")

# standard imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# custom imports
from models.livresModel import LivreInexistantError
from models.membresModel import MembreInexistantError
from models.historiqueModel import LivreIndisponibleError, LivreDisponibleError, QuotaEmpruntDepasseError



class EmpruntsView:
    def __init__(self, parent, bibliotheque, livresView, membresView): 
        self.livresView = livresView
        self.membresView = membresView
        # Linking the model to the view
        self._model = bibliotheque.getHistoriqueModel()
        self._model.loadData()  # Load the data from the JSON file 'historique.json'
        # Creating the frame for the view
        self._frame = Frame(parent)
        self.initUI()

    def initUI(self):
        outerFrame = Frame(self._frame, bg="white", height=100)
        outerFrame.pack(fill='x', padx=10, pady=10)
        #-------------------------------- Borrowing books section
        # ------------------------------------------------------------------------------------------
        empruntsFrame = Frame(outerFrame, bg="white")
        empruntsFrame.pack(side="left", fill='both', expand=True, padx=10, pady=10)
        # sub-components for borrowing books
        empruntsContainerFrame = Frame(empruntsFrame, bg="white", width=400, height=200)
        empruntsContainerFrame.pack(pady=10)
        # labels and entries for borrowing books
        empruntsIsbnFrame = Frame(empruntsContainerFrame, bg="white")
        empruntsIsbnFrame.pack(pady=5, fill="both", expand=True)
        empruntsISBNLabel = ttk.Label(empruntsIsbnFrame, text="ISBN du livre à emprunter:", width=26)
        empruntsISBNLabel.pack(side="left", pady=5, fill="both", expand=True)
        empruntsISBNEntry = Entry(empruntsIsbnFrame, width=40)
        empruntsISBNEntry.pack(side="left", pady=5, fill="both", expand=True)
        #
        empruntsMemberFrame = Frame(empruntsContainerFrame, bg="white")
        empruntsMemberFrame.pack(pady=5, fill="both", expand=True)
        empruntsMembreIdLabel = ttk.Label(empruntsMemberFrame, text="ID du membre:", width=26)
        empruntsMembreIdLabel.pack(side="left", pady=5, fill="both", expand=True)
        empruntsMembreIdEntry = Entry(empruntsMemberFrame, width=40)
        empruntsMembreIdEntry.pack(side="left", pady=5, fill="both", expand=True)
        # button to borrow a book
        empruntsButton = ttk.Button(empruntsFrame, text="Emprunter le livre", command=lambda: self.validerEmprunt(empruntsISBNEntry.get(), empruntsMembreIdEntry.get()))
        empruntsButton.pack(pady=5)

        # --------------------------------------Returnning books section
        # ------------------------------------------------------------------------------------------
        retourFrame = Frame(outerFrame, bg="white")
        retourFrame.pack(side="left", fill='both', expand=True, padx=10, pady=10)
        # sub-components for returning books
        retourContainerFrame = Frame(retourFrame, bg="white", width=400, height=200)
        retourContainerFrame.pack(pady=10)
        # labels and entries for returning books
        retourIsbnFrame = Frame(retourContainerFrame, bg="white")
        retourIsbnFrame.pack(pady=5, fill="both", expand=True)
        retourISBNLabel = ttk.Label(retourIsbnFrame, text="ISBN du livre à retourner:", width=26)
        retourISBNLabel.pack(side="left", pady=5, fill="both", expand=True)
        retourISBNEntry = Entry(retourIsbnFrame, width=40)
        retourISBNEntry.pack(side="left", pady=5, fill="both", expand=True)
        #
        retourMemberFrame = Frame(retourContainerFrame, bg="white")
        retourMemberFrame.pack(pady=5, fill="both", expand=True)
        retourMembreIdLabel = ttk.Label(retourMemberFrame, text="ID du membre:", width=26)
        retourMembreIdLabel.pack(side="left", pady=5, fill="both", expand=True)
        retourMembreIdEntry = Entry(retourMemberFrame, width=40)
        retourMembreIdEntry.pack(side="left", pady=5, fill="both", expand=True)
        # button to return a book
        retourButton = ttk.Button(retourFrame, text="Retourner le livre", command=lambda: self.validerRetour(retourISBNEntry.get(), retourMembreIdEntry.get()))
        retourButton.pack(pady=5)

        #-------------------- Save button
        # ------------------------------------------------------------------------------------------
        saveButton = ttk.Button(self._frame, text=" Enregistrer ", command=self.saveData)
        saveButton.pack(pady=10)

        return self._frame

    def getUI(self):
        return self._frame

    def validerEmprunt(self, isbn, membreId) : 
        try : 
            self._model.emprunterLivre(isbn, membreId)
            messagebox.showinfo("Succès", "Livre emprunté avec succès.")
            # update ui of books and members
            self.livresView.afficherLivres()
            self.membresView.afficherMembres()
        except LivreInexistantError as e : 
            messagebox.showerror("Erreur", str(e))
        except MembreInexistantError as e :
            messagebox.showerror("Erreur", str(e))
        except LivreIndisponibleError as e :
            messagebox.showerror("Erreur", str(e))
        except QuotaEmpruntDepasseError as e :
            messagebox.showerror("Erreur", str(e))
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur inattendue est survenue")
    def validerRetour(self, isbn, membreId) :
        try : 
            self._model.retournerLivre(isbn, membreId)
            messagebox.showinfo("Succès", "Livre retourné avec succès.")
            # update ui of books and members
            self.livresView.afficherLivres()
            self.membresView.afficherMembres()
        except LivreInexistantError as e : 
            messagebox.showerror("Erreur", str(e))
        except MembreInexistantError as e :
            messagebox.showerror("Erreur", str(e))
        except LivreDisponibleError as e :
            messagebox.showerror("Erreur", str(e))
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur inattendue est survenue")

    def saveData(self):
        self._model.saveData()
        messagebox.showinfo("Succès", "Les emprunts ont été enregistrés avec succès.")