import math
import time
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


def is_leftright_truncatable_prime(prime):
    digits = list(map(int, str(prime)))
    
    for loop in range(1,len(digits)):
        digits.pop(0)
        if isprime(int(''.join(map(str,digits)))) == False:
            return False
    return True


def is_rightleft_truncatable_prime(prime):
    digits = list(map(int, str(prime)))
    
    for loop in range(1,len(digits)):
        digits.pop(len(digits)-1)
        if isprime(int(''.join(map(str,digits)))) == False:
            return False
    return True


def main():
    start = time.time()
    truncatablePrimes = []
    
    for prime in itertools.count(23,2):
        if isprime(prime) == False:
            continue
        
        digits = str(prime)

        if digits.startswith('1') == True or digits.endswith('1') == True:
            continue
        
        if '4' in digits or '6' in digits or '8' in digits or '0' in digits:
            continue

        if is_leftright_truncatable_prime(prime) == True and is_rightleft_truncatable_prime(prime) == True:
            truncatablePrimes.append(prime)

        if len(truncatablePrimes) == 11:
            break

    elapse = time.time()
    print(elapse-start)
    return sum(truncatablePrimes)

# The answer is 748317
        
        





        
    
