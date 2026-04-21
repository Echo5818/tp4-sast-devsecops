import sqlite3
import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def get_user():
    user_id = request.args.get("id")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    # L'injection SQL classique
    cursor.execute("SELECT * FROM users WHERE id = " + user_id)
    return "User data"

@app.route("/remove")
def remove():
    filename = request.args.get("file")
    # L'injection de commande classique
    os.system("rm -rf " + filename)

SECRET_KEY = "AKIAIMNO789ABCDEF012"