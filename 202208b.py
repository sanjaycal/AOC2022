


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
    totalu = 0
    for i in range(x-1,-1, -1):
        totalu +=1
        if grid[i][y] >= v:
            break
    
    totald = 0
    for i in range(x+1, len(grid)):
        totald +=1
        if grid[i][y] >= v:
            break
    
    totall = 0
    for i in range(y-1,-1, -1):
        totall +=1
        if grid[x][i] >= v:
            break
    
    totalr = 0
    for i in range(y+1, len(grid[0])):
        totalr+=1
        if grid[x][i] >= v:
            break
    
    

    return totalu*totald*totall*totalr


mx = 0

for x in range(len(data)):
    for y in range(len(data)):
        mx = max(checkVisibility(x,y,data),mx)
    
print(mx)
