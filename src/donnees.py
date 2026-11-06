"""Lecture, nettoyage des données et classes de variables (à venir)."""
import pandas as pd

class Data:

    def __init__(self, path, annee_ref=2026):
        self._path = path
        self._annee_ref = annee_ref
        self._df = pd.read_csv(path)

    def inspecter(self):
        pass

    def clean(self):
        pass

    def split(self):
        pass