import math
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



def prime_factorization(n):
    prime_pow_Dict = dict()
    prime_factors = primeFactors(n)

    for prime in prime_factors:
        power = 0
        while n % prime == 0:
            power = power + 1
            n = n/prime

        prime_pow_Dict[str(prime)] = power

    return prime_pow_Dict



def num_divisors(n):
    numDivisors = 1

    for key in prime_factorization(n):
        numDivisors = numDivisors * (prime_factorization(n)[key] + 1)

    return numDivisors



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
        
        


def main(limit):
    start = time.time()
    count = 0

    for n in range(1,limit):
        if isprime(n) == True:
            continue
        
        elif pow(n, 1/3) % 1 == 0:
            continue

        elif (n % 4 == 0 and n != 4) or (n % 6 == 0 and n!= 6) or (n % 9 == 0 and n!= 9) or (n % 10 == 0 and n!= 10) or (n % 14 == 0 and n!= 14) or (n % 15 == 0 and n!= 15) or (n % 21 == 0 and n!= 21) or (n % 22 == 0 and n != 22):
            continue

        elif (n % 25 == 0 and n != 25) or (n % 26 == 0 and n != 26) or (n % 33 == 0 and n != 33) or (n % 34 == 0 and n != 34) or (n % 35 == 0 and n != 35) or (n % 38 == 0 and n != 38) or (n % 39 == 0 and n != 39):
            continue
        
        elif num_divisors(n) == 3 or num_divisors(n) == 4:
            count += 1

    end = time.time()
    print(end-start)
    return count
            

# Answer: 17427258
