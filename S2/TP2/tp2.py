import csv, nltk, json

# Ex1 

text = []
with open("pg10775.txt", encoding='utf-8', mode="r") as file:
    for line in file:
        text.append(line.strip())
    file.close()

# 1.1
text_string = " ".join(text)
print(len(text_string.split(" ")))

# 1.2 
tokens = nltk.tokenize.word_tokenize(" ".join(text))
print(len(tokens))

# 1.3 

tokens_set = set(tokens)
print(len(tokens_set))

# Ex2

# 2.1.1

header = None
values = []
with open("notes.csv", encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for i, row in enumerate(csv_reader):
        if i == 0:
            header = row
        else:
            values.append(row)
    csv_file.close()

formatted_header = "\t\t".join(header)
print(formatted_header)
for value in values:
    formatted_value = "\t\t".join(value)
    print(formatted_value)

# 2.1.2

def major(path:str) -> str:
    top_grade = 0
    top_name = ""
    with open(path, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for i, row in enumerate(csv_reader):
            if i != 0:
                if len(row) != 0:
                    if float(row[2]) > float(top_grade):
                        top_name = " ".join([row[0], row[1]])
                        top_grade = row[2]
    return top_name

print(f"{major('notes.csv')} a la note la plus élevée.")

# 2.1.3

with open('notes.csv', mode='a', encoding='utf-8', newline='') as csv_file:
    csv_file.write("\n") # Ajout manuel d'une nouvelle ligne pour éviter que la valeur ajoutée plus tard soit sur la dernière ligne
    writer = csv.writer(csv_file)
    writer.writerow(["Laure","Plaquer", "15"])
    csv_file.close()

# 2.2.1
# 2.2.2
# 2.2.3

with open ('019HexaSmal.csv', mode='r') as csv_file:
    count = 0
    reader = csv.reader(csv_file, delimiter=';')
    for row in reader:
        if row[3].strip() == "MARSEILLE": #  or row[0] == "13213"
            count+=1
    print(f"Marseille apparait {count} fois")

# 2.3.2

prenom_2003 = []
with open ('nat2022.csv', mode='r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for i, row in enumerate(reader):
        if i != 0:
            if row[2] == "2003":
                prenom_2003.append((row[0],row[1], row[3]))
    csv_file.close()

top_filles = [None, 0]
top_garcons = [None, 0]
for i in prenom_2003:
    if i[0] == "1":
        if int(i[2]) > int(top_garcons[1]) and i[1] != "_PRENOMS_RARES":
            top_garcons[0] = i[1]
            top_garcons[1] = i[2]
    elif i[0] == "2":
        if int(i[2]) > int(top_filles[1]) and i[1] != "_PRENOMS_RARES":
            top_filles[0] = i[1]
            top_filles[1] = i[2]

print(f"Le prénom le plus donné aux filles nées en 2003 est {top_filles[0]}, {top_filles[1]} fois")
print(f"Le prénom le plus donné aux garçons nés en 2003 est {top_garcons[0]}, {top_garcons[1]} fois")


# Pour 2022

prenom_2022 = []
with open ('nat2022.csv', mode='r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for i, row in enumerate(reader):
        if i != 0:
            if row[2] == "2022":
                prenom_2022.append((row[0],row[1], row[3]))
    csv_file.close()

top_filles = [None, 0]
top_garcons = [None, 0]
for i in prenom_2022:
    if i[0] == "1":
        if int(i[2]) > int(top_garcons[1]) and i[1] != "_PRENOMS_RARES":
            top_garcons[0] = i[1]
            top_garcons[1] = i[2]
    elif i[0] == "2":
        if int(i[2]) > int(top_filles[1]) and i[1] != "_PRENOMS_RARES":
            top_filles[0] = i[1]
            top_filles[1] = i[2]

print(f"Le prénom le plus donné aux filles nées en 2022 est {top_filles[0]}, {top_filles[1]} fois")
print(f"Le prénom le plus donné aux garçons nés en 2022 est {top_garcons[0]}, {top_garcons[1]} fois")

# 2.3.3

prenoms_dict = []
with open("dpt2022.csv", encoding='utf-8', mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for i, row in enumerate(csv_reader):
        dico = {}
        dico["Prénom"] = ""
        dico["Occurences"] = ""
        dico["Département"] = ""
        dico["Année"] = ""
        if i != 0:
            if row[1].upper() == "PAUL":
                dico["Prénom"] = row[1]
                dico["Occurences"] = row[3]
                dico["Département"] = row[4]
                dico["Année"] = row[2]
                prenoms_dict.append(dico)

max_paul_dpt = ""
max_paul_num = 0
max_paul_year = ""

for i in prenoms_dict:
    if not "X" in i["Occurences"]:
        if int(i["Occurences"]) > max_paul_num:
            max_paul_dpt = i["Département"]
            max_paul_num = int(i["Occurences"])
            max_paul_year = i["Année"]

print(f"{max_paul_num} enfants ont été nommés PAUL dans le {max_paul_dpt} en {max_paul_year}.")

# Exercice 3

# 3 

json_list = []
with open("ODSEN_GENERAL.json", encoding='utf-8', mode="r") as json_file:
    for i in json_file:
        json_list.append(i.strip())
    json_file.close()

json_string = " ".join(json_list)
data = json.loads(json_string)
data = data['results']

actifs = []
for i in data:
    if i["Etat"] == 'ACTIF':
        actifs.append(i)
print(f"{len(actifs)} sénateurs sont actifs dans les données.")

# 4 
age_total = 0
for senateur in actifs:
    année = int(senateur["Date_naissance"][0:4])
    age = 2025 - année
    age_total += age

age_moyen = age_total//len(actifs)

print(f"l'age moyen des Sénateurs actifs est de {age_moyen} ans")

