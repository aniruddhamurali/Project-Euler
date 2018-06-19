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



def circular_primes(n):
    start = time.time()
    primes = generate_primes(n)
    circularPrimes = []

    for prime in primes:
        digits = list(map(int, str(prime)))

        if len(digits) == 1:
            circularPrimes.append(prime)
            continue

        if 2 in digits or 4 in digits or 5 in digits or 6 in digits or 8 in digits or 0 in digits:
            continue
        
        if prime in circularPrimes:
            continue

        track = [prime]

        for loop in range(1,len(digits)):
            digits.append(digits.pop(0))
            if isprime(int(''.join(map(str,digits)))) == False:
                break
                
            track.append(int(''.join(map(str,digits))))

            if isprime(int(''.join(map(str,digits)))) == True:
                if loop == len(digits) - 1:
                    
                    for item in track:
                        if not item in circularPrimes:
                            circularPrimes.append(item)
                else:
                    continue

    elapse = time.time()
    print(elapse-start)
    return len(circularPrimes)
                
# The answer is 55
        

    
