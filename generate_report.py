import pandas as pd
from datetime import datetime
import json

# Charger les données
df = pd.read_csv('sp500_data.csv', names=['datetime', 'sp500'])
df['datetime'] = pd.to_datetime(df['datetime'])
df['sp500'] = df['sp500'].astype(float)

# Garder uniquement les données d'aujourd'hui
today = pd.Timestamp.now().normalize()
df_today = df[df['datetime'] >= today]

if not df_today.empty:
    open_price = df_today.iloc[0]['sp500']
    close_price = df_today.iloc[-1]['sp500']
    variation = ((close_price - open_price) / open_price) * 100
    volatility = df_today['sp500'].std()

    report = {
        'date': today.strftime('%Y-%m-%d'),
        'open_price': round(open_price, 2),
        'close_price': round(close_price, 2),
        'variation_percent': round(variation, 2),
        'volatility': round(volatility, 2)
    }
else:
    report = {'message': 'Pas assez de données pour aujourd\'hui'}

# Sauvegarder dans un fichier JSON
with open('daily_report.json', 'w') as f:
    json.dump(report, f)
