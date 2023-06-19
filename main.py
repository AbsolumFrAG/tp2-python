import json

def load_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def add_student(data):
    student_name = input("Nom de l'élève : ")
    if student_name in data:
        print("Cet élève existe déjà.")
        return
    data[student_name] = {'notes': {}, 'appréciation': ''}
    print(f"L'élève '{student_name}' a été ajouté.")

def add_grade(data):
    student_name = input("Nom de l'élève : ")
    if student_name not in data:
        print("Cet élève n'existe pas.")
        return
    tp_name = input("Nom du TP : ")
    grade = input("Note : ")
    data[student_name]['notes'][tp_name] = int(grade)
    print(f"La note du TP '{tp_name}' pour l'élève '{student_name}' a été ajoutée.")

def update_appreciation(data):
    student_name = input("Nom de l'élève : ")
    if student_name not in data:
        print("Cet élève n'existe pas.")
        return
    appreciation = input("Nouvelle appréciation : ")
    data[student_name]['appréciation'] = appreciation
    print(f"L'appréciation de l'élève '{student_name}' a été mise à jour.")

def list_students(data):
    for student, info in data.items():
        print(f"Élève : {student}")
        print("Notes :")
        for tp, grade in info['notes'].items():
            print(f"- {tp}: {grade}")
        print(f"Appréciation : {info['appréciation']}")
        print("")

def generate_stats(data):
    stats = {}
    for student, info in data.items():
        notes = info['notes'].values()
        stats[student] = {
            'moyenne': sum(notes) / len(notes),
            'min': min(notes),
            'max': max(notes)
        }
    with open('stats.json', 'w') as file:
        json.dump(stats, file, indent=4)
    print("Les statistiques ont été générées.")

def main():
    data = load_data()
    
    while True:
        command = input("Commande : ")

        if command == 'add':
            add_student(data)
        elif command == 'notes':
            add_grade(data)
        elif command == 'appr':
            update_appreciation(data)
        elif command == 'list':
            list_students(data)
        elif command == 'quitter':
            save_data(data)
            generate_stats(data)
            print("Données sauvegardées. Au revoir !")
            break
        else:
            print("Pas compris")

if __name__ == '__main__':
    main()
