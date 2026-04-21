import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def get_user():
    user_id = request.args.get("id")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    # Utilisation de requêtes paramétrées (SÉCURISÉ)
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return "Données sécurisées"
