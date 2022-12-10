from copy import deepcopy


data = open("202210i.txt","r").read().split("\n")

c = 0

cd = 0

Vs = []

xval = 1

for i in data:
    if i[0] == "n":
        c+=1
        if (c+20)//40 >cd:
            Vs.append(xval * (c))
            cd +=1
            print(xval)
            print(c)
    else:
        c+=2
        if (c+20)//40 >cd:
            if c%2 == 0:
                Vs.append(xval * (c))
            else:
                Vs.append(xval * (c-1))
            cd +=1
        xval += int(i.split(" ")[-1])
        

print(Vs)
print(sum(Vs))