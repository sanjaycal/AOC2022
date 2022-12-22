from copy import deepcopy
import networkx
import string
import ast
import z3
import matplotlib.pyplot as plt

data = open("202221i.txt","r").read().split("\n")

monkeys = {}

s = z3.Solver()



for i in data:
    k = i.split(": ")[0]
    mval = i.split(": ")[1]
    monkeys[k] = [mval, z3.Int(k)]

def get_value(monkeys, name):
    global s
    mval = monkeys[name][0]
    if name == "humn":
        return
    if mval[0] in ["1","2","3","4","5","6","7","8","9","0"]:
        s.add(monkeys[name][1] == int(mval))
        return
    
    eq = mval.split(" ")

    v0 = get_value(monkeys, eq[0])
    v1 = get_value(monkeys, eq[2])

    if name == "root":
        s.add(monkeys[eq[0]][1] == monkeys[eq[2]][1])
        return
    
    

    if eq[1] == "+":
        s.add(monkeys[name][1] == monkeys[eq[0]][1] + monkeys[eq[2]][1] )
    if eq[1] == "-":
        s.add(monkeys[name][1] == monkeys[eq[0]][1] - monkeys[eq[2]][1] )
    if eq[1] == "/":
        s.add(monkeys[name][1] == monkeys[eq[0]][1] / monkeys[eq[2]][1] )
    if eq[1] == "*":
        s.add(monkeys[name][1] == monkeys[eq[0]][1] * monkeys[eq[2]][1] )


print(get_value(monkeys, "root"))
print(s.check())
print(s)
print(s.model()[monkeys["humn"][1]])