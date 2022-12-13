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
    


cn = 0
out = 0

for i in data:
    cn +=1
    lines = i.split("\n")
    l1 = ast.literal_eval(lines[0])
    l2 = ast.literal_eval(lines[1])
    ot = compare(l1, l2)
    if ot =="r":
        out += cn

print(out)
