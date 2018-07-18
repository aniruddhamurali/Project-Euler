import math
import itertools

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


def pandigital_prime():
    maxpandigitalprime = 1
    
    fourDigitPermutations = list(itertools.permutations([1,2,3,4],4))
    sevenDigitPermutations = list(itertools.permutations([1,2,3,4,5,6,7],7))

    for fourDigitTuple in fourDigitPermutations:
        fourDigitList = list(fourDigitTuple)
        num = ''

        for i in fourDigitList:
            num = num + str(i)

        if isprime(int(num)) == True:
            maxpandigitalprime = int(num)

    for sevenDigitTuple in sevenDigitPermutations:
        sevenDigitList = list(sevenDigitTuple)
        num = ''

        for i in sevenDigitList:
            num = num + str(i)

        if isprime(int(num)) == True:
            maxpandigitalprime = int(num)
        
        
    return maxpandigitalprime

# The answer is 7652413
