from copy import deepcopy
import networkx
import string
import ast
import z3
import matplotlib.pyplot as plt

data = open("202220i.txt","r").read().split("\n")

file = []
c = 0
for i in data:
    file.append([int(i)*811589153,c])
    c+=1
ofile = deepcopy(file)

for iiiii in range(10):
    c = 0
    for i in range(len(ofile)):
        oindex = 0
        for f in range(len(file)):
            if file[f][1] == i:
                oindex = f
        vti = file.pop(oindex)
        insertAt = (vti[0]+oindex) % (len(file))
        if insertAt == 0:
            insertAt = len(file)
        file.insert(insertAt, vti)
    print(iiiii)



nf = []

for i in file:
    nf.append(i[0])

file = nf

n1 = file[(1000 + file.index(0))%len(file)]
n2 = file[(2000 + file.index(0))%len(file)]
n3 = file[(3000 + file.index(0))%len(file)]

print(n1+n2+n3)