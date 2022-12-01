


data = open("202201i.txt","r").read()

dreins = data.split("\n\n")

max = []

print(len(dreins))

c = 0

for i in dreins:
    ncs = i.split("\n")
    cals = 0
    for j in ncs:
        cals += int(j)
    max.append(cals)
    c+=1

max = sorted(max)

print(max[-3:])

print(sum(max[-3:]))

print(c)