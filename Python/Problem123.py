import math

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


def main():
    primes = generate_primes(250000)

    for prime in primes:
        n = primes.index(prime) + 1
        
        if n % 2 == 0:
            continue
        
        p = primes[n-1]
        r = (pow(p-1,n) + pow(p+1,n)) % (pow(p,2))
        if r > pow(10,10):
            return n

# The answer is 21035
