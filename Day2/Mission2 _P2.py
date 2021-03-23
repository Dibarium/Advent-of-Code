import re

def ver(liste):
    vrai = 0
    liste = liste.replace('-', ' ')
    liste = re.split(': | |  ' ,liste)
    print(liste)
    for i in range(0, len(liste[3])):
        if liste[3][i] == liste[2] :
            if i == int(liste[0])-1:
                vrai += 1
            elif i == int(liste[1])-1:
                vrai += 1
    if vrai == 1:
        return True
    else:
        return False
    
        

f = open("input.txt", "r" )
liste = []
line = f.read()
liste.append(line.split("\n"))

verif = False
reussite = 0

for i in range(0,1000):
    mdp = ver(liste[0][i])
    if mdp == True:
        reussite += 1
print(reussite)