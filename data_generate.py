import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configurations
np.random.seed(42)  # Pour la reproductibilité
random.seed(42)

# Définir les dates
start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 12, 31)
date_range = (end_date - start_date).days

# Générer des dates aléatoires
def generate_random_dates(n):
    return [start_date + timedelta(days=random.randint(0, date_range)) for _ in range(n)]

# Générer des données
def generate_esg_data(num_entries):
    data = {
        'Date': generate_random_dates(num_entries),
        'Category': np.random.choice(['Environmental', 'Social', 'Governance'], num_entries),
        'Metric': np.random.choice(['Carbon Emissions (tonnes)', 'Water Usage (m3)', 'Waste Production (kg)', 
                                    'Employee Satisfaction (%)', 'Health & Safety Incidents (#)', 
                                    'Diversity (%)', 'Board Independence (%)', 'Executive Compensation (USD)'], num_entries),
        'Value': np.round(np.random.uniform(0, 1000, num_entries), 2)
    }
    df = pd.DataFrame(data)
    return df

# Nombre d'entrées
num_entries = 999

# Générer le DataFrame
df_esg = generate_esg_data(num_entries)

# Sauvegarder le DataFrame dans un fichier CSV
df_esg.to_csv('esg_data.csv', index=False)

print("Données ESG simulées générées et sauvegardées dans 'simulated_esg_data.csv'.")
