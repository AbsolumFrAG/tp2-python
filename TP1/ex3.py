def gestion_liste():
    liste_mots = []

    while True:
        action = input("Que souhaitez-vous faire ? (Ajouter/Supprimer/Tableau/Stop) ")

        if action.lower() == "ajouter":
            mot = input("Entrez un mot à ajouter : ")
            if mot not in liste_mots:
                liste_mots.append(mot)
                print("Le mot", mot, "a été ajouté à la liste.")
            else:
                print("Le mot", mot, "est déjà présent dans la liste.")

        elif action.lower() == "supprimer":
            mot = input("Entrez un mot à supprimer : ")
            if mot in liste_mots:
                liste_mots.remove(mot)
                print("Le mot", mot, "a été supprimé de la liste.")
            else:
                print("Le mot", mot, "n'est pas présent dans la liste.")

        elif action.lower() == "tableau":
            print("Contenu de la liste :", liste_mots)

        elif action.lower() == "stop":
            print("Arrêt du programme.")
            break

        else:
            print("Action invalide. Veuillez réessayer.")

# Exemple d'utilisation :
gestion_liste()
