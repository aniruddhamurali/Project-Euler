import math

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
    for x in range(3, round(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True

def main():
    loopcount = 2
    looplength = 3

    totalcount = 1
    primecount = 0

    while True:
        bottomright = pow(looplength,2)
        bottomleft = bottomright - (looplength - 1)
        topright = bottomright - 6 * (loopcount-1)
        topleft = topright + (looplength - 1)

        if isprime(bottomright) == True:
            primecount = primecount + 1
        if isprime(bottomleft) == True:
            primecount = primecount + 1
        if isprime(topright) == True:
            primecount = primecount + 1
        if isprime(topleft) == True:
            primecount = primecount + 1

        totalcount = totalcount + 4

        if primecount/totalcount < 0.1:
            return looplength

        loopcount = loopcount + 1
        looplength = looplength + 2

# The answer is 26241





        
    
