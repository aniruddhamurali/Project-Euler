# Problem 77
# Answer: 71

# Uses the Sieve of Eratosthenes to generate a list of primes below a number
def sieve(n):
    """Return a list of the primes below n."""
    prime = [True] * n
    result = [2]
    append = result.append
    sqrt_n = (int(n**.5) + 1) | 1 # ensure it's odd
    for p in range(3, sqrt_n, 2):
        if prime[p]:
            append(p)
            prime[p*p::2*p] = [False] * ((n-p*p-1) // (2*p) + 1)
    for p in range(sqrt_n, n, 2):
        if prime[p]:
            append(p)
    return result

# Counts the number of ways to add prime numbers to get n
def count_summations(n):
    ways = [1] + [0]*n
    primes = sieve(n)
    
    for i in range(len(primes)):
        for j in range(primes[i], n+1):
            ways[j] += ways[j-primes[i]]
    
    return ways[n]


def main():
    n = 2
    while count_summations(n) <= 5000:
        n += 1
    return n

print(main())
