import numpy as np

# Génération des notes de TP aléatoires entre 0 et 20
np.random.seed(42)  # Pour obtenir des résultats reproductibles
notes = np.random.randint(0, 21, size=(12, 10))

# Affichage de la matrice de notes
print("Matrice de notes :")
print(notes)
print()

# Sélection des 4 premiers TP
tp_4_premiers = notes[:, :4]
print("Notes des 4 premiers TP :")
print(tp_4_premiers)
print()

# Sélection d'un élève sur deux
eleves_un_sur_deux = notes[::2, :]
print("Notes des élèves un sur deux :")
print(eleves_un_sur_deux)
print()

# Notes supérieures à 13
notes_sup_13 = notes[notes > 13]
print("Notes supérieures à 13 :")
print(notes_sup_13)
print()

# Calcul de la moyenne de chaque élève et de chaque TP
moyenne_eleve = np.mean(notes, axis=1)
moyenne_tp = np.mean(notes, axis=0)
print("Moyenne de chaque élève :")
print(moyenne_eleve)
print()
print("Moyenne de chaque TP :")
print(moyenne_tp)
print()

# Calcul de la médiane de chaque élève et de chaque TP
mediane_eleve = np.median(notes, axis=1)
mediane_tp = np.median(notes, axis=0)
print("Médiane de chaque élève :")
print(mediane_eleve)
print()
print("Médiane de chaque TP :")
print(mediane_tp)
print()

# Calcul du minimum de chaque élève et de chaque TP
min_eleve = np.min(notes, axis=1)
min_tp = np.min(notes, axis=0)
print("Minimum de chaque élève :")
print(min_eleve)
print()
print("Minimum de chaque TP :")
print(min_tp)
print()

# Calcul du maximum de chaque élève et de chaque TP
max_eleve = np.max(notes, axis=1)
max_tp = np.max(notes, axis=0)
print("Maximum de chaque élève :")
print(max_eleve)
print()
print("Maximum de chaque TP :")
print(max_tp)
print()
