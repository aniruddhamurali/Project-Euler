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



def main(limit):
    start = time.time()
    primes = generate_primes(math.floor(pow(limit,0.5)))
    nums = set()

    for a in primes:
        for b in primes:
            for c in primes:
                total = a**2 + b**3 + c**4

                if total >= limit:
                    break
                elif total in nums:
                    continue
                else:
                    nums.add(total)

    end = time.time()
    print(end-start)
    return len(nums)

# Answer: 1097343
