import pandas as pd

def preprocess_data(input_path, output_path):
    # Charger les données
    df = pd.read_csv(input_path)

    # Convertir la colonne Date en datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Nettoyer les valeurs manquantes ou incorrectes
    df = df.dropna()
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
    df = df.dropna()

    # Sauvegarder les données traitées
    df.to_csv(output_path, index=False)

# Définir les chemins des fichiers
input_path = "/Users/omarhaddad/Desktop/ESG_analysis/data/raw/esg_data.csv"
output_path = "/Users/omarhaddad/Desktop/ESG_analysis/data/processed/processed_esg_data.csv"

# Appeler la fonction de prétraitement
preprocess_data(input_path, output_path)