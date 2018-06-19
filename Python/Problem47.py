import math
import itertools

def generate_primes(n):
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

def main():
    for count in itertools.count(2):
        if len(primeFactors(count)) == 4 and len(primeFactors(count+1)) == 4 and len(primeFactors(count+2)) == 4 and len(primeFactors(count+3)) == 4:
            print(count)
            print(count+1)
            print(count+2)
            return count+3

# The answer is 134043
        
