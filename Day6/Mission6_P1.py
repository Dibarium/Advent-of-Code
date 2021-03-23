"""
Advent 2020
Mission 6 Part 1:
The point of this mission is to count every different caracter into different group seperate by empty line
and sum all the count to get the answer.
"""
file = open("input.txt").read().split("\n")
caracter = []
question =[]
for x in range(len(file)):#pass throught every line of the file.
    if len(file[x]) == 0 :#If a line is empty, keep the number of different caracter and reset the array.
        question.append(len(caracter))
        caracter = []
    else:
        for y in range(len(file[x])):
            if caracter == []:#add the first caracter of the line if caracter is empty cause the letter can't double if it's empty
                caracter.append(file[x][y])
            if file[x][y] not in caracter:#If the caracter is not contain in the array of all different caracter add
                caracter.append(file[x][y])
            
                
                
count = 0         
for h in range(len(question)):#add every length of question of every group
    count+= question[h]
print(count)