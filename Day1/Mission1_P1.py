"""
Advent of code 2020
Day1 Part1
The point of this exercise is to find two entries that sum to 2020 and then multiply
them to entray to get the answer
"""

#get file object
import random as r
f = open("input.txt", "r")
liste = []
while(True):
	#read next line
	line = f.readline()
	#if line is empty, you are done with all lines in the file
	if not line:
		break
	#you can access the line
	liste.append(line.strip())

#Double loop to try every sum in the array
for i in range(len(liste)):
    for y in range(len(liste)):
        
        if int(liste[i])+int(liste[y]) == 2020:
            print(int(liste[i])*int(liste[y]))


f.close
