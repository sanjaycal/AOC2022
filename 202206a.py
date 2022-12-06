


data = open("202206i.txt","r").read()

c = 0

stream = []

for i in range(len(data)-3):
    dset = set(data[i:i+4])
    if len(dset) == 4:
        print(i + 4)
        break