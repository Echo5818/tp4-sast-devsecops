import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/delete")
def delete_file():
    file_to_delete = request.args.get("name")
    # Injection de commande système (DANGEREUX)
    os.system("rm -rf " + file_to_delete)
    return "Fichier supprimé"
