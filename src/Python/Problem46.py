import math
import itertools

def isPrime(n):
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
    
    for odd in itertools.count(9,2):
        if isPrime(odd) == False:
            
            for prime in range(3, odd):
                if prime == odd-1:
                    return odd
                
                if isPrime(prime) == True:
                    difference = odd -  prime
                    square = difference/2
                    sqrt = math.sqrt(square)
                    
                    if int(sqrt) == sqrt:
                        break
    
# Answer: 5777
