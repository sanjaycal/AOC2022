from copy import deepcopy
import networkx
import string
import ast

data = open("202214i.txt","r").read().split("\n")

map = [[0 for x in range(1000)] for x in range(1000)]

print(len(map[0]))

sandSource = [500,0]

my = 0

for i in data:
    path = i.split(" -> ")
    for item in range(len(path[1:])):
        p1 = path[item].split(",")
        p1[0] = int(p1[0])
        p1[1] = int(p1[1])
        p2 = path[item+1].split(",")
        p2[0] = int(p2[0])
        p2[1] = int(p2[1])

        my = max(my, p1[1], p2[1])

        print(p2)

        if p1[0] != p2[0]:
            for ii in range(p1[0] ,p2[0]+(1 if p2[0]>p1[0] else -1), 1 if p2[0]>p1[0] else -1):
                map[ii][p1[1]] = 1
        if p1[1] != p2[1]:
            for ii in range(p1[1],p2[1]+(1 if p2[1]>p1[1] else -1), 1 if p2[1]>p1[1] else -1):
                map[p1[0]][ii] = 1

my = my +2

print("a")

for i in range(1000):
    map[i][my] = 1

print("a")

o = ""
for i in range(10):
    s = ""
    for j in range(494,504):
        s += str(map[j][i])
    o+= s + "\n"

print(o)
def update(pos, map):
    if map[pos[0]][pos[1]+1] == 0:
        return [pos[0],pos[1]+1]
    if map[pos[0]-1][pos[1]+1] == 0:
        return [pos[0]-1,pos[1]+1]
    if map[pos[0]+1][pos[1]+1] == 0:
        return [pos[0]+1,pos[1]+1]
    return "w"

def addSand(start, map):
    global my
    sandpos = deepcopy(start)
    c = 0
    while True:
        a = update(sandpos,map)
        if a == "w":
            break
        sandpos = a
        c +=1
        if c > my:
            return "done"
    if sandpos == sandSource:
        return "done"
    return sandpos

c = 0

while True:
    a = addSand(sandSource,map)
    if a!="done":
        map[a[0]][a[1]] = 2
        c+=1
    if a == "done":
        break
    print(c)


print(c+1)
    
    