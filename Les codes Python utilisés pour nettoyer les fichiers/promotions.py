import pandas as pd
from datetime import datetime

# Charger le fichier
file_path = 'promotions.csv'
data = pd.read_csv(file_path)

# Nettoyage des colonnes
# 1. Remplacer les valeurs manquantes dans "Réduction (%)" par 0 (aucune réduction)
data['Réduction (%)'] = data['Réduction (%)'].fillna(0)

# 2. Vérifier la cohérence des dates
# Convertir les colonnes en type datetime
data['Début_Validité'] = pd.to_datetime(data['Début_Validité'], errors='coerce')
data['Fin_Validité'] = pd.to_datetime(data['Fin_Validité'], errors='coerce')

# Supprimer les lignes où "Fin_Validité" est antérieure à "Début_Validité"
data = data[data['Fin_Validité'] >= data['Début_Validité']]

# 3. Supprimer les lignes avec des valeurs critiques manquantes (ID_Promotion, ID_Produit)
data = data.dropna(subset=['ID_Promotion', 'ID_Produit'])

# 4. Réinitialiser l'index après nettoyage
data = data.reset_index(drop=True)

# Sauvegarder le fichier nettoyé
cleaned_file_path = 'promotions_cleaned.csv'
data.to_csv(cleaned_file_path, index=False)

print(f"Fichier nettoyé sauvegardé ici : {cleaned_file_path}")
