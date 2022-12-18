from copy import deepcopy
import networkx
import string
import ast
import z3
import matplotlib.pyplot as plt

data = open("202218i.txt","r").read().split("\n")

cubes = [[[1 for x in range(22)] for x in range(22)] for x in range(22)]

cubeposlist = []

for i in data:
    values = i.split(",")
    x = int(values[0])
    y = int(values[1])
    z = int(values[2])
    cubeposlist.append([x,y,z])
    cubes[x][y][z] = 0

print(len(cubeposlist))

total = 0

for i in cubeposlist:
    x = i[0]
    y = i[1]
    z = i[2]
    cn = cubes[x + 1][y][z] + cubes[x][y + 1][z] + cubes[x][y][z + 1] + cubes[x - 1][y][z] + cubes[x][y - 1][z] + cubes[x][y][z -1]
    total += cn

print(total)

