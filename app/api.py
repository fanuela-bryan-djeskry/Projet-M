from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

# Initialisation de l'application Flask
app = Flask(__name__)

# Connexion à MongoDB
# Récupération de l'URI MongoDB depuis les variables d'environnement
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/weather_data")
client = MongoClient(mongo_uri)
db = client["weather_data"]
collection = db["weather"]

# Route pour ajouter des données météo
@app.route('/add_weather', methods=['POST'])
def add_weather():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    collection.insert_one(data)
    return jsonify({"message": "Weather data added successfully"}), 201

# Route pour récupérer toutes les données météo
@app.route('/weather', methods=['GET'])
def get_weather():
    data = list(collection.find({}, {"_id": 0}))  # Exclure l'ID MongoDB par défaut
    return jsonify(data), 200

# Point d'entrée de l'application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
