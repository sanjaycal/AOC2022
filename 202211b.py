from copy import deepcopy


data = open("202211i.txt","r").read().split("\n\n")


class monkey:
    def __init__(self, si, op, tst, tt, tf):
        self.startingItems = si
        self.ni = 0
        self.operation = op
        self.test = tst
        self.throwTrue = tt
        self.throwFalse = tf
    
    def throw(self, n, monkeyList, mn):
        monkeyList[mn].startingItems.append(self.startingItems[n])
        return monkeyList

    def inspect(self, n, monkeyList,lcm):
        self.ni +=1
        old = self.startingItems[n]

        new = 0

        
        fv = old if self.operation[0] == "old" else int(self.operation[0])
        sv = old if self.operation[2] == "old" else int(self.operation[2])
        
        if self.operation[1] == "+":
            new = fv+sv
        else:
            new = fv*sv

        new = new%lcm
        self.startingItems[n] = new
        monkeyList = self.throw(n, monkeyList, self.throwTrue if new%self.test == 0 else self.throwFalse)
        return monkeyList
    
    def inspectAll(self,monkeyList, lcm):
        for i in range(len(self.startingItems)):
            monkeyList = self.inspect(i, monkeyList, lcm)
        self.startingItems = []
        return monkeyList


monkeylist = []

for i in data:
    
    lines = i.split("\n")
    si = lines[1].split(": ")[-1].split(",")
    sis = []
    for j in si:
        sis.append(int(j))
    op = lines[2].split(": ")[-1].split("= ")[-1].split(" ")
    tst = int(lines[3].split(" ")[-1])
    tt = int(lines[4].split(" ")[-1])
    tf = int(lines[5].split(" ")[-1])
    nm = monkey(sis,op,tst,tt,tf)
    monkeylist.append(nm)

lcm = 1

for m in monkeylist:
    lcm *= lcm*m.test


for i in range(10000):
    for m in monkeylist:
        monkeylist = m.inspectAll(monkeylist,lcm)

out = [x.ni for x in monkeylist]
print(out)
sout = sorted(out)
print(sout[-1]* sout[-2])