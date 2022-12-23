from copy import deepcopy
import networkx
import string
import ast
import z3
import matplotlib.pyplot as plt

data = open("202222i.txt","r").read().split("\n\n")


mp = []

mv = 0

for i in data[0].split("\n"):
    mv = max(mv, len(i))
    a = []
    for j in i:
        if j == " ":
            a.append(0)
        elif j==".":
            a.append(1)
        elif j=="#":
            a.append(2)
    mp.append(a)

for i in range(len(mp)):
    while len(mp[i])<mv:
        mp[i].append(0)

mp.append([0 for x in range(mv)])

mp.insert(0, [0 for x in range(mv)])

print(mp[0])
for i in range(len(mp)):
    mp[i].insert(0,0)
    mp[i].append(0)




spos = [1,1]

for i in range(len(mp[1])):
    if mp[0][i] == 1:
        spos[0] = i
        break


facing = 0

def moveRight(pos, map):
    npos = [pos[0] + 1, pos[1]]
    if map[npos[1]][npos[0]] == 1:
        return npos
    if map[npos[1]][npos[0]] == 2:
        return pos
    
    r = map[pos[1]]
    
    for i in range(len(r)):
        if r[i] == 1 or r[i] == 2:
            npos = [i,pos[1]]
            break
    if map[npos[1]][npos[0]] == 1:
        return npos
    if map[npos[1]][npos[0]] == 2:
        return pos

def moveLeft(pos, map):
    npos = [pos[0] - 1, pos[1]]
    if map[npos[1]][npos[0]] == 1:
        return npos
    if map[npos[1]][npos[0]] == 2:
        return pos

    r = map[pos[1]]
    
    for i in range(len(r)-1,-1,-1):
        if r[i] == 1 or r[i] == 2:
            npos = [i,pos[1]]
            break
    if map[npos[1]][npos[0]] == 1:
        return npos
    if map[npos[1]][npos[0]] == 2:
        return pos

def moveUp(pos, map):
    npos = [pos[0], pos[1] - 1]
    if map[npos[1]][npos[0]] == 1:
        return npos
    if map[npos[1]][npos[0]] == 2:
        return pos

    r = []

    for i in range(len(map)):
        r.append(map[i][npos[0]])
    
    for i in range(len(r)-1,-1,-1):
        if r[i] == 1 or r[i] == 2:
            npos = [pos[0],i]
            break
    if map[npos[1]][npos[0]] == 1:
        return npos
    if map[npos[1]][npos[0]] == 2:
        return pos

def moveDown(pos, map):
    npos = [pos[0], pos[1] + 1]
    if map[npos[1]][npos[0]] == 1:
        return npos
    if map[npos[1]][npos[0]] == 2:
        return pos

    r = []

    for i in range(len(map)):
        r.append(map[i][npos[0]])
    
    for i in range(len(r)):
        if r[i] == 1 or r[i] == 2:
            npos = [pos[0],i]
            break
    if map[npos[1]][npos[0]] == 1:
        return npos
    if map[npos[1]][npos[0]] == 2:
        return pos


ins = data[1]

instructions = []

stack = ""

for i in ins:
    if i !="L" and i != "R":
        stack += i
    else:
        instructions.append(int(stack))
        instructions.append(i)
        stack = ""

if len(stack) != 0:
    instructions.append(int(stack))


def move(pos, map, dir):
    if dir == 0:
        return moveRight(pos,map)
    if dir == 1:
        return moveDown(pos,map)
    if dir == 2:
        return moveLeft(pos,map)
    if dir == 3:
        return moveUp(pos,map)

print(instructions)

cpos = spos

dr = 0

for instruction in instructions:
    if type(instruction) == int:
        for i in range(instruction):
            cpos = move(cpos, mp, dr)
    else:
        if instruction == "R":
            dr = (dr+1)%4
        if instruction == "L":
            dr = (dr-1)%4

print(cpos[1] * 1000 + cpos[0] * 4 + dr)

    