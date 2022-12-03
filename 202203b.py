


data = open("202203i.txt","r").read().split("\n")

d2 = []

for i in range(len(data)//3):
    d2.append([data[i*3+0],data[i*3+1],data[i*3+2], ])

total = 0

for i in d2:
    c1 = i[0]
    c2 = i[1]
    c3 = i[2]
    sc = []
    for c in c1:
        if c in c2:
            sc.append(c)
    nsc = ""
    for c in sc:
        if c in c3:
            nsc = c
    CLIST = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    total += 1 + CLIST.index(nsc)

print(total)