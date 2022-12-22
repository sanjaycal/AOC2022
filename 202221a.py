from copy import deepcopy
import networkx
import string
import ast
import z3
import matplotlib.pyplot as plt

data = open("202221i.txt","r").read().split("\n")

monkeys = {}

for i in data:
    k = i.split(": ")[0]
    mval = i.split(": ")[1]
    monkeys[k] = mval

def get_value(monkeys, name):
    if monkeys[name][0] in ["1","2","3","4","5","6","7","8","9","0"]:
        return int(monkeys[name])
    
    eq = monkeys[name].split(" ")

    v0 = get_value(monkeys, eq[0])
    v1 = get_value(monkeys, eq[2])

    if eq[1] == "+":
        return v0 + v1
    if eq[1] == "-":
        return v0 - v1
    if eq[1] == "/":
        return v0 / v1
    if eq[1] == "*":
        return v0 * v1


print(get_value(monkeys, "root"))