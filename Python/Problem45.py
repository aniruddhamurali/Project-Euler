import itertools
import time

def main():
    start = time.time()
    triList = []
    pentList = []
    hexList = []
    tphList = []

    for n in itertools.count(1):
        triNum = n * (n+1)//2
        pentNum = n * (3*n - 1)//2
        hexNum = n * (2*n - 1)
        
        triList.append(triNum)
        pentList.append(pentNum)
        hexList.append(hexNum)

        if triNum in pentList and triNum in hexList:
            tphList.append(triNum)

        if len(tphList) == 3:
            elapse = time.time()
        print(elapse-start)
            return tphList[2]

# The answer is 1533776805

def main2():
    start = time.time()
    triSet = set(x*(x+1)//2 for x in range(1,60000))
    pentSet = set(x*(3*x-1)//2 for x in range(1,60000))
    hexSet = set(x*(2*x - 1) for x in range(1,60000))

    elapse = time.time()
    print(elapse-start)
    return triSet.intersection(pentSet,hexSet)
    
            

    
