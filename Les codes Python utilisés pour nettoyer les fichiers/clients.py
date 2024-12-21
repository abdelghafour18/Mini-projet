import pandas as pd

# Charger le fichier
file_path = 'clients.csv'
data = pd.read_csv(file_path)

# Nettoyage des colonnes
# 1. Remplacer les âges négatifs ou aberrants par NaN
import numpy as np
data['Âge'] = data['Âge'].apply(lambda x: np.nan if x <= 0 else x)

# 2. Supprimer les lignes où les informations critiques sont manquantes (par exemple, ID_Client ou Nom)
data = data.dropna(subset=['ID_Client', 'Nom'])

# 3. Remplacer les valeurs manquantes dans "Sexe" par "Inconnu"
data['Sexe'] = data['Sexe'].fillna('Inconnu')

# 4. Remplir les valeurs manquantes de "Ville" par "Non spécifié"
data['Ville'] = data['Ville'].fillna('Non spécifié')

# 5. Réinitialiser l'index après nettoyage
data = data.reset_index(drop=True)

# Sauvegarder le fichier nettoyé
cleaned_file_path = 'clients_cleaned.csv'
data.to_csv(cleaned_file_path, index=False)

print(f"Fichier nettoyé sauvegardé ici : {cleaned_file_path}")
