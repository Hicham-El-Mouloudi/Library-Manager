# Système de Gestion de Bibliothèque

**Auteur :** Hicham El Mouloudi

## Description

Cette application est un système complet de gestion de bibliothèque développé en Python 3.12.5. Elle propose une interface graphique moderne avec Tkinter, la gestion des livres et des membres, le suivi des emprunts/retours, la persistance des données au format JSON, et la visualisation de statistiques à l'aide de Matplotlib.

L'application suit une **architecture Modèle-Vue (MV)** pour séparer les responsabilités et faciliter la maintenance.

- **Modèle** : (`src/models/*`) gèrent les données, la logique métier et les fichiers JSON.
- **Vue** : (`src/views/*`) s'occupe de l'interface Tkinter, capte les entrées et affiche les retours.
- **Bibliotheque** : coordonne les modèles et les vues, applique les règles et quotas.

Cette structure rend le code modulaire, testable et évolutif.

## Fonctionnalités

* **Gestion des livres** : ajouter, supprimer et lister les livres.
* **Gestion des membres** : enregistrer, supprimer et lister les membres.
* **Emprunts et retours** : emprunter et retourner des livres, gérer les quotas et l'historique des emprunts.
* **Statistiques visuelles** :

  * Diagramme circulaire de répartition des livres par genre.
  * Histogramme des auteurs les plus empruntés (livres empruntés le plus souvent).
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
python src/main.py
```

> **Important :** Ne pas exécuter directement les autres fichiers (modèles ou vues) sous peine d'obtenir un message d'erreur volontaire.

## Exemples d'utilisation

* **Ajouter un livre** : onglet "Livres" → remplir les champs → cliquer sur "Ajouter".
* **Supprimer un ou plusieurs membres** : onglet "Membres" → sélectionner les membre → cliquer sur "Supprimer".
* **Emprunter un livre** : onglet "Emprunts" → saisir l'ISBN et l'ID du membre → cliquer sur "Emprunter le livre".
* **Visualiser les statistiques** : onglet "Statistiques" → les graphiques s'affichent automatiquement.
> **Note :** Les statistiques seront actualisées lors du redémarrage de l'application.

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

> **Note :** L'application est fournie avec des données de test situées dans le répertoire `/data`.  
> Vous pouvez les supprimer directement depuis l'application (et non en modifiant les fichiers) pour démarrer avec vos propres données.

## Documentation en ligne

La documentation complète du projet est disponible à l’adresse suivante :

👉 [https://hicham-el-mouloudi.github.io/Projects-Documentations/](https://hicham-el-mouloudi.github.io/Projects-Documentations/)

## Conseils

* Ne modifiez pas les fichiers JSON manuellement.
* Utilisez les boutons d'enregistrement pour sauvegarder vos modifications.
* Si les graphiques ne s'affichent pas, vérifiez l'installation de Matplotlib.