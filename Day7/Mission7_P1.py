file = open("input.txt").read().split("\n")
main = {}
name = []
for i in range(0,len(file)-1):
    file[i] = file[i].split(" ")
    if file[i][0]+file[i][1] not in name:
        name.append(file[i][0]+file[i][1])
print(name)

for j in range(0,len(file)):
    for k in range(2,len(file[j])-1):
        if file[j][0]+file[j][1]not in name :
             main[file[j][0]+file[j][1]] = file[j][k]+file[j][k+1]
                
    