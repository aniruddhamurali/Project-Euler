import time

def sieve(n):
    #start = time.time()
    """Return a list of the primes below n."""
    prime = [True] * n
    result = [2]
    append = result.append
    sqrt_n = (int(n ** .5) + 1) | 1    # ensure it's odd
    for p in range(3, sqrt_n, 2):
        if prime[p]:
            append(p)
            prime[p*p::2*p] = [False] * ((n - p*p - 1) // (2*p) + 1)
    for p in range(sqrt_n, n, 2):
        if prime[p]:
            append(p)

    ##print (time.time()-start)
    return result


def pascal(n):
    tri = [[1]]
    for i in range(1, n):
        start = [1]
        for n in range(0, i-1):
            start.append(tri[i-1][n]+tri[i-1][n+1])
        start.append(1)
        tri.append(start)
    return tri


def isSquareFree(n):
    primes = sieve(int(n**.5)+1)

    for prime in primes:
        if n % prime**2 == 0:
            return False

    return True


def main():
    start = time.time()
    total = 0
    pascalTriangle = pascal(51)
    nums = []

    for row in pascalTriangle:
        for num in row:
            if isSquareFree(num) == True and num not in nums:
                nums.append(num)
                total += num

    print(time.time()-start)
    return total


# Answer: 34029210557338
            
    
