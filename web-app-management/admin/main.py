import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

# Connexion à la base de données MySQL
db = mysql.connector.connect(
    host="localhost",
    user="votre_utilisateur",
    password="votre_mot_de_passe",
    database="ma_base_de_donnees"
)
cursor = db.cursor()

# Route pour ajouter des données à la base de données
@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.json
    query = "INSERT INTO ma_table (colonne1, colonne2) VALUES (%s, %s)"
    values = (data['valeur1'], data['valeur2'])

    cursor.execute(query, values)
    db.commit()

    return jsonify({"message": "Données ajoutées avec succès"})

# Route pour récupérer toutes les données de la base de données
@app.route('/get_data', methods=['GET'])
def get_data():
    query = "SELECT * FROM ma_table"
    cursor.execute(query)
    result = cursor.fetchall()

    data_list = []
    for row in result:
        data_list.append({
            "colonne1": row[0],
            "colonne2": row[1]
        })

    return jsonify(data_list)

if __name__ == '__main__':
    app.run(debug=True)
