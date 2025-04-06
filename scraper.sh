#!/bin/bash

# Récupération de la valeur du S&P 500
SP500=$(curl -s "https://www.investing.com/indices/us-spx-500" | grep -oP '"instrument-price-last">\K[0-9,]+')

# Ajouter la date et la valeur dans un fichier de log
SP500_CLEAN=$(echo "$SP500" | tr -d ',')
echo "$(date +"%Y-%m-%d %H:%M:%S"),$SP500_CLEAN" >> /home/ubuntu/sp500-dashboard/sp500_data.csv


# Afficher la valeur dans le terminal
echo "[$(date +"%Y-%m-%d %H:%M:%S")] S&P 500 : $SP500"
