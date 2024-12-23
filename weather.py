import requests
import os

# Base URL de l'API OpenWeather
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Clé API (assurez-vous d'utiliser votre propre clé API)
API_KEY = os.getenv("OPENWEATHER_API_KEY", "votre_clé_api_ici")

def fetch_weather(city_name):
    """
    Récupère les données météo pour une ville donnée.
    
    :param city_name: Nom de la ville
    :return: Dictionnaire contenant les données météo ou un message d'erreur
    """
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",  # Pour obtenir des températures en Celsius
        "lang": "fr"       # Langue des descriptions météo
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Génère une erreur pour les codes HTTP 4xx/5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Test du script
if __name__ == "__main__":
    # Exemple : Récupérer les données météo pour Paris
    city = "Paris"
    weather_data = fetch_weather(city)
    
    if "error" in weather_data:
        print(f"Erreur : {weather_data['error']}")
    else:
        print(f"Météo à {city} :")
        print(f" - Température : {weather_data['main']['temp']}°C")
        print(f" - Humidité : {weather_data['main']['humidity']}%")
        print(f" - Description : {weather_data['weather'][0]['description']}")
