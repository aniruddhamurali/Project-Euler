import math
import itertools

def main(limit):
    triNumber = 0
    for count in itertools.count(1):
        triNumber = triNumber + count

        if num_divisors(triNumber) > limit:
            break

    return triNumber


def num_divisors(n):
    numDivisor = 0
    for divisor in range(1,round(math.sqrt(n))):
        if n % divisor == 0:
            numDivisor = numDivisor + 2

    sqrtn = math.sqrt(n)
    if int(sqrtn) == float(sqrtn):
        numDivisor = numDivisor + 1

    return numDivisor

    
