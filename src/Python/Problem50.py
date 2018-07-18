import math
import time

def generate_primes(n):
        """generate_primes(n) -> list
        Returns a list of all primes <= n."""

        start = time.time()
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
        elapse = time.time()
        #print(elapse-start)
        #print(sum(primes))
        return sum(primes)

def primeFactors(n):
        """factory(int) -> list
        Returns the prime factorization of the input as a list
        of primes in increasing order."""
        sqrtn = int(math.sqrt(n))
        primes = generate_primes(sqrtn)

        factors = []
        for i in primes:
            while n % i == 0:
                factors.append(i)
                n //= i

        if n != 1:
            factors.append(n)

        return factors

'''def sum_primes(n):
    start = time.time()
    #primesList = []
    sumList = []
    currentTotal = 0
    
    for i in range(2,n+1):
        if primeFactors(i) == [i]:
            #primesList.append(i)
            currentTotal = currentTotal + i

        #total = sum(primesList)
        
        if primeFactors(currentTotal) == [currentTotal] and currentTotal < n:
            if currentTotal not in sumList:
                sumList.append(currentTotal)
            else:
                continue
    elapse = time.time()
    print(elapse-start)
    return max(sumList)'''

def sum_primes(n):

    start = time.time()
    sumList = 0

    for i in range(2,n):
        numList = generate_primes(i)
        total = sum(numList)

        if primeFactors(total) == [total] and total < n:
            sumList = total
        else:
            continue

    elapse = time.time()
    print(elapse-start)
    return sumList
        
    
# 7699 after 60 terms
# 8893 after 64 terms
            
            
            
