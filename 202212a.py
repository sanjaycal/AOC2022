from copy import deepcopy
import networkx
import string

data = open("202212i.txt","r").read().split("\n")

rivermap = [list(ln) for ln in data]

spos = []
epos = []
for y in range(len(rivermap)):
    for x in range(len(rivermap[0])):
        if rivermap[y][x] == "S":
            spos = [x,y]
            rivermap[y][x] = "a"
        elif rivermap[y][x] == "E":
            epos = [x,y]
            rivermap[y][x] = "z"
            
G = networkx.DiGraph()
for y in range(len(rivermap)):
    for x in range(len(rivermap[0])):
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(rivermap[0]) and 0 <= ny < len(rivermap):
                A = string.ascii_lowercase.index(rivermap[y][x])
                B = string.ascii_lowercase.index(rivermap[ny][nx])
                if B <= A + 1:
                    G.add_edge((x, y), (nx, ny))

p = networkx.shortest_path(G, (spos[0], spos[1]), (epos[0], epos[1]))
print(len(p) - 1)
