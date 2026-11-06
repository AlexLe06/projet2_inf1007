"""Lecture, nettoyage des données et classes de variables."""
import os

import pandas as pd
from sklearn.model_selection import train_test_split

from exceptions import DonneeInvalideError

CIBLE = "selling_price"
COLONNES_NUMERIQUES = ["year", "km_driven", "mileage", "engine", "max_power", "seats"]
COLONNES_CATEGORIELLES = ["marque", "fuel", "seller_type", "transmission", "owner"]
KM_MAXIMUM = 1_000_000  # au-delà, le kilométrage est jugé impossible (erreur de saisie)


class Data:
    """Charge le jeu CarDekho, le nettoie et le sépare en entraînement / test."""

    def __init__(self, path: str) -> None:
        
    def _extraire_nombre(serie: pd.Series) -> pd.Series:

    def clean(self) -> pd.DataFrame:

        