from datetime import date

def calculer_age(annee_naissance):
    date_actuelle = date.today()
    annee_actuelle = date_actuelle.year
    mois_actuel = date_actuelle.month
    jour_actuel = date_actuelle.day

    age_en_annees = annee_actuelle - annee_naissance
    age_en_mois = (age_en_annees * 12) + (mois_actuel - 1)
    age_en_jours = (date_actuelle - date(annee_naissance, mois_actuel, jour_actuel)).days
    age_en_semaines = age_en_jours // 7

    return age_en_annees, age_en_mois, age_en_jours, age_en_semaines

annee_de_naissance = int(input("Entrez une année : "))
age_annees, age_mois, age_jours, age_semaines = calculer_age(annee_de_naissance)

print("Âge :")
print("Années :", age_annees)
print("Mois :", age_mois)
print("Jours :", age_jours)
print("Semaines :", age_semaines)
