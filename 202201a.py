


data = open("202201i.txt","r").read()

dreins = data.split("\n\n")

max = 0

print(len(dreins))

c = 0

for i in dreins:
    ncs = i.split("\n")
    cals = 0
    for j in ncs:
        cals += int(j)
    if cals>max:
        max = cals
    c+=1

print(c)
print(max)