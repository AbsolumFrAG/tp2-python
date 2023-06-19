import os
import json
import csv

dicEleves = {
    'eleve1': {'notes': {'tp1': 10, 'tp2': 13, 'tp3': 17}, 'appréciation': 'moyenne'},
    'eleve2': {'notes': {'tp1': 19, 'tp2': 11, 'tp3': 14}, 'appréciation': 'Très bien'},
    'eleve3': {'notes': {'tp1': 15, 'tp2': 8, 'tp3': 13}, 'appréciation': 'Bonne'}
}

# Créer un dossier 'eleves' s'il n'existe pas déjà
if not os.path.exists('eleves'):
    os.makedirs('eleves')

# Parcourir chaque élève et créer un dossier pour chaque élève
for eleve in dicEleves:
    eleve_folder = os.path.join('eleves', eleve)
    if not os.path.exists(eleve_folder):
        os.makedirs(eleve_folder)