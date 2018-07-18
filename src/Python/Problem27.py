import itertools
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
    if n % 2 == 0:
        return False
    for x in range(3, round(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True


def main():
    productPrimeList = []

    for a in range(-999, 1000):
        for b in range(-999, 1000):
            primeCount = 0
            product = a*b
            
            for n in itertools.count(0):
                value = n**2 + a*n + b
                if isprime(value) == True:
                    primeCount += 1
                else:
                    break
                
            productPrimeList.append((primeCount,product))

    return max(productPrimeList)


# Answer: -59231
