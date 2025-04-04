- Scraping du cours du S&P 500 toutes les 5 minutes via un script Bash (`scraper.sh`)
- Stockage des données horodatées dans `sp500_data.csv`
- Génération d’un **rapport quotidien à 20h** avec :
  - Prix d’ouverture
  - Prix de clôture
  - Variation en %
  - Volatilité
- Dashboard web interactif en Python avec Dash (`dashboard.py`)


1. Lancer l’environnement virtuel :
   ```bash
   source venv_dash/bin/activate
