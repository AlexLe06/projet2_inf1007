import pandas as pd

# 1. Charger et inspecter
df = pd.read_csv("Car details v3.csv")   # adapte le nom/chemin du fichier

print(df.shape)          # (lignes, colonnes)
print(df.head())         # 5 premières lignes
print(df.dtypes)         # object = texte à nettoyer
print(df.isna().sum())   # valeurs manquantes par colonne

# Voir les valeurs possibles d'une colonne texte
for col in ["fuel", "seller_type", "transmission", "owner"]:
    print(col, df[col].unique())


# 2. name -> marque + modele  (exemple complet)
mots = df["name"].str.split()
df["marque"] = mots.str[0]
df["modele"] = mots.str[1]
df = df.drop(columns=["name"])


# 3. Garder seulement les nombres
# TODO : pour "mileage", "engine", "max_power"
# Nettoyage des colonnes "nombre + unité" (ex. "23.4 kmpl", "1248 CC", "74 bhp")
# .str.split() coupe chaque valeur aux espaces, .str[0] garde le 1er morceau (le nombre)
# pd.to_numeric convertit toute la colonne en nombres
# errors="coerce" transforme les valeurs sans nombre (ex. " bhp") en NaN au lieu de planter
df["mileage"]   = pd.to_numeric(df["mileage"].str.split().str[0],   errors="coerce")
df["engine"]    = pd.to_numeric(df["engine"].str.split().str[0],    errors="coerce")
df["max_power"] = pd.to_numeric(df["max_power"].str.split().str[0], errors="coerce")

# TODO : "torque" -> extraire le 1er nombre, puis ×9.8 si la valeur contient "kgm"
#   (ou df.drop(columns=["torque"]) si tu choisis de l'enlever)
df = df.drop(columns=["torque"]) # je drop cette info car elle est coreller a max power et engin, elle n<apporte pas beaucoup d,informaiton 
# 4. Texte -> nombres

# TODO : owner avec .map({...})  (Test Drive Car=0, First Owner=1, ...)
# TODO : transmission avec .map({"Manual": 0, "Automatic": 1})
# TODO : fuel et seller_type avec pd.get_dummies(df, columns=[...])
# TODO : marque et modele