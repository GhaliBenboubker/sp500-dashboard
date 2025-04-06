import pandas as pd
from datetime import datetime

# Lire le fichier
df = pd.read_csv("sp500_data.csv", names=["datetime", "sp500"])
df["datetime"] = pd.to_datetime(df["datetime"])

# Filtrer les données du jour
today = pd.Timestamp.today().normalize()
df_today = df[df["datetime"] >= today]

# Initialiser le contenu du rapport
if not df_today.empty:
    open_price = df_today.iloc[0]["sp500"]
    close_price = df_today.iloc[-1]["sp500"]
    change = close_price - open_price
    volatility = df_today["sp500"].std()

    report = f"""📅 Rapport du {today.date()}
🟢 Ouverture : {open_price}
🔴 Clôture  : {close_price}
📈 Évolution : {change:.2f}
🌪️ Volatilité : {volatility:.2f}
"""
else:
    report = f"❌ Aucune donnée trouvée pour le {today.date()}.\n"

# Sauvegarde du rapport
with open("daily_report.txt", "w") as f:
    f.write(report)

# Afficher à l'écran
print(report)

