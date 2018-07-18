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



def generate_primes(n):
        """generate_primes(n) -> list
        Returns a list of all primes <= n."""
    
        sqrtN = math.sqrt(n)

        if n < 2:
            return []
        elif n < 3:
            return [2]
        
        primes = [2]
        potentialPrimes = list(range(3,n+1,2))
        currentPrime = potentialPrimes[0]

        while currentPrime < sqrtN:
            primes.append(currentPrime)

            for i in potentialPrimes[:]:
                if i % currentPrime == 0:
                    potentialPrimes.remove(i)
            currentPrime = potentialPrimes[0]

        primes += potentialPrimes
        return primes



def primeFactors(n):
        """factory(int) -> list
        Returns the prime factorization of the input as a list
        of primes in increasing order."""
        sqrtn = int(math.sqrt(n))
        primes = generate_primes(sqrtn)

        factors = []
        for i in primes:
            while n % i == 0:
                if not i in factors:
                    factors.append(i)
                n //= i

        if n != 1:
            factors.append(n)

        return factors



def rad(n):
    rad = 1

    if isprime(n) == True: return n

    primefactors = primeFactors(n)
    
    for prime in primefactors:
        rad *= prime

    return rad



def main(k):
    start= time.time()
    sortedRad = []

    for n in range(1,100001):
        sortedRad.append((rad(n),n))

    sortedRad.sort()

    end = time.time()
    print(end-start)
    return sortedRad[k-1][1]


# Answer: 21417
        
