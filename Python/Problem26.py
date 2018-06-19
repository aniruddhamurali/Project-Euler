import math
import itertools
import time

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
    start = time.time()
    maxD = 0
    maxDigitCycle = 0
    primes = generate_primes(1000)

    for d in primes:
        n = 1 # n-digit recurring cycle

        if d == 2 or d == 5:
            continue
        
        digitCycle = 0
            
        for n in itertools.count(1):
            x = 10**n - 1

            if x % d == 0:
                digitCycle = n
                break
                
        if n > maxDigitCycle:
            maxD = d
            maxDigitCycle = digitCycle


    end = time.time()
    print(end-start)
    return maxD, maxDigitCycle

# Answer: 983
        
