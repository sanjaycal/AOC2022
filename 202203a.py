


data = open("202203i.txt","r").read().split("\n")

total = 0

for i in data:
    c1 = i[:len(i)//2]
    c2 = i[len(i)//2:]
    sc = ""
    for c in c1:
        if c in c2:
            sc = c
    CLIST = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    total += 1 + CLIST.index(sc)

print(total)