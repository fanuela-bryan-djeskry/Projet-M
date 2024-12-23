import dash
from dash import dcc, html
import plotly.express as px

app = dash.Dash(__name__)

# Exemple de données
data = [
    {"timestamp": "2024-12-23T10:00:00", "temperature": 12},
    {"timestamp": "2024-12-23T11:00:00", "temperature": 14},
    {"timestamp": "2024-12-23T12:00:00", "temperature": 16},
]

fig = px.line(data, x="timestamp", y="temperature", title="Température au fil du temps")

app.layout = html.Div(children=[
    html.H1("Tableau de bord Météo"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
