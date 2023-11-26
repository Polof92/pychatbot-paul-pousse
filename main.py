import os
import math

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
# donne le nom des fichiers qui sont dans speeches

directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)
#appel de la fonction 

def nom_president():
    a = files_names
    for i in range(len(a)):
        a[i] = a[i][11:len(a[i])-4]
        if a[i][len(a[i])-1] == '1' or a[i][len(a[i])-1] == '2':
            a[i] = a[i][:len(a[i])-1]
    return a
tab = nom_president()
print(tab)
#créer une liste avec le nom des présidents 


def prenom(a):
    for i in range(len(a)):
        if a[i] == "Chirac":
            a[i] = "Jacques"
        if a[i] == "Giscard dEstaing":
            a[i] = "Valérie"
        if a[i] == "Hollande":
            a[i] = "FrançoisH"
        if a[i] == "Macron":
            a[i] = "Emmanuel"
        if a[i] == "Mitterrand":
            a[i] = "FrançoisM"
        if a[i] == "Sarkozy":
            a[i] = "Nicolas"
    print(set(a))
prenom(tab)
#remplace leurs noms par leurs prénoms en elevant les doublons 

def convertir(f, f2):
    with open(f, "r",) as f3, open(f2, "w") as f4:
        c = f3.readlines()
        for i in range(len(c)):
            a = ""
            for j in range(len(c[i])):
                if (ord(c[i][j]) > 64) and (ord(c[i][j]) < 91):
                    a += chr(ord(c[i][j])+32)
                else:
                    a += c[i][j]
            f4.write(a)
    return f4
#copie le texte dans un autre fichier en elevant les majuscules

def fichier():
    a=os.listdir("./speeches")
    print(a)
    b=[]
    for i in range(len(a)):
        c="Cleaned_"
        for j in range(11,len(a[i])):
            c+=a[i][j]
        b.append(c)
    return b
print(fichier())
#créer une liste avec le nom des fchiers qu'on a créé

def del_pon(f):
    with (open(f, "r") as f3):
        c = f3.readlines()
        with open(f, "w") as f3:
            a = ""
            for i in range(len(c)):
                for j in range(len(c[i])):
                    if (c[i][j] == ',') or (c[i][j] == '.') or (c[i][j] == '!') or (c[i][j] == '-') or (c[i][j] == ':') or (c[i][j] == ';') :
                        a += ''
                    elif (c[i][j] == ',') or (c[i][j] == chr(39)):
                        a += ' '
                    else:
                        a += c[i][j]
            f3.write(a)
    return f3
#enlève la ponctuation



def creation():
    a=fichier()
    c=os.listdir("./speeches")
    for i in range(len(a)):
        b="./cleaned/"+a[i]
        d="./speeches/"+c[i]
        with open(b,"w") as f1:
            convertir(d,b)
            del_pon(b)
creation()
# enlève les majuscules
def list_of_files2(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

directory = "./cleaned"
files_names2 = list_of_files2(directory, "txt")
print (files_names2)

def tf(f1):
    with open(f1,"r",encoding="utf-8") as f:
        d={}
        a=f.readlines()
        b=[]
        for i in range(len(a)):
            j = 0
            while j<len(a[i]):
                c=""
                while a[i][j]!=" " and j<len(a[i])-1:
                    c+=a[i][j]
                    j += 1
                b.append(c)
                j+=1
    for i in range(len(b)):
        if b[i] not in d:
            d[b[i]]=1
        else:
            d[b[i]]+=1
    return d
#calcul le score TF
def test_tf():
    a=0
    b=files_names2
    listd=[]
    for i in range(len(files_names2)):
        listd.append(tf("./cleaned/" + files_names2[i]))
    return listd
print(test_tf())
def idf_mot(mot):
    c=0
    a=test_tf()
    for i in range(len(a)):
        if mot in a[i]:
            c+=1
    c=math.log(1/(c/len(a)),10)
    return c
    #fais l'idf d'un mot
def idf():
    a=test_tf()
    b=[]
    for i in  range(len(a)):
        for cle in a[i].keys():
            if cle not in b:
                b.append(cle)
    return b
    #fais une liste de tous les mots utilisés dans les fichiers sans doublons
def idf2():

    c=[]
    b=idf()
    for i in range(len(b)):
        c.append(idf_mot(b[i]))
    return c
#print(idf())
#fais une liste de l'idf de tous les mots utilisés dans les fichiers sans doublons
def tf1():
    a=test_tf()
    b=idf()
    c=idf2()
    print(b)
    print(c)
    for i in range(len(b)):
        for j in range(len(a)):
            if b[i] in a[j]:
                a[j][b[i]]=c[i]*a[j][b[i]]
    return a
    #calcule le tf-idf de chaque mot de chaque fichier
#print(tf1())
def matrice():
   a=idf()
   tab=[]
   b=tf1()
   for i in range(len(a)):
       tab.append([])
       for j in range(len(b)):
            if a[i] in b[j]:
                tab[i].append(b[j][a[i]])
            else:
                tab[i].append(-1)
       tab[i].append(a[i])
   return tab
#print(matrice())

#fais une matrice de tous les mots avec leur tf-idf dans chaque document


def affichage_matrice(tab):
    for i in range(len(tab)):
        print(tab[i])
tab=matrice()
affichage_matrice(tab)
 #affiche la matrice précédente                              
def mot_pas_important():
    a=matrice()
    b=[]
    for i in range(len(a)):
        s=0
        t=[]
        for j in range(len(a[i])-1):
           if a[i][j]!=0:
               s+=a[i][j]
        if s==0:
            b.append(a[i][j+1])
    return b
#print(mot_pas_important())
#renvoir les mots les plus utilisés
def mot_plus_important():
    a = matrice()
    b = []
    for i in range(len(a)):
        s = 0
        t = []
        for j in range(len(a[i]) - 1):
            if a[i][j] != 0:
                s += a[i][j]
        if s >=2:
            b.append(a[i][j + 1])
    return b
print(mot_plus_important())
#renvoie les mots les moins utilisés
def fusion(d1,d2):
    f={}
    for cle,valeur in d1.items():
        f[cle]=valeur
    for cle2,valeur2 in d2.items():
        if cle2 in f:
            f[cle2]+=valeur2
        else:
            f[cle2]=valeur
    return f
    #fais la fusion de deux dictionnaires
def chirac():
    a=test_tf()
    b=fusion(a[0],a[1])
    ivaleur=0
    icle=0
    for cle,valeur in b.items():
        if valeur>ivaleur:
            ivaleur=valeur
            icle=cle
    return icle        
chirac()
directory = "./speeches"
files_names = list_of_files(directory, "txt")
print (files_names)
    #renvoie les mots les plus prononcés par Chirac
def nation():
    a=test_tf()
    imax=0
    c=-1
    d = nom_president()
    f=[]
    for i in range(len(a)):
        if 'nation' in a[i]:
            f.append(d[i])

    for i in range(len(a)):
        for cle,valeur in a[i].items():
            if 'nation' in a[i] and valeur>imax:
                imax=valeur
                c=i
    return set(f),d[c]
    #renvoie le nom du président qui a le plus prononcé le mot nation
    #on peut transformer cette fonction pour qu'elle marche avec n'importe quel mot si on rajoute un argument et qu'on remplace "nation" par l'argument
