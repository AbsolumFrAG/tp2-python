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

    # Créer un fichier appréciation.txt dans le dossier de chaque élève
    with open(os.path.join(eleve_folder, 'appréciation.txt'), 'w') as file:
        note = dicEleves[eleve]['notes']['tp1']
        file.write(str(note))

    # Créer un fichier notes.csv dans le dossier de chaque élève
    with open(os.path.join(eleve_folder, 'notes.csv'), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['TP1', 'TP2', 'TP3'])
        notes = dicEleves[eleve]['notes']
        writer.writerow([notes['tp1'], notes['tp2'], notes['tp3']])

    # Créer un fichier json dans le dossier de chaque élève avec la structure demandée
    eleve_data = {
        'moyenne': sum(notes.values()) / len(notes),
        'min': min(notes.values()),
        'max': max(notes.values())
    }
    with open(os.path.join(eleve_folder, 'eleve.json'), 'w') as file:
        json.dump(eleve_data, file, indent=4)