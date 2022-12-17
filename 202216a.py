from copy import deepcopy
import networkx
import string
import ast
import z3
import matplotlib.pyplot as plt

data = open("202216i.txt","r").read().split("\n")

valves = {}


frs = {}
valves = {}
Opens = {}


for i in data:
    name = i[6:8]
    frs[name] = int(i.split(";")[0].split("=")[-1])
    sl = i.split("valve")[-1][1:].split(",") if i.split("valve")[-1][0] != "s" else i.split("valve")[-1][2:].split(",")
    slt = []
    for i in sl:
        slt.append(i.strip())
    valves[name] = slt
    Opens[name] = False 

seen = {}
mx = 0

def run(depth, cpos, totflow):
    global mx, valves,Opens, seen


    if seen.get((depth,cpos), -1) >= sum(totflow):
        return mx
    seen[depth,cpos] = sum(totflow)

    if depth == 30:
        mx = max(mx,sum(totflow))
        return
    
    for k in range(2):
        if k == 0:
            if Opens[cpos] or frs[cpos] <=0:
                continue
            
            Opens[cpos] = True
            j = sum(frs[n] for n,v in Opens.items() if v)
            run(depth+1, cpos, totflow + [j])
            Opens[cpos] = False
        else:
            j = sum(frs[n] for n,v in Opens.items() if v)
            for valve in valves[cpos]:
                run(depth+1, valve if valve is not None else cpos, totflow + [j])

run(1, "AA", [0])

print(mx)