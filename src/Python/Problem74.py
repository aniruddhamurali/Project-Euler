import math
import time

def digitFactorialSum(n):
    total = 0
    
    for digit in str(n):
        total += math.factorial(int(digit))

    return total


def main():
    start = time.time()
    count = 0

    for i in range(0,1000000):
        chain = set()
        n = i

        while i not in chain:
            nSum = digitFactorialSum(n)
            if nSum in chain:
                break
            chain.add(nSum)
            n = nSum

        chain.add(i)
        if len(chain) == 60:
            count += 1
        #print(chain)

    print(time.time()-start)
    return count


# Answer: 402
