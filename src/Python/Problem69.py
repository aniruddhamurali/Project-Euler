# Problem 69
# Answer: 510510

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)


def phi(n):
    count = n
    p = 2
    while(p*p <= n):
        if n % p == 0:
            while n % p == 0:
                n = n//p
            count *= 1.0 - (1.0/float(p))
        p += 1

    if n > 1:
        count *= 1.0 - (1.0/float(n))

    return int(count)


def main():
    maxResult = 0
    maxNum = 0
    for i in range(1, 1000000):
        p = i/phi(i)
        if p > maxResult:
            maxResult = p
            maxNum = i
    return maxNum


print(main())

