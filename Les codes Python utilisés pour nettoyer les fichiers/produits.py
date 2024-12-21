import pandas as pd
import numpy as np

# Charger les données
produits = pd.read_csv('produits.csv')

# Nettoyer les prix unitaire : Remplacer les prix nuls ou manquants par la moyenne
produits['Prix_Unitaire'] = produits['Prix_Unitaire'].replace(0, np.nan)  # Remplacer 0 par NaN
produits['Prix_Unitaire'] = produits['Prix_Unitaire'].fillna(produits['Prix_Unitaire'].mean())

# Nettoyer le stock : Remplacer les valeurs négatives par 0
produits['Stock_Disponible'] = produits['Stock_Disponible'].apply(lambda x: max(x, 0))

# Sauvegarder les données nettoyées
produits.to_csv('produits_nettoyes.csv', index=False)

print("Nettoyage du fichier 'produits.csv' terminé !")
