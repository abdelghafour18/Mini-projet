import pandas as pd
import numpy as np

# Charger les données avec un encodage approprié
try:
    ventes = pd.read_csv('ventes.csv', encoding='utf-8')  # Essaie utf-8
except UnicodeDecodeError:
    ventes = pd.read_csv('ventes.csv', encoding='latin-1')  # Essaie latin-1 si utf-8 échoue

# Afficher les colonnes pour vérifier leur nom
print("Colonnes disponibles :", ventes.columns)

# Renommer la colonne si elle est mal encodée
if 'QuantitÃ©' in ventes.columns:
    ventes.rename(columns={'QuantitÃ©': 'Quantité'}, inplace=True)

# Nettoyer les dates : Convertir en format datetime et supprimer les dates invalides
ventes['Date_Vente'] = pd.to_datetime(ventes['Date_Vente'], errors='coerce')  # 'coerce' remplace les erreurs par NaT
ventes = ventes.dropna(subset=['Date_Vente'])  # Supprimer les lignes avec dates invalides

# Nettoyer les quantités : Remplacer les valeurs négatives ou NaN par 0
if 'Quantité' in ventes.columns:
    ventes['Quantité'] = ventes['Quantité'].fillna(0)  # Remplir les valeurs manquantes par 0
    ventes['Quantité'] = ventes['Quantité'].apply(lambda x: max(x, 0))  # Remplacer les valeurs négatives par 0
else:
    print("La colonne 'Quantité' est absente du fichier.")

# Calculer les prix totaux si manquants
if 'Prix_Total' in ventes.columns and 'Quantité' in ventes.columns and 'Prix_Unitaire' in ventes.columns:
    ventes['Prix_Total'] = ventes['Prix_Total'].replace(0, np.nan)  # Remplacer 0 par NaN
    ventes['Prix_Total'] = ventes['Prix_Total'].fillna(
        ventes['Quantité'] * ventes['Prix_Unitaire']
    )
else:
    print("Les colonnes nécessaires pour calculer le prix total sont absentes du fichier.")

# Sauvegarder les données nettoyées
ventes.to_csv('ventes_nettoyees.csv', index=False)

print("Nettoyage du fichier 'ventes.csv' terminé !")
