from copy import deepcopy


data = open("202209i.txt","r").read().split("\n")

tailposes = {"0,0":1}

headpos = [0,0]
tailpos = [0,0]

def moveu(hp, tp):
    headpos = deepcopy(hp)
    tailpos = deepcopy(tp)
    headpos[1] +=1
    if headpos[1] - 2 == tailpos[1]:
        tailpos[1]+=1
        if headpos[0] < tailpos[0]:
            tailpos[0] -=1
        if headpos[0] > tailpos[0]:
            tailpos[0] +=1
    return headpos,tailpos

def moved(hp, tp):
    headpos = deepcopy(hp)
    tailpos = deepcopy(tp)
    headpos[1] -=1
    if headpos[1] + 2 == tailpos[1]:
        tailpos[1]-=1
        if headpos[0] < tailpos[0]:
            tailpos[0] -=1
        if headpos[0] > tailpos[0]:
            tailpos[0] +=1
    return headpos,tailpos

def movel(hp, tp):
    headpos = deepcopy(hp)
    tailpos = deepcopy(tp)
    headpos[0] -=1
    if headpos[0] + 2 == tailpos[0]:
        tailpos[0]-=1
        if headpos[1] < tailpos[1]:
            tailpos[1] -=1
        if headpos[1] > tailpos[1]:
            tailpos[1] +=1
    return headpos,tailpos


def mover(hp, tp):
    headpos = deepcopy(hp)
    tailpos = deepcopy(tp)
    headpos[0] +=1
    if headpos[0] - 2 == tailpos[0]:
        tailpos[0]+=1
        if headpos[1] < tailpos[1]:
            tailpos[1] -=1
        if headpos[1] > tailpos[1]:
            tailpos[1] +=1
    return headpos,tailpos

def move(hp, tp, dir, num, tps):
    headpos = deepcopy(hp)
    tailpos = deepcopy(tp)

    for i in range(num):
        if dir == "U":
            headpos,tailpos = moveu(headpos,tailpos)
        if dir == "D":
            headpos,tailpos = moved(headpos,tailpos)
        if dir == "L":
            headpos,tailpos = movel(headpos,tailpos)
        if dir == "R":
            headpos,tailpos = mover(headpos,tailpos)
        tps[str(tailpos[0]) + "," + str(tailpos[1])] = 1
    print(tps.keys())
    return headpos,tailpos,tps

for instruction in data:
    dr = instruction[0]
    n = int(instruction[1:])
    headpos,tailpos,tailposes = move(headpos,tailpos,dr,n,tailposes)


print(len(tailposes.keys()))

