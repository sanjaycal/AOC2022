from copy import deepcopy
import string
import ast

data = open("202223i.txt","r").read().split("\n")

mp = []
elvespos = {}
elvesOrder = ["N","S","W","E"]
elfRequest = {}

for i in data:
    a = []
    for j in i:
        if j==".":
            a.append(0)
        else:
            a.append(1)
    mp.append(a)

c = 0


for i in range(len(mp)):
    for j in range(len(mp[i])):
        if mp[i][j] == 1:
            elvespos[c] = [j,i]
            c+=1


def checkNorth(elfpos):
    canNorth = {}
    for i in elfpos.keys():
        NW = [elfpos[i][0]-1, elfpos[i][1]-1] in elfpos.values()
        N = [elfpos[i][0], elfpos[i][1]-1] in elfpos.values()
        NE = [elfpos[i][0]+1, elfpos[i][1]-1] in elfpos.values()

        if NW + N + NE == 0:
            canNorth[i] = [elfpos[i][0], elfpos[i][1]-1]
        else:
            canNorth[i] = 0
    return canNorth

def checkSouth(elfpos):
    canSouth = {}
    for i in elfpos.keys():
        SW = [elfpos[i][0]-1, elfpos[i][1]+1] in elfpos.values()
        S = [elfpos[i][0], elfpos[i][1]+1] in elfpos.values()
        SE = [elfpos[i][0]+1, elfpos[i][1]+1] in elfpos.values()

        if SW + S + SE == 0:
            canSouth[i] = [elfpos[i][0], elfpos[i][1]+1]
        else:
            canSouth[i] = 0
    return canSouth

def checkEast(elfpos):
    canEast = {}
    for i in elfpos.keys():
        NE = [elfpos[i][0]+1, elfpos[i][1]-1] in elfpos.values()
        E = [elfpos[i][0]+1, elfpos[i][1]] in elfpos.values()
        SE = [elfpos[i][0]+1, elfpos[i][1]+1] in elfpos.values()

        if NE + E + SE == 0:
            canEast[i] = [elfpos[i][0]+1, elfpos[i][1]]
        else:
            canEast[i] = 0
    return canEast

def checkWest(elfpos):
    canWest = {}
    for i in elfpos.keys():
        NW = [elfpos[i][0]-1, elfpos[i][1]-1] in elfpos.values()
        W = [elfpos[i][0]-1, elfpos[i][1]] in elfpos.values()
        SW = [elfpos[i][0]-1, elfpos[i][1]+1] in elfpos.values()

        if NW + W + SW == 0:
            canWest[i] = [elfpos[i][0]-1, elfpos[i][1]]
        else:
            canWest[i] = 0
    return canWest

def checkEmpty(elfpos):
    canMove = {}
    for i in elfpos.keys():
        NW = [elfpos[i][0]-1, elfpos[i][1]-1] in elfpos.values()
        W = [elfpos[i][0]-1, elfpos[i][1]] in elfpos.values()
        SW = [elfpos[i][0]-1, elfpos[i][1]+1] in elfpos.values()
        NE = [elfpos[i][0]+1, elfpos[i][1]-1] in elfpos.values()
        E = [elfpos[i][0]+1, elfpos[i][1]] in elfpos.values()
        SE = [elfpos[i][0]+1, elfpos[i][1]+1] in elfpos.values()
        S = [elfpos[i][0], elfpos[i][1]+1] in elfpos.values()
        N = [elfpos[i][0], elfpos[i][1]-1] in elfpos.values()

        v = N + S + E + W + NE + NW + SE + SW

        if v==0:
            canMove[i] = 1
        else:
            canMove[i] = 0
    return canMove
    

for iii in range(10000000):
    elfRequest = {}

    cn = checkNorth(elvespos)
    cs = checkSouth(elvespos)
    ce = checkEast(elvespos)
    cw = checkWest(elvespos)
    cm = checkEmpty(elvespos)

    for d in elvesOrder:
        if d=="N":
            for elf in cn.keys():
                if cn[elf] != 0 and not elf in elfRequest.keys():
                    elfRequest[elf] = cn[elf]
        if d=="S":
            for elf in cs.keys():
                if cs[elf] != 0 and not elf in elfRequest.keys():
                    elfRequest[elf] = cs[elf]
        if d=="E":
            for elf in ce.keys():
                if ce[elf] != 0 and not elf in elfRequest.keys():
                    elfRequest[elf] = ce[elf]
        if d=="W":
            for elf in cw.keys():
                if cw[elf] != 0 and not elf in elfRequest.keys():
                    elfRequest[elf] = cw[elf]
    
    goodRequests = {}

    for request in elfRequest.keys():
        if not(list(elfRequest.values()).count(elfRequest[request]) > 1) and cm[request] == 0:
            goodRequests[request] = elfRequest[request]
    
    for i in goodRequests.keys():
        elvespos[i] = goodRequests[i]

    if len(goodRequests.keys()) == 0:
        print(iii)
        break

    es = elvesOrder[0]

    elvesOrder = elvesOrder[1:]

    elvesOrder.append(es)
    print(iii)