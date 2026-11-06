# Journal d'utilisation de l'IA

| Outil | Ce que nous avons demandé | Réponse reçue | Vérification faite | Décision |
|---|---|---|---|---|
| Claude | Analyse de l'énoncé du projet 2 | Résumé des exigences et démarche proposée | Comparaison avec l'énoncé PDF | Gardé |
| Claude | Mise en place du dépôt (CI, README, structure) | Fichiers de base et premier test | Exécution de `pytest` en local et CI | _à compléter_ |
| Claude | Plan de nettoyage du jeu CarDekho | Étapes et indices par colonne (name, unités, texte → nombres, valeurs manquantes) | Inspection des colonnes avec `unique()` et `isna().sum()` | Gardé |
| Claude | Séparer `name` en marque et modèle | Code avec `.str.split()` ; option nom complet (`n=1`) ou deux mots | Lecture de `df.head()` après le découpage | Gardé : deux mots (marque + modèle de base), le reste du nom est retiré |
| Claude | Correction de notre code pour `mileage`, `engine`, `max_power` | Utiliser `.str.split().str[0]` et `pd.to_numeric(errors="coerce")` au lieu de `float()` / `int()` sur une colonne | Vérification des types (`dtypes`) et du nombre de NaN | Gardé |
| Claude | Conversion de `torque` (unités Nm et kgm) | Extraction du nombre et conversion ×9,8 des kgm avec un masque | Analyse des formats de la colonne (unités mixtes, plages de rpm) | Rejeté : colonne retirée (format incohérent, information redondante avec `engine` et `max_power`) |
| Claude | Aide pour le push Git | Vérification de la structure du dépôt et commandes `add` / `commit` / `push` | `git rev-parse --show-toplevel`, push réussi (commit `95bb0f1`) | Gardé |
| Claude | Construire la régression linéaire étape par étape | Indices par étape et corrections de notre code | Résultats comparés : MAE 175 576 et R² 0,60 contre 286 660 et 0,00 pour la référence | Gardé |
