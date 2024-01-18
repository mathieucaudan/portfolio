# -*- coding: utf-8 -*-
"""SAE15

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DXDXUfUCLzA5C1buL_tUkgF-FItMM75U
"""

#Niveau0
import pandas as pd
# Ouverture du fichier grâce a la méthode read_csv de pandas
bd = pd.read_csv("liste01.csv", encoding_errors="ignore", sep=";", index_col=False, encoding="cp1252", names=["ref", "date", "groupe_postes", "id_user", "login_user", "id_doc", "type_consultation", "type_acces"])
# Affichage de la base de donnés
print(bd)

#Niveau1.1
import csv
import matplotlib.pyplot as plt

# Ouvrir le fichier CSV
with open('liste01.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    dico={}
    for row in reader:
        if row[1][:10] in dico:
            dico[row[1][:10]]+=1
        else:
            dico.update({row[1][:10]: 1})

    cles = [str(x[0]) for x in dico.items()]
    valeurs = [x[1] for x in dico.items()]
    plt.figure(figsize=(12, 9))
    plt.plot(cles, valeurs)
    plt.xticks(rotation=90)
    plt.xlabel("Date")
    plt.ylabel('Nombre de consultation')
    plt.show()

#Niveau1.2
import csv
import matplotlib.pyplot as plt

# Ouvrir le fichier CSV
with open('liste01.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    dico={}
    for row in reader:
        if row[2][:10] in dico:
            dico[row[2][:10]]+=1
        else:
            dico.update({row[2][:10]: 1})

    cles = [str(x[0]) for x in dico.items()]
    valeurs = [x[1] for x in dico.items()]
    plt.figure(figsize=(12, 9))
    plt.plot(cles, valeurs)
    plt.xticks(rotation=90)
    plt.xlabel("Groupe de postes")
    plt.ylabel('Nombre de consultation')
    plt.show()

#Niveau1.3
import csv
import matplotlib.pyplot as plt

# Ouvrir le fichier CSV
with open('liste01.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    # Création de variable compteur
    compt_modif=0
    compt_lect=0
    compt_crea=0
    compt_supp=0

    # Boucle afin incrémenter le compteur si le type d'accès est celui dans la condition
    for row in reader:
        if row[7] == "accès en mode modification" :
            compt_modif +=1
        elif row[7] == "accès en mode lecture" :
            compt_lect +=1
        elif row[7] == "création":
            compt_crea +=1
        elif row[7] == "suppression":
            compt_supp +=1
# Taille du camembert
plt.figure(figsize=(10,10))
#création du camembert avec les compteurs comme valeurs et le type d'accès comme titre
plt.pie([compt_modif, compt_lect, compt_crea, compt_supp], labels = ["accès en mode modification: "+str(compt_modif), "accès en mode lecture: "+str(compt_lect), "création: "+str(compt_crea), "suppression: "+str(compt_supp) ], normalize = True)
# Variable pour éviter la ligne de la légende
var_legende = plt.legend()

#Niveau2.1
import pandas as pd
import matplotlib.pyplot as plt
#ouverture du fichier grâce a la méthode read_csv de pandas
bd = pd.read_csv("liste01.csv", encoding_errors="ignore", sep=";", index_col=False, encoding="cp1252", names=["ref", "date", "groupe_postes", "id_user", "login_user", "id_doc", "type_consultation", "type_acces"])
# Créatiob du dictionnaire vide
dico={}
# Boucle pour ajouter l'identifiant au dictionnaire s'il n'est pas présent, s'il l'est sa valeur est incrémenter de 1
for i in range(len(bd)):
    if bd["date"][i][:10] in dico:
        dico[bd["date"][i][:10]]+=1
    else:
        dico.update({bd["date"][i][:10]: 1})

cles = [str(x[0]) for x in dico.items()]
valeurs = [x[1] for x in dico.items()]


plt.figure(figsize=(20, 9))
plt.plot(cles, valeurs)
plt.xticks(rotation=-45)
plt.xlabel("Login d'utilsateur")
plt.ylabel('Nombre de consultation')
plt.show()

#Niveau2.2
import pandas as pd
import matplotlib.pyplot as plt
bd = pd.read_csv("liste01.csv", encoding_errors="ignore", sep=";", index_col=False, encoding="cp1252", names=["ref", "date", "groupe_postes", "id_user", "login_user", "id_doc", "type_consultation", "type_acces"])
dico={}
for i in range(len(bd)):
    if bd["groupe_postes"][i] in dico:
        dico[bd["groupe_postes"][i]]+=1
    else:
        dico.update({bd["groupe_postes"][i]: 1})
print(len(dico))

cles = [str(x[0]) for x in dico.items()]
valeurs = [x[1] for x in dico.items()]

plt.figure(figsize=(12, 9))
plt.bar(cles, valeurs)
plt.xticks(rotation=90)
plt.xlabel("Groupe de postes")
plt.ylabel('Nombre de consultation')
plt.show()

#Niveau2.3
import pandas as pd

# Ouverture du fichier grâce a la méthode read_csv de pandas
bd = pd.read_csv("liste01.csv", encoding_errors="ignore", sep=";", index_col=False, encoding="cp1252", names=["ref", "date", "groupe_postes", "id_user", "login_user", "id_doc", "type_consultation", "type_acces"])
# Création de variable compteur
compt_modif=0
compt_lect=0
compt_crea=0
compt_supp=0
# Boucle afin incrémenter le compteur si le type d'accès est celui dans  la condition
for element in bd["type_acces"]:
    if element == "accès en mode modification" :
        compt_modif +=1
    elif element == "accès en mode lecture" :
        compt_lect +=1
    elif element == "création":
        compt_crea +=1
    elif element == "suppression":
        compt_supp +=1

# Création du camembert
bd = pd.DataFrame({"mode d'accès": [compt_modif/len(bd), compt_lect/len(bd) ,compt_crea/len(bd), compt_supp/len(bd)],
                   'radius': [compt_modif,compt_lect,compt_crea,compt_supp]},
                  index=['accès en mode modification: '+str(compt_modif), 'accès en mode lecture: '+str(compt_lect), 'création: '+str(compt_crea), 'suppression: '+str(compt_supp)])
# Taille de du camembert et nom de du camembert sur l'axe des ordonnées
plot = bd.plot.pie(y="mode d'accès", figsize=(10, 10))

#Niveau3.1
import csv
import matplotlib.pyplot as plt



# Ouvrir le fichier CSV
with open('liste01.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    compt_ssr=0
    compt_sej=0
    compt_doc=0
    compt_con=0
    for row in reader:
        if row[6][:3] == "SSR" :
            compt_ssr+=1
        elif row[6] == "séjour" :
            compt_sej+=1
        elif row[6] == "document" :
            compt_doc+=1
        elif row[6] == "consultation" :
            compt_con+=1
plt.figure(figsize=(10,10))
#création du camembert avec les compteurs comme valeurs et le type d'accès comme titre
plt.pie([compt_ssr, compt_sej, compt_doc, compt_con], labels = ["SSR: "+str(compt_ssr), "séjour: "+str(compt_sej), "document: "+str(compt_doc), "consultation: "+str(compt_con) ], normalize = True)
# Variable pour éviter la ligne de la légende
var_legende = plt.legend()

#Niveau3.3
import csv
import matplotlib.pyplot as plt
import datetime as date
import numpy as np

# Ouvrir le fichier CSV
with open('liste01.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    #création de variable pour chaque type d'accès en fonction du jour
    compt_modif_lun=0
    compt_lect_lun=0
    compt_crea_lun=0
    compt_supp_lun=0

    compt_modif_mar=0
    compt_lect_mar=0
    compt_crea_mar=0
    compt_supp_mar=0

    compt_modif_jeu=0
    compt_lect_jeu=0
    compt_crea_jeu=0
    compt_supp_jeu=0

    compt_modif_mer=0
    compt_lect_mer=0
    compt_crea_mer=0
    compt_supp_mer=0

    compt_modif_ven=0
    compt_lect_ven=0
    compt_crea_ven=0
    compt_supp_ven=0

    compt_modif_sam=0
    compt_lect_sam=0
    compt_crea_sam=0
    compt_supp_sam=0

    compt_modif_dim=0
    compt_lect_dim=0
    compt_crea_dim=0
    compt_supp_dim=0

    modif_total=0
    lect_total=0
    crea_total=0
    supp_total=0
    # Boucle multiconditionnel qui incrémente la variable compteur en fonction du type d'accès et du jour
    for row in reader:
        if (date.datetime.strptime(row[1][:10], "%Y-%m-%d")).weekday() == 0:
            if row[7] == "accès en mode modification" :
                compt_modif_lun +=1
                modif_total+=1
            elif row[7] == "accès en mode lecture" :
                compt_lect_lun +=1
                lect_total+=1
            elif row[7] == "création" :
                compt_crea_lun +=1
                crea_total+=1
            elif row[7] == "suppression" :
                compt_supp_lun +=1
                supp_total+=1
        elif (date.datetime.strptime(row[1][:10], "%Y-%m-%d")).weekday() == 1:
            if row[7] == "accès en mode modification" :
                compt_modif_mar +=1
                modif_total+=1
            elif row[7] == "accès en mode lecture" :
                compt_lect_mar +=1
                lect_total+=1
            elif row[7] == "création" :
                compt_crea_mar +=1
                crea_total+=1
            elif row[7] == "suppression" :
                compt_supp_mar +=1
                supp_total+=1
        elif (date.datetime.strptime(row[1][:10], "%Y-%m-%d")).weekday() == 2:
            if row[7] == "accès en mode modification" :
                compt_modif_mer +=1
                modif_total+=1
            elif row[7] == "accès en mode lecture" :
                compt_lect_mer +=1
                lect_total+=1
            elif row[7] == "création" :
                compt_crea_mer +=1
                crea_total+=1
            elif row[7] == "suppression" :
                compt_supp_mer +=1
                supp_total+=1
        elif (date.datetime.strptime(row[1][:10], "%Y-%m-%d")).weekday() == 3:
            if row[7] == "accès en mode modification" :
                compt_modif_jeu +=1
                modif_total+=1
            elif row[7] == "accès en mode lecture" :
                compt_lect_jeu +=1
                lect_total+=1
            elif row[7] == "création" :
                compt_crea_jeu +=1
                crea_total+=1
            elif row[7] == "suppression" :
                compt_supp_jeu +=1
                supp_total+=1
        elif (date.datetime.strptime(row[1][:10], "%Y-%m-%d")).weekday() == 4:
            if row[7] == "accès en mode modification" :
                compt_modif_ven +=1
                modif_total+=1
            elif row[7] == "accès en mode lecture" :
                compt_lect_ven +=1
                lect_total+=1
            elif row[7] == "création" :
                compt_crea_ven +=1
                crea_total+=1
            elif row[7] == "suppression" :
                compt_supp_ven +=1
                supp_total+=1
        elif (date.datetime.strptime(row[1][:10], "%Y-%m-%d")).weekday() == 5:
            if row[7] == "accès en mode modification" :
                compt_modif_sam +=1
                modif_total+=1
            elif row[7] == "accès en mode lecture" :
                compt_lect_sam +=1
                lect_total+=1
            elif row[7] == "création" :
                compt_crea_sam +=1
                crea_total+=1
            elif row[7] == "suppression" :
                compt_supp_sam +=1
                supp_total+=1
        elif (date.datetime.strptime(row[1][:10], "%Y-%m-%d")).weekday() == 6:
            if row[7] == "accès en mode modification" :
                compt_modif_dim +=1
                modif_total+=1
            elif row[7] == "accès en mode lecture" :
                compt_lect_dim +=1
                lect_total+=1
            elif row[7] == "création" :
                compt_crea_dim +=1
                crea_total+=1
            elif row[7] == "suppression" :
                compt_supp_dim +=1
                supp_total+=1
# Création du dictionnaire avec les valeurs des 4 types d'accès pour chaque jour
data = {'Lundi':(compt_modif_lun,compt_lect_lun,compt_crea_lun,compt_supp_lun),
        'Mardi':(compt_modif_mar,compt_lect_mar,compt_crea_mar,compt_supp_mar),
        'Mercredi':(compt_modif_mer,compt_lect_mer,compt_crea_mer,compt_supp_mer),
        'Jeudi':(compt_modif_jeu,compt_lect_jeu,compt_crea_jeu,compt_supp_jeu),
        'Vendredi':(compt_modif_ven,compt_lect_ven,compt_crea_ven,compt_supp_ven),
        'Samedi':(compt_modif_sam,compt_lect_sam,compt_crea_sam,compt_supp_sam),
        'Dimanche':(compt_modif_dim,compt_lect_dim,compt_crea_dim,compt_supp_dim)}
# Création de liste et de variables
modification = []
lecture = []
creation = []
suppression = []

# Boucle qui permet de compter chaque type d'accès en fonction du jour grâce au dictionnaire
for day, counts in data.items():
    modification.append(counts[0]/modif_total*100)
    lecture.append(counts[1]/lect_total*100)
    creation.append(counts[2]/crea_total*100)
    suppression.append(counts[3]/supp_total*100)


# Utilisation de numpy pour la taille des collones du graphqieu en fonction de la taille du dictionnaire
x = np.arange(len(data))

# Taille du graphique
plt.figure(figsize=(20, 15))

# Création de chaque barre pour chaque type d'accès et chaque jour
plt.bar(x - 0.3, modification, width=0.2, label='Modification')
plt.bar(x - 0.1, lecture, width=0.2, label='Lecture')
plt.bar(x + 0.1, creation, width=0.2, label='Création')
plt.bar(x + 0.3, suppression, width=0.2, label='Suppression')

#Utilisation du dictionnaire avec la clés du dictionnaire(les jours) pour les jours sous chaque 4 collones
plt.xticks(x, data.keys())

# Mettre la légende en haut a gauche
plt.legend(loc="upper left")
# Nom de l'axe x
plt.xlabel('Jour de la semaine')
# Nom de l'axe y
plt.ylabel('Pourcentage du nombre de connections par semaine')
# Affichage du graphique
plt.show()

#Niveau4.1
import pandas as pd
import matplotlib.pyplot as plt

# Ouvrir le fichier CSV
bd = pd.read_csv("liste01.csv", encoding_errors="ignore", sep=";", index_col=False, encoding="cp1252", names=["ref", "date", "groupe_postes", "id_user", "login_user", "id_doc", "type_consultation", "type_acces"])
compt_ssr=0
compt_sej=0
compt_doc=0
compt_con=0
for element in bd["type_consultation"]:
    if element[:3] == "SSR" :
        compt_ssr +=1
    elif element == "séjour" :
        compt_sej +=1
    elif element == "document":
        compt_doc +=1
    elif element == "consultation":
        compt_con +=1
plt.figure(figsize=(10,10))
#création du camembert avec les compteurs comme valeurs et le type d'accès comme titre
plt.pie([compt_ssr, compt_sej, compt_doc, compt_con], labels = ["SSR: "+str(compt_ssr), "séjour: "+str(compt_sej), "document: "+str(compt_doc), "consultation: "+str(compt_con) ], normalize = True, autopct="%1.0f%%",explode=[0.2,0.1,0,0.3])
# Variable pour éviter la ligne de la légende
var_legende = plt.legend()

#Niveau4.3
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import numpy as np

#ouverture du fichier grâce a la méthode read_csv de pandas
bd = pd.read_csv("liste01.csv", encoding_errors="ignore", sep=";", index_col=False, encoding="cp1252", names=["ref", "date", "groupe_postes", "id_user", "login_user", "id_doc", "type_consultation", "type_acces"])
#création de variable pour chaque type d'accès en fonction du jour
compt_modif_lun=0
compt_lect_lun=0
compt_crea_lun=0
compt_supp_lun=0

compt_modif_mar=0
compt_lect_mar=0
compt_crea_mar=0
compt_supp_mar=0

compt_modif_jeu=0
compt_lect_jeu=0
compt_crea_jeu=0
compt_supp_jeu=0

compt_modif_mer=0
compt_lect_mer=0
compt_crea_mer=0
compt_supp_mer=0

compt_modif_ven=0
compt_lect_ven=0
compt_crea_ven=0
compt_supp_ven=0

compt_modif_sam=0
compt_lect_sam=0
compt_crea_sam=0
compt_supp_sam=0

compt_modif_dim=0
compt_lect_dim=0
compt_crea_dim=0
compt_supp_dim=0

modif_total= 0
lect_total= 0
crea_total= 0
supp_total= 0
# Boucle multiconditionnel qui incrémente la variable compteur en fonction du type d'accès et du jour
for x in range(len(bd)):
    if (date.fromisoformat(bd["date"][x][:10])).weekday() == 0:
        if bd["type_acces"][x] == "accès en mode modification" :
            compt_modif_lun +=1
            modif_total+=1
        elif bd["type_acces"][x] == "accès en mode lecture" :
            compt_lect_lun +=1
            lect_total+=1
        elif bd["type_acces"][x] == "création" :
            compt_crea_lun +=1
            crea_total+=1
        elif bd["type_acces"][x] == "suppression" :
            compt_supp_lun +=1
            supp_total+=1
    elif (date.fromisoformat(bd["date"][x][:10])).weekday() == 1:
        if bd["type_acces"][x] == "accès en mode modification" :
            compt_modif_mar +=1
            modif_total+=1
        elif bd["type_acces"][x] == "accès en mode lecture" :
            compt_lect_mar +=1
            lect_total+=1
        elif bd["type_acces"][x] == "création" :
            compt_crea_mar +=1
            crea_total+=1
        elif bd["type_acces"][x] == "suppression" :
            compt_supp_mar +=1
            supp_total+=1
    elif (date.fromisoformat(bd["date"][x][:10])).weekday() == 2:
        if bd["type_acces"][x] == "accès en mode modification" :
            compt_modif_mer +=1
            modif_total+=1
        elif bd["type_acces"][x] == "accès en mode lecture" :
            compt_lect_mer +=1
            lect_total+=1
        elif bd["type_acces"][x] == "création" :
            compt_crea_mer +=1
            crea_total+=1
        elif bd["type_acces"][x] == "suppression" :
            compt_supp_mer +=1
            supp_total+=1
    elif (date.fromisoformat(bd["date"][x][:10])).weekday() == 3:
        if bd["type_acces"][x] == "accès en mode modification" :
            compt_modif_jeu +=1
            modif_total+=1
        elif bd["type_acces"][x] == "accès en mode lecture" :
            compt_lect_jeu +=1
            lect_total+=1
        elif bd["type_acces"][x] == "création" :
            compt_crea_jeu +=1
            crea_total+=1
        elif bd["type_acces"][x] == "suppression" :
            compt_supp_jeu +=1
            supp_total+=1
    elif (date.fromisoformat(bd["date"][x][:10])).weekday() == 4:
        if bd["type_acces"][x] == "accès en mode modification" :
            compt_modif_ven +=1
            modif_total+=1
        elif bd["type_acces"][x] == "accès en mode lecture" :
            compt_lect_ven +=1
            lect_total+=1
        elif bd["type_acces"][x] == "création" :
            compt_crea_ven +=1
            crea_total+=1
        elif bd["type_acces"][x] == "suppression" :
            compt_supp_ven +=1
            supp_total+=1
    elif (date.fromisoformat(bd["date"][x][:10])).weekday() == 5:
        if bd["type_acces"][x] == "accès en mode modification" :
            compt_modif_sam +=1
            modif_total+=1
        elif bd["type_acces"][x] == "accès en mode lecture" :
            compt_lect_sam +=1
            lect_total+=1
        elif bd["type_acces"][x] == "création" :
            compt_crea_sam +=1
            crea_total+=1
        elif bd["type_acces"][x] == "suppression" :
            compt_supp_sam +=1
            supp_total+=1
    elif (date.fromisoformat(bd["date"][x][:10])).weekday() == 6:
        if bd["type_acces"][x] == "accès en mode modification" :
            compt_modif_dim +=1
            modif_total+=1
        elif bd["type_acces"][x] == "accès en mode lecture" :
            compt_lect_dim +=1
            lect_total+=1
        elif bd["type_acces"][x] == "création" :
            compt_crea_dim +=1
            crea_total+=1
        elif bd["type_acces"][x] == "suppression" :
            compt_supp_dim +=1
            supp_total+=1

# Création du dictionnaire avec les valeurs des 4 types d'accès pour chaque jour
data = {'Lundi':(compt_modif_lun,compt_lect_lun,compt_crea_lun,compt_supp_lun),
        'Mardi':(compt_modif_mar,compt_lect_mar,compt_crea_mar,compt_supp_mar),
        'Mercredi':(compt_modif_mer,compt_lect_mer,compt_crea_mer,compt_supp_mer),
        'Jeudi':(compt_modif_jeu,compt_lect_jeu,compt_crea_jeu,compt_supp_jeu),
        'Vendredi':(compt_modif_ven,compt_lect_ven,compt_crea_ven,compt_supp_ven),
        'Samedi':(compt_modif_sam,compt_lect_sam,compt_crea_sam,compt_supp_sam),
        'Dimanche':(compt_modif_dim,compt_lect_dim,compt_crea_dim,compt_supp_dim)}

# Création de liste et de variables
modification = []
lecture = []
creation = []
suppression = []

# Boucle qui permet de compter chaque type d'accès en fonction du jour grâce au dictionnaire
for day, counts in data.items():
    modification.append(counts[0]/modif_total*100)
    lecture.append(counts[1]/lect_total*100)
    creation.append(counts[2]/crea_total*100)
    suppression.append(counts[3]/supp_total*100)

# Utilisation de numpy pour la taille des collones du graphqieu en fonction de la taille du dictionnaire
x = np.arange(len(data))

# Taille du graphique
plt.figure(figsize=(9, 6))

# Création de chaque barre pour chaque type d'accès et chaque jour
plt.bar(x - 0.3, modification, width=0.2, label='Modification')
plt.bar(x - 0.1, lecture, width=0.2, label='Lecture')
plt.bar(x + 0.1, creation, width=0.2, label='Création')
plt.bar(x + 0.3, suppression, width=0.2, label='Suppression')

#Utilisation du dictionnaire avec la clés du dictionnaire(les jours) pour les jours sous chaque 4 collones
plt.xticks(x, data.keys())

# Mettre la légende en haut a gauche
plt.legend(loc="upper left")
# Nom de l'axe x
plt.xlabel('Jour de la semaine')
# Nom de l'axe y
plt.ylabel('Pourcentage du nombre de connections par semaine')
# Affichage du graphique
plt.show()

#Niveau5.2
import datetime
import pandas as pd
import matplotlib.pyplot as plt

#ouverture du fichier grâce a la méthode read_csv de pandas
bd = pd.read_csv("liste01.csv", encoding_errors="ignore", sep=";", index_col=False, encoding="cp1252", names=["ref", "date", "groupe_postes", "id_user", "login_user", "id_doc", "type_consultation", "type_acces"])

#fonction pour convertire les heures minutes secondes en secondes
def heure_en_secondes(time_string):
    # convertir la chaîne de temps en objet datetime
    heure_objet = datetime.datetime.strptime(time_string, "%H:%M:%S")
    # extraire les heures, minutes et secondes de l'objet datetime
    heures = heure_objet.hour
    minutes = heure_objet.minute
    secondes = heure_objet.second
    # calculer le nombre total de secondes
    total_seconds = (heures * 3600) + (minutes * 60) + secondes
    return total_seconds


total=0
plage1={'0h':0,'1h':0,'2h':0,'3h':0,'4h':0,'5h':0,'6h':0}
plage2={'6h':0,'7h':0,'8h':0,'9h':0,'10h':0,'11h':0,'12h':0}
plage3={'12h':0,'13h':0,'14h':0,'15h':0,'16h':0,'17h':0,'18h':0}
plage4={'18h':0,'19h':0,'20h':0,'21h':0,'22h':0,'23h':0}
for i in range(len(bd)):
    if 0<=heure_en_secondes(bd["date"][i][-8:]) < 3600:
        plage1['0h']+=1
        total+=1
    elif 3600<=heure_en_secondes(bd["date"][i][-8:]) < 7200:
        plage1['1h']+=1
        total+=1
    elif 7200<=heure_en_secondes(bd["date"][i][-8:]) < 10800:
        plage1['2h']+=1
        total+=1
    elif 10800<=heure_en_secondes(bd["date"][i][-8:]) < 14400:
        plage1['3h']+=1
        total+=1
    elif 14400<=heure_en_secondes(bd["date"][i][-8:]) < 18000:
        plage1['4h']+=1
        total+=1
    elif 18000<=heure_en_secondes(bd["date"][i][-8:]) < 21600:
        plage1['5h']+=1
        total+=1
    elif 21600<=heure_en_secondes(bd["date"][i][-8:]) < 25200:
        plage1['6h']+=1
        plage2['6h']+=1
        total+=1
    elif 25200<=heure_en_secondes(bd["date"][i][-8:]) < 28800:
        plage2['7h']+=1
        total+=1
    elif 28800<=heure_en_secondes(bd["date"][i][-8:]) < 32400:
        plage2['8h']+=1
        total+=1
    elif 32400<=heure_en_secondes(bd["date"][i][-8:]) < 36000:
        plage2['9h']+=1
        total+=1
    elif 36000<=heure_en_secondes(bd["date"][i][-8:]) < 39600:
        plage2['10h']+=1
        total+=1
    elif 39600<=heure_en_secondes(bd["date"][i][-8:]) < 43200:
        plage2['11h']+=1
        total+=1
    elif 43200<=heure_en_secondes(bd["date"][i][-8:]) < 46800:
        plage2['12h']+=1
        plage3['12h']+=1
        total+=1
    elif 46800<=heure_en_secondes(bd["date"][i][-8:]) < 50400:
        plage3['13h']+=1
        total+=1
    elif 50400<=heure_en_secondes(bd["date"][i][-8:]) < 54000:
        plage3['14h']+=1
        total+=1
    elif 54000<=heure_en_secondes(bd["date"][i][-8:]) < 57600:
        plage3['15h']+=1
        total+=1
    elif 57600<=heure_en_secondes(bd["date"][i][-8:]) < 61200:
        plage3['16h']+=1
        total+=1
    elif 61200<=heure_en_secondes(bd["date"][i][-8:]) < 64800:
        plage3['17h']+=1
        total+=1
    elif 64800<=heure_en_secondes(bd["date"][i][-8:]) < 68400:
        plage3['18h']+=1
        plage4['18h']+=1
        total+=1
    elif 68400<=heure_en_secondes(bd["date"][i][-8:]) < 72000:
        plage4['19h']+=1
        total+=1
    elif 72000<=heure_en_secondes(bd["date"][i][-8:]) < 75600:
        plage4['20h']+=1
        total+=1
    elif 75600<=heure_en_secondes(bd["date"][i][-8:]) < 79200:
        plage4['21h']+=1
        total+=1
    elif 79200<=heure_en_secondes(bd["date"][i][-8:]) < 82800:
        plage4['22h']+=1
        total+=1
    elif 82800<=heure_en_secondes(bd["date"][i][-8:]):
        plage4['23h']+=1
        total+=1


# Créationde liste cles et valeur avec les identifiant du top 10 et les valeurs des identifiants
cles1 = [x[0] for x in plage1.items()]
valeurs1 = [x[1] for x in plage1.items()]
cles2 = [x[0] for x in plage2.items()]
valeurs2 = [x[1] for x in plage2.items()]
cles3 = [x[0] for x in plage3.items()]
valeurs3 = [x[1] for x in plage3.items()]
cles4 = [x[0] for x in plage4.items()]
valeurs4 = [x[1] for x in plage4.items()]

plt.figure(figsize=(12, 9))
plt.plot(cles1, valeurs1)
plt.plot(cles2, valeurs2)
plt.plot(cles3, valeurs3)
plt.plot(cles4, valeurs4)
plt.xticks(rotation=-45)
plt.xlabel("Plage horaire")
plt.ylabel('Nombre de consultation en pourcentage')
plt.show()

#Niveau5.3
import pandas as pd
import heapq
import matplotlib.pyplot as plt
#ouverture du fichier grâce a la méthode read_csv de pandas
bd = pd.read_csv("liste01.csv", encoding_errors="ignore", sep=";", index_col=False, encoding="cp1252", names=["ref", "date", "groupe_postes", "id_user", "login_user", "id_doc", "type_consultation", "type_acces"])
# Créatiob du dictionnaire vide
dico={}
# Boucle pour ajouter l'identifiant au dictionnaire s'il n'est pas présent, s'il l'est sa valeur est incrémenter de 1
for i in range(len(bd)):
    if bd["id_doc"][i] in dico:
        dico[bd["id_doc"][i]]+=1
    else:
        dico.update({bd["id_doc"][i]: 1})

# Création du Top 10 contenant les 10 plus grandes valeurs
dico= heapq.nlargest(10, dico.items(), key=lambda x: x[1])

# Créationde liste cles et valeur avec les identifiant du top 10 et les valeurs des identifiants
cles = [str(x[0]) for x in dico]
valeurs = [x[1] for x in dico]
print(valeurs)
# Taille de la figure
plt.figure(figsize=(12, 9))
# Création du graphique en fonction des clés et valeurs
plt.bar(cles, valeurs)
# Nom de l'axe x
plt.xlabel('Documents')
# Nom de l'axe y
plt.ylabel('Nombre de consultation')
# Affichage du graphique
plt.show()

#Option1
import pandas as pd
import heapq
import matplotlib.pyplot as plt
df = pd.read_csv("liste01.csv", encoding_errors="ignore", sep=";", index_col=False, encoding="cp1252", names=["ref", "date", "groupe_postes", "id_user", "login_user", "id_doc", "type_consultation", "type_acces"])
dico={}
for i in range(len(bd)):
    if bd["id_user"][i] in dico:
        dico[bd["id_user"][i]]+=1
    else:
        dico.update({bd["id_user"][i]: 1})

dico = heapq.nlargest(10, dico.items(), key=lambda x: x[1])
cles = [str(x[0]) for x in dico]
valeurs = [x[1] for x in dico]

plt.figure(figsize=(12, 9))
plt.plot(cles, valeurs)
plt.xticks(rotation=-45)
plt.xlabel("Les 10 login d'utilsateur qui consultent le plus")
plt.ylabel('Nombre de consultation')
plt.show()