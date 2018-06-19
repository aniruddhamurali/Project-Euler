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
    """
    n * pow(p+n,1/3) / pow(n,1/3) = k
    p+n = y**3    ,     n = x**3
    p = y**3 - x**3 = (y-x) * (y**2 + x*y + x**2)

    Since p is prime, y-x = 1

    p = y**3 - x**3 = (i+1)**3 - i*3
    
    """

    count = 0

    for i in range(1, 577):
        p = pow(i+1,3) - pow(i,3)
        if isprime(p) == True:
            count += 1

    return count


# Answer: 173


