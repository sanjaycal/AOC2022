


data = open("202202i.txt","r").read().split("\n")


points = 0

for i in data:
    v = i.split(" ")
    if v[-1] == "X":
        if v[0] == "A":
            points += 3
        if v[0] == "B":
            points += 1
        if v[0] == "C":
            points += 2
    if v[-1] == "Y":
        points += 3
        if v[0] == "A":
            points += 1
        if v[0] == "B":
            points += 2
        if v[0] == "C":
            points += 3
    if v[-1] == "Z":
        points += 6
        if v[0] == "A":
            points += 2
        if v[0] == "B":
            points += 3
        if v[0] == "C":
            points += 1

print(points)