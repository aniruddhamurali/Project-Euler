def isprime(n):
    """Checks number (n) for primality, and returns
    True of False."""
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True
 
def main():
    """this example takes the numbers 1, 3, 5, 7, 9, etc., and
    checks for primality."""
    number = 1
    primes = 1 
    while True:
        if isprime(number):
            primes += 1
        if primes == 10001:
            return number
        number += 2

