"""
Advent of Code 2020
Mission 2 Part 1:
The point of this mission is to find if the passwords are correct. It must contain the letter before the ":"
and this letter must be present tat least *insert first number* and most *insert second number* . For exemple :

1-3 a: abcde
This password is right because it contain 1 "a"
1-3 b: cdefg
This password is wrong because it contain 0 "b" and must be present at least 1 time and at most 3 times
"""
import re

def ver(liste):
    count = 0
    liste = liste.replace('-', ' ')
    liste = re.split(': | |  ' ,liste)#Split "-" and ":"
    print(liste)
    for i in range(0, len(liste[3])):#For the length of the password
        if liste[3][i] == liste[2]:#Go throught every letters of the password and compare with the letter we're searching for
            count += 1 #add 1 to the count of the letter correspond
            
    #Search if the number of time the letters appear in the password and if it's present the good amount f times
    if count >= int(liste[0]) and count <= int(liste[1]):
        return True
    else:
        return False
    

f = open("input.txt", "r" )
liste = []
line = f.read()
liste.append(line.split("\n"))
reussite = 0

for i in range(0,1000):
    mdp = ver(liste[0][i])
    if mdp == True:
        #If the password if correct, add 1 to reussite
        reussite += 1
#print the amount of good password
print(reussite)
    