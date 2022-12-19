from copy import deepcopy
import networkx
import string
import ast
import z3
import matplotlib.pyplot as plt

data = open("202219i.txt","r").read().split("\n")


    
def heuristic(state):
    time, robots, inv, mined = state
    return 1000*mined[3] + 100*mined[2] + 10*mined[1] + mined[0]

def simulate(bp, cdt):

    queue = []
    queue.append((0,[1,0,0,0],[0,0,0,0],[0,0,0,0]))
    mx = 0
    depth = 0
    
    while queue:
        time, robots, inv, mined = queue.pop(0)

        if time > depth:

            queue.sort(key=heuristic, reverse=True)
            queue = queue[:cdt]
            depth = time
        
        if time == 32:
            mx = max(mx, mined[3])
            continue

        ninv = [inv[i] + robots[i] for i in range(4)]
        nmined = [mined[i] + robots[i] for i in range(4)]

        queue.append((time + 1, deepcopy(robots), deepcopy(ninv), deepcopy(nmined)))

        for i in range(4):
            robotCost = bp[i]

            if all([inv[j] >= robotCost[j] for j in range(4)]):
                nr = deepcopy(robots)
                nr[i] += 1

                ninvstate = [ninv[j] - robotCost[j] for j in range(4)]
                queue.append((time + 1, nr, ninvstate, nmined))
    return mx


blueprints = []

for i in data:
    sentences = i.split(".")
    oreCost = int(sentences[0].split("costs ")[1].split(" o")[0])
    clayCost = int(sentences[1].split("costs ")[1].split(" o")[0])
    obsidianOreCost = int(sentences[2].split("costs ")[1].split(" o")[0])
    obsidianClayCost = int(sentences[2].split("and ")[1].split(" c")[0])
    geodeOreCost = int(sentences[3].split("costs ")[1].split(" o")[0])
    geodeObsidianCost = int(sentences[3].split("and ")[1].split(" o")[0])
    
    blueprints.append([[oreCost,0,0,0],[clayCost,0,0,0],[obsidianOreCost,obsidianClayCost,0,0],[geodeOreCost,0,geodeObsidianCost,0]])


total = []

for bp in blueprints[:3]:
    a = simulate(bp, 20000)
    total.append(a)
    print(a)

nt = 1
for i in total:
    nt = nt*i
print(nt)
