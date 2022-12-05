


data = open("202205i.txt","r").read().split("\n\n")

crates = {}

instructions = []

for i in data[1].split("\n"):
    n1 = int(i.split(" from")[0].split("ove ")[-1])
    n2 = int(i.split("from ")[1].split(" to")[0])
    n3 = int(i.split("from ")[1].split("to ")[1])
    instructions.append([n1,n2,n3])

flag = 0

stack = 1

counter = 0
layer = 0

for c in data[0]:
    if flag == 1:
        if not str(stack) in crates.keys():
            crates[str(stack)] = []
        print(c)
        print(stack)
        crates[str(stack)].insert(0,c)
        flag = 0
    if c=="[":
        flag = 1
    if c==" ":
        counter+=1
        flag = 0
    else:
        counter = 0
    if counter==4:
        stack += 1
        counter = 0
    if c=="]":
        counter = 0
        stack +=1
        flag = 0
    if c=="\n":
        stack = 1
        counter = 0
        layer += 1


def move(i,f,crates, amount):
    crates[str(f)].extend(crates[str(i)][-amount:])
    tmp = crates[str(i)]
    tmp = tmp[:len(tmp)-amount]
    crates[str(i)] = tmp
    return crates


for instruction in instructions:
    crates = move(instruction[1], instruction[2], crates, instruction[0])

print(crates)

out = ""

for i in range(len(crates.keys())):
    out = out + crates[str(i+1)].pop()

print(out)
