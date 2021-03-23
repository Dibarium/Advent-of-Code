"""
Adevent of code 2020
Day4 Part2
The point of this exercise is to pass throught a lot of fictional passports and to verify every
information written on them :

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

Every passports are separate by an empty line
I should have split the txt with \n\n it would have been much easyier
"""
import re
file = open("input.txt", "r").read().split("\n")#Open the input read it and split at every line break
i=0
total = 0
while i <= len(file)-1:#End when all the lines of the txt have been read 
    count = 0
    while file[i] != "":#If there is an empty line, reset count and pass to another passport
        file[i] = re.split(':| ' ,file[i])#Split every ":" and space
         
        for j in range(len(file[i])):
            #Basically, verify each term of the array and make it match with
            #one of the 7 elements we have to verify.
            #I used j+1 because it is the term after the current term so this is where the information is
            #count = number of good information
            if file[i][j] == "ecl":
                #verify if the information is one of those values
                if file[i][j+1] in ["amb", "blu", "brn","gry","grn","hzl","oth"]:
                    count+=1
            elif file[i][j] == "pid":
                #the length must be 9
                if len(file[i][j+1]) == 9:
                    count+=1
            elif file[i][j] == "eyr":
                #Must be between 2020 and 2030 include
                if int(file[i][j+1])>=2020 and int(file[i][j+1])<=2030:
                    count+=1
            elif file[i][j] == "hcl":
                #Must start by an # and followed by 6 digit numbers
                if file[i][j+1][0]=="#" and len(file[i][j+1])==7 :
                    count+=1
            elif file[i][j] == "byr":
                #Must be between 1920 and 2002 include
                if int(file[i][j+1]) >= 1920 and int(file[i][j+1]) <= 2002:
                    count+=1
            elif file[i][j] == "iyr":
                #Must be between 2010 and 2020 include
                if int(file[i][j+1]) >= 2010 and int(file[i][j+1]) <= 2020:
                    count+=1
            elif file[i][j] == "hgt":
                #if the last 2 letters are "cm"
                if file[i][j+1][-1]=="m" and file[i][j+1][-2]=="c":
                    file[i][j+1] = file[i][j+1].translate({ord(i): None for i in 'cm'})#delete letters "c" and "m"
                    #Must be between 150 and 193 include
                    if int(file[i][j+1]) >= 150 and int(file[i][j+1]) <= 193:
                        count+=1
                #if the last 2 letters are "in"
                elif file[i][j+1][-1]=="n" and file[i][j+1][-2]=="i":
                    file[i][j+1] = file[i][j+1].translate({ord(i): None for i in 'in'})#delete letters "i" and "n"
                    #Must be between 59 and 76 include
                    if int(file[i][j+1]) >= 59 and int(file[i][j+1]) <= 76:
                        count+=1               
        i+=1#add 1 to i to get to another line
        
    if count == 7:#at the end of a passport, the number of good information must be 7 to confirm that it is legal
        total +=1#total of good passports
    i+=1
print(total)#print the total of good passports at the end of all the test
        
