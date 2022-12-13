from copy import deepcopy
import networkx
import string
import ast

data = open("202213i.txt","r").read().split("\n\n")


def compare(a,b):
    if type(a) == int and type(b)==int:
        if a==b:
            return "n"
        if a<b:
            return "r"
        if a>b:
            return "w"
    if type(a) == list and type(b)==list:
        for i in range(max(len(a),len(b))):
            try:
                o = compare(a[i],b[i])
                if o != "n":
                    return o
            except:
                if len(a) < len(b):
                    return "r"
                else:
                    return "w"
        return "n"
    if type(a) == list and type(b)==int:
        return compare(a,[b])
    if type(a) == int and type(b) == list:
        return compare([a],b)
    

dset = []

for i in data:
    lines = i.split("\n")
    dset.append(ast.literal_eval(lines[0]))
    dset.append(ast.literal_eval(lines[1]))

dset.append([[2]])
dset.append([[6]])

outlist = []

for i in dset:
    c = -1
    v = -1
    for l in outlist:
        c+=1
        cp = compare(i,l)
        if cp == "r":
            v=1
            break
    if v==-1:
        outlist.append(i)
    else:
        outlist.insert(c,i)

print((outlist.index([[2]])+1) * (outlist.index([[6]])+1))