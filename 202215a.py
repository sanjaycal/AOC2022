from copy import deepcopy
import networkx
import string
import ast

data = open("202215i.txt","r").read().split("\n")


hcalc = 2000000

rges = []


for sensor in data:
    sx = int(sensor.split(",")[0].split("=")[1])
    sy = int(sensor.split(":")[0].split("y=")[1])
    bx = int(sensor.split("x=")[-1].split(",")[0])
    by = int(sensor.split("=")[-1])

    smd = abs(bx-sx) + abs(by-sy)
    
    r = smd-(abs(sy-hcalc))


    if r>=0:
        rges.append([sx-r,sx+r])


otrges = rges

for i in range(len(data)*5):
    trges = []
    for i in otrges:
        u = 1
        for j in trges:
            if i[1] < j[0] or i[0]>j[1]:
                u = 1
            elif i[0]< j[0] and i[1]<=j[1]:
                j[0] = i[0]
                u=0
            elif i[0] >= j[0] and i[1] >= j[1]:
                j[1] = i[1]
                u=0
            elif i[0]>j[0] and i[1]<j[1]:
                u= 0
                pass
        if len(trges) == 0 or u==1:
            trges.append(i)
    otrges = trges
    otrges.reverse()
    trges = []


n = 0

for i in otrges:
    n+= i[1]-i[0]

print(otrges)

print(n)