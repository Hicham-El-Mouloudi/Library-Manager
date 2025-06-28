# Système de Gestion de Bibliothèque

**Auteur :** Hicham El Mouloudi

## Description

Cette application est un système complet de gestion de bibliothèque développé en Python 3.12.5. Elle propose une interface graphique moderne avec Tkinter, la gestion des livres et des membres, le suivi des emprunts/retours, la persistance des données au format JSON, et la visualisation de statistiques à l'aide de Matplotlib.

## Fonctionnalités

* **Gestion des livres** : ajouter, supprimer, rechercher et lister les livres.
* **Gestion des membres** : enregistrer, supprimer, rechercher et lister les membres.
* **Emprunts et retours** : emprunter et retourner des livres, gérer les quotas et l'historique des emprunts.
* **Statistiques visuelles** :

  * Diagramme circulaire de répartition des livres par genre.
  * Histogramme des auteurs les plus empruntés.
  * Courbe d'activité des emprunts sur les 30 derniers jours.
* **Persistance des données** : stockage des informations dans des fichiers JSON.
* **Interface intuitive** : navigation via des onglets.
* **Gestion des erreurs** : messages clairs et robustesse de l'application.

## Installation

### Prérequis

* Python **3.12.5**
* pip

### Dépendances

```bash
pip install matplotlib
```

## Lancement de l'application

Exécute uniquement le fichier `main.py` pour démarrer l'application :

```bash
python main.py
```

> **Important :** Ne pas exécuter directement les autres fichiers (modèles ou vues) sous peine d'obtenir un message d'erreur volontaire.

## Exemples d'utilisation

* **Ajouter un livre** : onglet "Livres" → remplir les champs → cliquer sur "Ajouter Un Livre".
* **Supprimer un membre** : onglet "Membres" → sélectionner un membre → cliquer sur "Supprimer".
* **Emprunter un livre** : onglet "Emprunts" → saisir l'ISBN et l'ID du membre → cliquer sur "Emprunter le livre".
* **Visualiser les statistiques** : onglet "Statistiques" → les graphiques s'affichent automatiquement.

## Structure du projet

```
src/
  main.py
  models/
    ...
  views/
    components/
      ...
data/
  livres.json
  membres.json
  historique.json
```

## Conseils

* Ne modifiez pas les fichiers JSON manuellement.
* Utilisez les boutons d'enregistrement pour sauvegarder vos modifications.
* Si les graphiques ne s'affichent pas, vérifiez l'installation de Matplotlib.