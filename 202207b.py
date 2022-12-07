


data = open("202207i.txt","r").read().split("$ ")

filesystem = {}

curdir = []


def setValue(fs, value, path):
    if not path[0] in fs.keys():
        fs[path[0]] = {"value": value}
        return fs
    setValue(fs[path[0]], value, path[1:])


for i in data:
    if i[0] == "c":
        if i.split(" ")[1][:-1] == "..":
            curdir.pop()
        else:
            st = ""
            for j in curdir:
                st = st + "/" + j
            curdir.append(st + "/" + i)
    if i[0] == "l":
        files = i.split("\n")[1:]
        sumSize = 0
        for head in files:
            if head[:3] != "dir":
                if head != "":
                    sumSize += int(head.split(" ")[0])
        for i in curdir:
            if not i in filesystem.keys():
                filesystem[i] = 0
            filesystem[i] += sumSize

gvs = filesystem
total = 0
toFree = gvs[list(gvs.keys())[0]] - (70000000 - 30000000)

mn = 99999999999999
sv = ""

for i in gvs.keys():
    if gvs[i] <=mn and gvs[i] > toFree:
        mn = gvs[i]
        sv = i

print(mn)