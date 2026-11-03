# Fiche de décisions

| Choix | Options envisagées | Choix retenu et justification | Validé par l'auxiliaire (date) |
|---|---|---|---|
| Domaine | Finance (stratégie momentum sur des actions), marché automobile | Prix des voitures d'occasion : lié à notre intérêt pour la finance (estimer une valeur de marché), avec des données tabulaires plus simples à modéliser qu'une série boursière | |
| Jeu de données | Données boursières (momentum), CarDekho « Car details v3 » (Kaggle) | CarDekho v3 : 8128 voitures, 13 colonnes (année, km, carburant, transmission, propriétaires, moteur, puissance…). Assez de lignes pour entraîner un modèle et des colonnes faciles à interpréter | |
| Cible et métrique | Cible : `selling_price`. Métriques : MAE, RMSE, R² | Cible `selling_price` (régression). MAE pour l'erreur moyenne en roupies, facile à expliquer ; R² pour la part de variation du prix expliquée. Comparaison avec une référence qui prédit toujours le prix moyen | |
| Modèle | Régression linéaire, arbre de décision, forêt aléatoire | Forêt aléatoire (`RandomForestRegressor`) : gère les relations non linéaires (ex. dépréciation selon l'année), peu sensible aux échelles des colonnes, et donne l'importance de chaque variable. La régression linéaire servira de comparaison | |
| Technologie d'interface | Tkinter, Streamlit, PyQt | _à décider_ | |