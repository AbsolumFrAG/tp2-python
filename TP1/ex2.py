def compter_mots(chaine):
    mots = chaine.split()
    return len(mots)

phrase = "Ceci est une phrase de test"
nombre_mots = compter_mots(phrase)
print("Nombre de mots :", nombre_mots)

def compter_voyelles(chaine):
    voyelles = "aeiouy"
    nombre_voyelles = 0
    for char in chaine:
        if char.lower() in voyelles:
            nombre_voyelles += 1
    return nombre_voyelles

mot = "Bonjour"
nombre_voyelles = compter_voyelles(mot)
print("Nombre de voyelles :", nombre_voyelles)

def compter_presence_lettre(chaine, lettre):
    nombre_presence = 0
    for char in chaine:
        if char.lower() == lettre.lower():
            nombre_presence += 1
    return nombre_presence

chaine = "Bienvenue dans le monde de Python"
lettre = "e"
nombre_presence = compter_presence_lettre(chaine, lettre)
print("Nombre de présences de la lettre", lettre, ":", nombre_presence)

def liste_mots(phrase):
    mots = phrase.split()
    return mots

phrase = "Je suis une phrase de test"
liste_des_mots = liste_mots(phrase)
print("Liste des mots :", liste_des_mots)

def verifier_presence_lettre(chaine, lettre):
    return lettre.lower() in chaine.lower()

chaine = "Bonjour tout le monde"
lettre = "o"
presence_lettre = verifier_presence_lettre(chaine, lettre)
if presence_lettre:
    print("La lettre", lettre, "est présente dans la chaîne.")
else:
    print("La lettre", lettre, "n'est pas présente dans la chaîne.")

def verifier_presence_mot(liste, mot):
    if mot in liste:
        return liste.index(mot)
    else:
        return -1

liste_mots = ["chat", "chien", "oiseau", "poisson"]
mot_recherche = "chien"
position_mot = verifier_presence_mot(liste_mots, mot_recherche)
if position_mot != -1:
    print("Le mot", mot_recherche, "est présent à la position", position_mot)
else:
    print("Le mot", mot_recherche, "n'est pas présent dans la liste.")
