from copy import deepcopy
import networkx
import string
import ast
import z3

data = open("202215i.txt","r").read().split("\n")


hcalc = 2000000

rges = []

s = z3.Solver()

x = z3.Int("x")
y = z3.Int("y")

s.add(0 < x)
s.add(0 < y)
s.add(x < 4000000)
s.add(y < 4000000)

for sensor in data:
    sx = int(sensor.split(",")[0].split("=")[1])
    sy = int(sensor.split(":")[0].split("y=")[1])
    bx = int(sensor.split("x=")[-1].split(",")[0])
    by = int(sensor.split("=")[-1])

    smd = abs(bx-sx) + abs(by-sy)
    
    s.add(z3.If(sx-x>=0,sx-x,x-sx) + z3.If(sy-y>=0,sy-y,y-sy) > smd)

print(s.check())
print(s.model())
xv = int(str(s.model()).split(",")[0].split("= ")[1])
yv = int(str(s.model()).split(",")[1].split("= ")[1][:-1])
print(xv*4000000 + yv)