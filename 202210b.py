from copy import deepcopy


data = open("202210i.txt","r").read().split("\n")

c = 0

cd = 0

Vs = [["." for x in list(range(40))] for x in range(40)]

print(Vs[0][2])

xval = 1

for i in data:
    if i[0] == "n":
        if abs(xval-c%40)<=1:
            Vs[c//40][c%40] = "#"
        else:
            print(c)
            Vs[c//40][c%40] = "."
        if (c)//40 >cd:
            cd +=1
        c+=1
    else:
        if abs(xval-c%40)<=1:
            Vs[c//40][c%40] = "#"
        else:
            Vs[c//40][c%40] = "."
        if (c)//40 >cd:
            cd +=1
        c+=1
        if abs(xval-c%40)<=1:
            Vs[c//40][c%40] = "#"
        else:
            Vs[c//40][c%40] = "."
        if (c)//40 >cd:
            cd +=1
        c+=1
        xval += int(i.split(" ")[-1])
        

for i in Vs:
    s = ""
    for j in i:
        s = s+j
    print(s)