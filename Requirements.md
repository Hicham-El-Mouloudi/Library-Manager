# Requirements techniques :

## Environnement
- Python 3.x

## Bibliothèques requises
- `matplotlib` : visualisation
- `json` : sauvegarde/chargement
- `tkinter` : interface graphique

## Architecture
- Programmation orientée objet (POO)
- Gestion des exceptions (avec exceptions personnalisées)
- Persistance des données : fichiers `.json`



# 🧩 Requirements fonctionnels :

## 1. Gestion des Livres
- Ajouter/supprimer un livre (ISBN, titre, auteur, année, genre, statut)
- Lister tous les livres
- Rechercher un livre
- Souvegarder l'état des livres dans un fichier `.json`

## 2. Gestion des Membres
- Enregistrer un membre (ID, nom)
- Associer des livres empruntés à un membre
- Vérifier les quotas d'emprunt

## 3. Emprunts et Retours
- Emprunter un livre (statut, quota)
- Retourner un livre
- Historique des emprunts/retours (fichier .json)

## 4. Validation et Gestion des Erreurs
- Saisie utilisateur vérifiée
- Exceptions personnalisées :
  - `LivreIndisponibleError`
  - `QuotaEmpruntDepasseError`
  - `MembreInexistantError`
  - `LivreInexistantError`

## 5. Tableau de bord statistique (Matplotlib)
- Diagramme circulaire : % de livres par genre
- Histogramme : Top 10 auteurs
- Courbe temporelle : activité des 30 derniers jours

## 6. Interface utilisateur
- Interface graphique avec `tkinter`
  - Quatre menu principal avec options :
    - Gestion des livres
    - Gestion des membres
    - Emprunts/retours
    - Statistiques