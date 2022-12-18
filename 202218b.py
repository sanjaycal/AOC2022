from copy import deepcopy
import networkx
import string
import ast
import z3
import matplotlib.pyplot as plt

data = open("202218i.txt","r").read().split("\n")

cubes = [[[0 for x in range(21)] for x in range(21)] for x in range(21)]

cubeposlist = []

for i in data:
    values = i.split(",")
    x = int(values[0])
    y = int(values[1])
    z = int(values[2])
    cubeposlist.append([x,y,z])
    cubes[x][y][z] = 1

print(len(cubeposlist))


outerPoses = [[0,0,0]]


k = 0
while k < 3:
    ta = []
    for pos in outerPoses:
        toAdd = []
        x = pos[0]
        y = pos[1]
        z = pos[2]
        if x ==0:
            toAdd.append([x+1,y,z])
        elif x == 20:
            toAdd.append([x-1,y,z])
        else:
            toAdd.append([x+1,y,z])
            toAdd.append([x-1,y,z])
        
        if y ==0:
            toAdd.append([x,y+1,z])
        elif y == 20:
            toAdd.append([x,y-1,z])
        else:
            toAdd.append([x,y+1,z])
            toAdd.append([x,y-1,z])
        
        if z ==0:
            toAdd.append([x,y,z+1])
        elif z == 20:
            toAdd.append([x,y,z-1])
        else:
            toAdd.append([x,y,z+1])
            toAdd.append([x,y,z-1])

        for i in toAdd:
            if cubes[i[0]][i[1]][i[2]] ==0 and not i in outerPoses:
                ta.append(i)
    if len(ta) == 0:
        break
    c = 0
    for i in ta:
        if not i in outerPoses:
            c+=1
            outerPoses.append(i)
    if c == 0:
        k += 1


total = 0

t = []

for i in outerPoses:
    x = i[0]
    y = i[1]
    z = i[2]
    n = 0
    try:
        n += cubes[x + 1][y][z]
    except:
        pass
    try:
        n += cubes[x - 1][y][z]
    except:
        pass
    try:
        n += cubes[x][y + 1][z]
    except:
        pass
    try:
        n += cubes[x][y - 1][z]
    except:
        pass
    try:
        n += cubes[x][y][z + 1]
    except:
        pass
    try:
        n += cubes[x][y][z - 1]
    except:
        pass
    
    t.append(n)

    total += n

print(sum(t) + 5)



