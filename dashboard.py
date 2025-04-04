import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import json

# Fonction pour charger les données scrappées
def load_data():
    df = pd.read_csv('sp500_data.csv', names=['datetime', 'sp500'])
    df['datetime'] = pd.to_datetime(df['datetime'])
    df['sp500'] = df['sp500'].astype(float)
    return df

# Fonction pour charger le rapport quotidien
def load_report():
    try:
        with open('daily_report.json') as f:
            report = json.load(f)
        return report
    except:
        return {"message": "Rapport non disponible."}

# Initialisation de l'app Dash
app = dash.Dash(__name__)

# Layout de l'application
app.layout = html.Div([
    html.H1("📊 S&P 500 Live Tracker", style={'textAlign': 'center'}),

    dcc.Graph(id='price-graph'),

    html.Div(id='daily-report', style={
        'marginTop': '30px',
        'fontSize': '18px',
        'textAlign': 'center'
    }),

    dcc.Interval(
        id='interval-update',
        interval=5*60*1000,  # toutes les 5 minutes
        n_intervals=0
    )
])

# Callback pour actualiser le graphe + rapport
@app.callback(
    [Output('price-graph', 'figure'),
     Output('daily-report', 'children')],
    Input('interval-update', 'n_intervals')
)
def update_dashboard(n):
    df = load_data()
    fig = px.line(df, x='datetime', y='sp500', title='S&P 500 Time Series')

    report = load_report()
    if "message" in report:
        report_text = report["message"]
    else:
        report_text = (
            f"📅 {report['date']}  |  "
            f"🔹 Open: {report['open_price']}  |  "
            f"🔸 Close: {report['close_price']}  |  "
            f"📈 Variation: {report['variation_percent']}%  |  "
            f"💥 Volatility: {report['volatility']}"
        )

    return fig, report_text

# Lancer le serveur
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)

