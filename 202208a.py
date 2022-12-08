


data = open("202208i.txt","r").read().split("\n")

b = []

for i in data:
    a = []
    for c in i:
        a.append(int(c))
    b.append(a)

data = b

def checkVisibility(x,y, grid):
    v = grid[x][y]
    c = 0
    for i in range(0,x):
        if grid[i][y] < v:
            c+=1
    if c==x:
        return True
    
    c = 0
    for i in range(x+1, len(grid)):
        if grid[i][y] < v:
            c+=1
    if c==len(grid)-x-1:
        return True
    
    c = 0
    for i in range(0,y):
        if grid[x][i] < v:
            c+=1
    if c==y:
        return True
    c = 0
    for i in range(y+1, len(grid[0])):
        if grid[x][i] < v:
            c+=1
    if c==len(grid[0])-y-1:
        return True
    
    return False


total = 0

for x in range(len(data)):
    for y in range(len(data)):
        total += int(checkVisibility(x,y,data))
    
print(total)
