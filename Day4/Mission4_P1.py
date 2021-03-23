"""
Adevent of code 2020
Day4 Part1
The point of this exercise is to pass throught a lot of fictional passports and to verify every
information written on them :

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)


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
            #count = number of good information
            if file[i][j] == "ecl":
                count+=1
            elif file[i][j] == "pid":
                count+=1
            elif file[i][j] == "eyr":
                count+=1
            elif file[i][j] == "hcl":
                count+=1
            elif file[i][j] == "byr":
                count+=1
            elif file[i][j] == "iyr":
                count+=1
            elif file[i][j] == "hgt":
                count+=1               
        i+=1#add 1 to i to get to another line
        
    if count == 7:#at the end of a passport, the number of good information must be 7 to confirm that it is legal
        total +=1#total of good passports
    i+=1
print(total)#print the total of good passports at the end of all the test
        