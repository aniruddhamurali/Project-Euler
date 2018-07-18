import math
import time

def divisors(n):
    divisorList = []
    for divisor in range(2, round(math.sqrt(n)) + 1):
        
        if n % divisor == 0:
            divisorList.append(divisor)
            
            if divisor == n//divisor:
                continue
            else:
                divisorList.append(n//divisor)

    divisorList.append(1)
    return divisorList


def isAbundantNumber(n):
    factors = divisors(n)

    if sum(factors) > n:
        return True
    else:
        return False


def main(limit):
    start = time.time()
    total = 0
    
    abundantNumbers = []
    sumAbundant = set()

    for i in range(1, limit+1):
        if isAbundantNumber(i) == True:
            abundantNumbers.append(i)


    for x in range(0, len(abundantNumbers)):
        for y in range(0, len(abundantNumbers)):
            sumAbundant.add(abundantNumbers[x] + abundantNumbers[y])


    for n in range(1,limit+1):
        if n not in sumAbundant:
            total += n

    end = time.time()
    print(end-start)
    return total

# Answer: 4179871

    
