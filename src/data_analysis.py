# src/data_analysis.py

import pandas as pd

def analyze_data(data_path):
    # Charger les données
    df = pd.read_csv(data_path)

    # Exemple d'analyse : Moyenne des valeurs ESG par catégorie
    mean_values = df.groupby('Category')['Value'].mean()
    print(mean_values)

    # Exemple d'analyse : Variance des valeurs ESG par catégorie
    var_values = df.groupby('Category')['Value'].var()
    print(var_values)

    # Autres analyses peuvent être ajoutées ici
