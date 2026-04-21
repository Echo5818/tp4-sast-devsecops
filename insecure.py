def login(password):
    # ERREUR: Mot de passe écrit en clair dans le code
    secret_pass = "Admin12345!" 
    if password == secret_pass:
        return "Accès accordé"
    return "Accès refusé"
