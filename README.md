# Projet 2 INF1007 — de la donnée à l'application

Application qui entraîne un modèle simple sur un jeu de données, puis permet à un utilisateur de faire des prédictions avec une interface graphique.

**Équipe :** Alex · Joud Katbe

## Jeu de données
- Source : _à compléter_
- Licence : _à compléter_

## Installation et lancement
```bash
pip install -r requirements.txt
python src/main.py
```

## Tests et couverture
```bash
pytest -v
coverage run -m pytest && coverage report
```
Couverture : _à compléter_

## Structure du code
| Fichier | Rôle |
|---|---|
| `src/donnees.py` | Lecture, nettoyage, classes de variables |
| `src/modele.py` | Entraînement, évaluation, prédiction |
| `src/exceptions.py` | Exceptions personnalisées |
| `src/interface.py` | Interface graphique |
| `src/main.py` | Point d'entrée |
| `donnees/` | Jeu de données (CSV) |
| `modeles/` | Modèle sauvegardé + métadonnées JSON |

## Résultats du modèle
_Métrique et comparaison avec la référence : à compléter._

## Outil du chapitre 7
_À compléter._

## Documentation consultée
- _pandas : à compléter_
- _scikit-learn : à compléter_
- _interface graphique : à compléter_
