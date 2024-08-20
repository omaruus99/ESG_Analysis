import pytest
import pandas as pd
from src.data_preprocessing import preprocess_data

def test_preprocess_data():
    preprocess_data('/Users/omarhaddad/Desktop/ESG_analysis/data/raw/esg_data.csv', '/Users/omarhaddad/Desktop/ESG_analysis/data/processed/processed_esg_data.csv')

    df = pd.read_csv('/Users/omarhaddad/Desktop/ESG_analysis/data/processed/processed_esg_data.csv')
    assert df.shape[0] > 0  # Vérifie qu'il y a des données après traitement
    assert df['Date'].dtype == 'datetime64[ns]'  # Vérifie que la colonne Date est en datetime
    assert df['Value'].notnull().all()  # Vérifie qu'il n'y a pas de valeurs manquantes dans la colonne Value
