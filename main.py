from src.data_preprocessing import preprocess_data
from src.data_analysis import analyze_data


def main():
    # Prétraitement des données
    preprocess_data('data/raw/esg_data.csv', 'data/processed/processed_data.csv')

    # Analyse des données
    analyze_data('data/processed/processed_data.csv')


if __name__ == "__main__":
    main()
