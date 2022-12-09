from copy import deepcopy


data = open("202209i.txt","r").read().split("\n")

tailposes = set((0,0))

headpos = [0,0]
tailpos = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],]

def move(hp, tp):
    dx = hp[0] - tp[0]
    dy = hp[1] - tp[1]

    if abs(dx)>=2 and abs(dy)>=2:
        if hp[0] > tp[0]:
            tx = hp[0]-1
        else:
            tx = hp[0] + 1
        
        if hp[1] > tp[1]:
            ty = hp[1]-1
        else:
            ty = hp[1]+1
        tp = [tx,ty]
    elif abs(dx) >=2:
        if hp[0] > tp[0]:
            tx = hp[0]-1
        else:
            tx = hp[0] + 1
        
        tp = [tx, tp[1]]
    
    elif abs(dy) >=2:
        if hp[1] > tp[1]:
            ty = hp[1]-1
        else:
            ty = hp[1]+1
        tp = [tp[0],ty]
    return tp

for instruction in data:
    dr = instruction[0]
    n = int(instruction[1:])

    for i in range(n):
        if dr=="U":
            headpos[1] -=1
            tailpos[0] = move(headpos,tailpos[0])
            for i in range(9):
                tailpos[i+1] = move(tailpos[i], tailpos[i+1])

        if dr=="D":
            headpos[1] +=1
            tailpos[0] = move(headpos,tailpos[0])
            for i in range(9):
                tailpos[i+1] = move(tailpos[i], tailpos[i+1])

        if dr=="L":
            headpos[0] -=1
            tailpos[0] = move(headpos,tailpos[0])
            for i in range(9):
                tailpos[i+1] = move(tailpos[i], tailpos[i+1])

        if dr=="R":
            headpos[0] +=1
            tailpos[0] = move(headpos,tailpos[0])
            for i in range(9):
                tailpos[i+1] = move(tailpos[i], tailpos[i+1])

        tailposes.add(tuple(tailpos[9]))


print(len(tailposes)-23)

