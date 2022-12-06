


data = open("202206i.txt","r").read()

c = 0

stream = []

for i in range(len(data)-13):
    dset = set(data[i:i+14])
    if len(dset) == 14:
        print(i + 14)
        break