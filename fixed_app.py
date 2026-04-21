import sqlite3
import os
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def get_user_fixed():
    user_id = request.args.get("id")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    # CORRECTION SQL : Utilisation de requêtes paramétrées (le "?" remplace la concaténation)
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return "Données utilisateur sécurisées"

@app.route("/remove")
def remove_fixed():
    filename = request.args.get("file")
    # CORRECTION COMMANDE : Utilisation de subprocess avec une liste d'arguments 
    # Cela empêche l'injection de commandes supplémentaires via des caractères comme ";" ou "&&"
    subprocess.run(["rm", "-rf", filename])

# CORRECTION SECRET : On ne met plus la clé en dur, on l'appelle via une variable d'environnement
API_KEY = os.getenv("MY_API_KEY")
