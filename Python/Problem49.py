import math
import time

def isPrime(n):
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


def main2():
    
    primes = set(sieve5(10000))
    n1 = 1488
    go = True
    while n1 < (10000-3):
        inc = 1
        while (n1 + inc + inc < 10000):
            if (n1 in primes):
                n2 = n1 + inc
                if (n2 in primes):
                        n3 = n2 + inc
                        if (n3 in primes):
                            s1 = set(str(n1))
                            s2 = set(str(n2))
                            s3 = set(str(n3))
                            if (s1 == s2 == s3):
                                return str(n1)+str(n2)+str(n3)
            inc += 1
        n1 += 1


def main():
    start = time.time()

    for x in range(1487,9999,2):
        for y in range(x,9999,2):
            for z in range(y,9999,2):
                
                if x == y == z:
                    continue                       
                    
                    if isPrime(x) == True and isPrime(y) == True and isPrime(z) == True:
                        n1 = sortedStrList(list(str(x)))
                        n2 = sortedStrList(list(str(y)))
                        n3 = sortedStrList(list(str(z)))

                        if n1 == n2 == n3:
                            print(time.time() - start)
                            print(x,y,z," ",n1,n2,n3)
                            print(" ")



def sortedStrList(array):
    for i in range(0,len(array)):
        array[i] = int(array[i])

    array.sort()
    return array


def checkPermutation(n1,n2,n3):
    s1 = set(str(n1))
    s2 = set(str(n2))
    s3 = set(str(n3))

    if s1 == s2 == s3:
        return True
    else:
        return False

    



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
        

# Answer: 296962999629
# Took 906 seconds with main()
# Took 1-2 seconds with main2()




        

