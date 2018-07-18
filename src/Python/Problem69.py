import math
import time


def isprime(n):
    """Checks number (n) for primality, and returns
    True of False."""
    n = abs(n)
    if n < 2:
        return False
    if n == 2:
        return True
    if not n % 1 == 0:
        return False
    if n % 2 == 0:
        return False
    for x in range(3, round(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True



def divisors(n):
    divisors = set()

    for divisor in range(1, round(math.sqrt(n))+1):

        if n % divisor == 0:
            divisors.add(divisor)

            if divisors == n//divisor:
                continue
            else:
                divisors.add(n//divisor)
    
    return divisors
    


def phi(n):
    relativePrimesCount = 1
    nDivisors = divisors(n)

    for num in range(2, n):
        numDivisors = divisors(num)
        intersection = nDivisors.intersection(numDivisors)

        if intersection == {1}:
            relativePrimesCount += 1

    return relativePrimesCount



def quotient(n):
    quotient = n/phi(n)
    return quotient



def main(limit):
    start = time.time()
    maxQuotient = 0
    maxN = 0

    for n in range(2, limit+1):
        if isprime(n) == True:
            continue
        elif n % 2 == 1:
            continue
        elif len(divisors(n)) < 20:
            continue
        
        qt = quotient(n)

        if qt > maxQuotient:
            maxQuotient = qt
            maxN = n

    end = time.time()
    print(end-start)
    #print(maxQuotient)
    return maxN


