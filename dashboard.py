import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go

app = Dash(__name__)
server = app.server  # nécessaire si tu déploies via gunicorn plus tard

# Charger les données du CSV
def load_data():
    df = pd.read_csv("sp500_data.csv", names=["datetime", "sp500"])
    df["datetime"] = pd.to_datetime(df["datetime"])
    return df

# Charger le rapport
def load_report():
    try:
        with open("daily_report.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "📭 Aucun rapport disponible pour aujourd’hui."

# Layout de l’application
app.layout = html.Div([
    html.H1("📈 Suivi S&P 500 en direct", style={"textAlign": "center"}),

    dcc.Graph(id="sp500-graph"),

    dcc.Interval(
        id="interval-component",
        interval=60 * 1000,  # 60 secondes
        n_intervals=0
    ),

    html.H2("🗒 Rapport quotidien"),
    html.Pre(id="report", style={"whiteSpace": "pre-wrap", "fontSize": "16px", "backgroundColor": "#f9f9f9", "padding": "10px", "border": "1px solid #ccc"})
])

# Callback pour mettre à jour la courbe
@app.callback(
    Output("sp500-graph", "figure"),
    Input("interval-component", "n_intervals")
)
def update_graph(n):
    df = load_data()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["datetime"], y=df["sp500"], mode="lines+markers", name="S&P 500"))
    fig.update_layout(title="Évolution du S&P 500", xaxis_title="Temps", yaxis_title="Valeur", template="plotly_white")
    return fig

# Callback pour mettre à jour le rapport
@app.callback(
    Output("report", "children"),
    Input("interval-component", "n_intervals")
)
def update_report(n):
    return load_report()

# Lancer l’app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)


