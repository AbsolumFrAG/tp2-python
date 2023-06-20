import pandas as pd
import numpy as np

# Création des données de notes aléatoires
np.random.seed(42)  # Pour obtenir des résultats reproductibles
eleves = ['Élève ' + str(i+1) for i in range(10)]
tps = ['TP ' + str(i+1) for i in range(12)]
notes = np.random.randint(0, 20, size=(10, 12))

# Création du dataframe avec les notes
df = pd.DataFrame(notes, index=eleves, columns=tps)
print("Matrice des notes de TP :")
print(df)

# Sélection des 4 premiers TP
premiers_tps = df.iloc[:, :4]
print("\nLes 4 premiers TP :")
print(premiers_tps)

# Sélection d'un élève sur deux
eleves_un_sur_deux = df.iloc[::2, :]
print("\nUn élève sur deux :")
print(eleves_un_sur_deux)

# Notes supérieures à 13
notes_sup_13 = df[df > 13]
print("\nNotes supérieures à 13 :")
print(notes_sup_13)

# Moyenne de chaque élève et de chaque TP
moyenne_eleve = df.mean(axis=1)
moyenne_tp = df.mean(axis=0)
print("\nMoyenne de chaque élève :")
print(moyenne_eleve)
print("\nMoyenne de chaque TP :")
print(moyenne_tp)

# Médiane de chaque élève et de chaque TP
median_eleve = df.median(axis=1)
median_tp = df.median(axis=0)
print("\nMédiane de chaque élève :")
print(median_eleve)
print("\nMédiane de chaque TP :")
print(median_tp)

# Minimum de chaque élève et de chaque TP
min_eleve = df.min(axis=1)
min_tp = df.min(axis=0)
print("\nMinimum de chaque élève :")
print(min_eleve)
print("\nMinimum de chaque TP :")
print(min_tp)

# Maximum de chaque élève et de chaque TP
max_eleve = df.max(axis=1)
max_tp = df.max(axis=0)
print("\nMaximum de chaque élève :")
print(max_eleve)
print("\nMaximum de chaque TP :")
print(max_tp)
