import os

# BONNE PRATIQUE : On ne stocke jamais de clé en clair. 
# On la récupère depuis l'environnement du serveur.
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

def get_connection():
    if not AWS_SECRET_KEY:
        raise ValueError("La clé AWS est manquante dans la configuration !")
    return "Connexion établie avec la clé sécurisée"
