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


def num_divisors(n):
    numDivisor = 0
    for divisor in range(1,round(math.sqrt(n))+1):
        if n % divisor == 0:
            numDivisor = numDivisor + 2

    sqrtn = math.sqrt(n)
    if int(sqrtn) == float(sqrtn):
        numDivisor = numDivisor - 1

    return numDivisor



def main(limit):
    start = time.time()
    count = 1

    for n in range(3,limit):
        if isprime(n) == True:
            continue
        elif num_divisors(n) == num_divisors(n+1):
            count += 1

    end = time.time()
    print(end-start)
    return count


# Answer: 986262




        
                
        
