"""
Advent 2020
Mission 6 Part 2:
The point of this mission is to count every different caracter into different group seperate by empty line
and sum all the count to get the answer.
"""
file = open("input.txt").read().split("\n\n")
file = [i.splitlines() for i in file]

rep = 0
first = []
for x in range(len(file)):
    rep += len(first)
    first = []
    main = []
    count = 0
    for y in file[x]:
        main.append(set(y))
        
    for k in range(len(main)):
        if count == 0:
            first = main[k]
            count += 1
        else:
            first = first.intersection(main[k])
            
print(rep)
    
        
        
