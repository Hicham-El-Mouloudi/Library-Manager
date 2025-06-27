from enum import Enum

# ----------------------------------------------------------------------------------------
# ------------------------------------ LibraryActionEnum ------------------------------------
# ----------------------------------------------------------------------------------------
class LibraryActionEnum(Enum):
    EMPRUNT = "emprunt"
    RETOUR = "retour"
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------
# ------------------------------------ Emprunt ------------------------------------
# ----------------------------------------------------------------------------------------
class HistoriqueRecord:
    def __init__(self, unixTime, isbn, membreId, action = LibraryActionEnum.EMPRUNT.value) :
        self.unixTime = unixTime  # Timestamp of the action
        self.isbn = isbn            # ISBN of the book
        self.membreId = membreId    # ID of the member who performed the action
        self.action = action        # Action performed (LibraryActionEnum values)