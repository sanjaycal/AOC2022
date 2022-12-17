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

seen = {}
mx = 0

def run(depth, cpos1, cpos2, totflow):
    global mx, valves, Opens, seen, _seen2
    
    if seen.get((depth, cpos1, cpos2), -1) >= sum(totflow):
        return
    seen[depth, cpos1, cpos2] = sum(totflow)
    
    if depth == 26:
        if sum(totflow) > mx:
            mx = sum(totflow)
            print(mx, totflow)
        return
    
    if all(v for k, v in Opens.items() if frs[k] > 0):
        tf = sum(frs[k] for k, v in Opens.items() if v)
        run(depth + 1, cpos1, cpos2, totflow + [tf])
        return
    
    for k in (0, 1):
        if k == 0:
            if Opens[cpos1] or frs[cpos1] <= 0:
                continue
                
            Opens[cpos1] = True
            
            for k2 in (0, 1):
                if k2 == 0:
                    if Opens[cpos2] or frs[cpos2] <= 0:
                        continue
                    
                    Opens[cpos2] = True
                    j = sum(frs[k] for k, v in Opens.items() if v)
                    run(
                        depth + 1,
                        cpos1,
                        cpos2,
                        totflow + [ j ]
                    )
                    Opens[cpos2] = False
                else:
                    j = sum(frs[k] for k, v in Opens.items() if v)
                    for v2 in valves[cpos2]:
                        run(depth + 1, cpos1, v2, totflow + [ j ])
            Opens[cpos1] = False
        else:
            j = sum(frs[k] for k, v in Opens.items() if v)
            for valve in valves[cpos1]:
                for k2 in (0, 1):
                    if k2 == 0:
                        if Opens[cpos2] or frs[cpos2] <= 0:
                            continue

                        Opens[cpos2] = True
                        j = sum(frs[k] for k, v in Opens.items() if v)
                        run(depth + 1, valve, cpos2, totflow + [ j ])
                        Opens[cpos2] = False
                    else:
                        j = sum(frs[k] for k, v in Opens.items() if v)
                        for valve2 in valves[cpos2]:
                            run(depth + 1, valve, valve2, totflow + [ j ])

run(1, "AA", "AA", [ 0 ])