import os
import json
import pandas as pd

# Dossier du script : le CSV est trouvé peu importe d'où on lance le programme
dossier = os.path.dirname(os.path.abspath(__file__))


# 1. Charger et inspecter le jeu de données
df = pd.read_csv(os.path.join(dossier, "Car details v3.csv"))   # lecture du fichier CSV

print(df.shape)          # nombre de lignes et de colonnes
print(df.head())         # aperçu des 5 premières lignes
print(df.dtypes)         # type de chaque colonne (object = texte à nettoyer)
print(df.isna().sum())   # nombre de valeurs manquantes par colonne

# Afficher les valeurs possibles des colonnes texte (pour écrire les correspondances)
for col in ["fuel", "seller_type", "transmission", "owner"]:
    print(col, df[col].unique())


# 2. Séparer "name" en marque (1er mot) et modèle (2e mot), puis supprimer "name"
mots = df["name"].str.split()
df["marque"] = mots.str[0]
df["modele"] = mots.str[1]
df = df.drop(columns=["name"])


# 3. Garder seulement les nombres dans les colonnes "nombre + unité" (ex. "23.4 kmpl", "1248 CC", "74 bhp")
# .str.split().str[0] garde le 1er morceau de chaque valeur, pd.to_numeric le convertit en nombre
# errors="coerce" transforme les valeurs sans nombre (ex. " bhp") en NaN au lieu de planter
df["mileage"]   = pd.to_numeric(df["mileage"].str.split().str[0],   errors="coerce")
df["engine"]    = pd.to_numeric(df["engine"].str.split().str[0],    errors="coerce")
df["max_power"] = pd.to_numeric(df["max_power"].str.split().str[0], errors="coerce")

# Suppression de "torque" : format incohérent (Nm, kgm, plages de rpm)
# et information déjà couverte par "engine" et "max_power"
df = df.drop(columns=["torque"])


# 4. Convertir les colonnes texte en nombres
# owner est ordonné : on remplace chaque catégorie par son rang (0 = voiture d'essai, 1 = 1er propriétaire, ...)
correspondance_owner = {"Test Drive Car": 0, "First Owner": 1, "Second Owner": 2, "Third Owner": 3, "Fourth & Above Owner": 4}
df["owner"] = df["owner"].map(correspondance_owner)

# transmission n'a que deux valeurs : manuelle = 0, automatique = 1
correspondance_transmission = {"Manual": 0, "Automatic": 1}
df["transmission"] = df["transmission"].map(correspondance_transmission)

# fuel et seller_type n'ont pas d'ordre : une colonne 0/1 par valeur (one-hot)
df = pd.get_dummies(df, columns=["fuel", "seller_type"], dtype=int)

# marque et modele : chaque nom devient un numéro (ordre alphabétique)
# 32 marques et 207 modèles : trop de valeurs pour get_dummies, un code par catégorie suffit pour une forêt aléatoire
# On garde la correspondance nom -> numéro pour que l'interface retrouve le même code
codes = {}
for col in ["marque", "modele"]:
    categories = df[col].astype("category").cat.categories
    codes[col] = {nom: i for i, nom in enumerate(categories)}
    df[col] = df[col].astype("category").cat.codes


# 5. Supprimer les lignes en double (mêmes valeurs dans toutes les colonnes)
df = df.drop_duplicates()

# Supprimer les lignes avec des valeurs manquantes (environ 3 % des lignes, presque toujours les mêmes)
df = df.dropna()

# Après dropna, engine et seats n'ont plus de NaN : on peut les remettre en entiers
df["engine"] = df["engine"].astype(int)
df["seats"] = df["seats"].astype(int)


# 6. Vérification finale
print(df.shape)                       # nombre de lignes restantes
print(df.dtypes)                      # plus aucune colonne "object"
print(df.isna().sum().sum())          # doit afficher 0


# 7. Sauvegarde
# Jeu nettoyé, utilisé ensuite pour entraîner le modèle
df.to_csv(os.path.join(dossier, "voitures_nettoyees.csv"), index=False)

# Correspondances nom -> code de marque et modele, utilisées par l'interface
with open(os.path.join(dossier, "codes_categories.json"), "w", encoding="utf-8") as f:
    json.dump(codes, f, ensure_ascii=False, indent=2)