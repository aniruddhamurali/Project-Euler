import math

def sum_primes(n):
    """sum_primes(n) -> list
        Returns the sum of all primes <= n."""


    sqrtN = math.sqrt(n)
    primes = [2]
    potentialPrimes = list(range(3,n+1,2))
    currentPrime = potentialPrimes[0]

    while currentPrime < sqrtN:
        primes.append(currentPrime)

        for i in potentialPrimes[:]:
            if i % currentPrime == 0:
                potentialPrimes.remove(i)
        currentPrime = potentialPrimes[0]

    primes.extend(potentialPrimes)
    return sum(primes)
    
