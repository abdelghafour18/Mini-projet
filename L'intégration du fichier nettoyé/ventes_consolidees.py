import pandas as pd

# Load CSV files
produits = pd.read_csv('produits_nettoyes.csv')
ventes = pd.read_csv('ventes_nettoyees.csv')
clients = pd.read_csv('clients_nettoyees.csv')
promotions = pd.read_csv('promotions_nettoyees.csv')

# Standardize column names
ventes.columns = ventes.columns.str.strip().str.lower()
clients.columns = clients.columns.str.strip().str.lower()
produits.columns = produits.columns.str.strip().str.lower()
promotions.columns = promotions.columns.str.strip().str.lower()

# Merge data using the correct key
try:
    ventes_clients = pd.merge(ventes, clients, on='id_client', how='inner')
    ventes_produits = pd.merge(ventes_clients, produits, on='id_produit', how='inner')
    ventes_finales = pd.merge(ventes_produits, promotions, on='id_produit', how='left')

    # Save the final integrated data
    ventes_finales.to_csv('ventes_consolidees.csv', index=False)
    print("Données intégrées avec succès !")

except KeyError as e:
    print(f"KeyError during merging: {e}")
    print("Ensure the merging keys exist and are correctly matched.")
