file = open("input.txt", "r").read().split("\n")

trees = []

for i in range(1, 5):
    treescount = 0
    pos_y = 0
    pos_x = 0
    while pos_y != 322:
        if i == 1:
            pos_y += 1
            pos_x += 1
        elif i == 2:
            pos_y += 1
            pos_x += 5
        elif i == 3:
            pos_y += 1
            pos_x += 7
        elif i == 4:
            pos_y += 2
            pos_x += 1
            
        if pos_x >= 31:
            pos_x -= 31
        if file[pos_y][pos_x] == "#":
            treescount += 1
        print(pos_y)
    
    trees.append(treescount)
print(trees)