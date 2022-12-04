


data = open("202204i.txt","r").read().split("\n")

c = 0

for i in data:
    p1 = i.split(",")[0].split("-")
    p2 = i.split(",")[1].split("-")
    p1n = [int(p1[0]),int(p1[1])]
    p2n = [int(p2[0]),int(p2[1])]
    if p1n[0] <= p2n[0] and p1n[1] >= p2n[0]:
        c+=1
    elif p2n[0] <= p1n[0] and p2n[1] >= p1n[0]:
        c+=1

print(c)