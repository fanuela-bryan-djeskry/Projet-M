from flask import Flask
import dash
from dash import dcc, html
import plotly.express as px

# Crée une instance Flask
server = Flask(__name__)

# Crée une instance Dash, et associe-la au serveur Flask
app = dash.Dash(__name__, server=server, routes_pathname_prefix='/dash/')

# Exemple de données pour le graphique
data = [
    {"timestamp": "2024-12-23T10:00:00", "temperature": 12},
    {"timestamp": "2024-12-23T11:00:00", "temperature": 14},
    {"timestamp": "2024-12-23T12:00:00", "temperature": 16},
]

# Crée un graphique avec Plotly
fig = px.line(data, x="timestamp", y="temperature", title="Température au fil du temps")

# Définir le layout de Dash
app.layout = html.Div(children=[
    html.H1("Tableau de bord Météo"),
    dcc.Graph(figure=fig)
])

# Route Flask pour la page d'accueil
@server.route('/')
def index():
    return "Bienvenue sur le serveur Flask avec Dash intégré ! Accédez au tableau de bord à <a href='/dash/'>ici</a>."

if __name__ == '__main__':
    # Lancer le serveur Flask qui gère aussi Dash
    server.run(debug=True, host='0.0.0.0', port=5000)
