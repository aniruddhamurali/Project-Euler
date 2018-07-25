# Problem 70
# Answer: 8319823
# Took about 14.5 minutes

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


def isPerm(n, phi):
    l1 = list(str(n))
    l1.sort()
    l2 = list(str(phi))
    l2.sort()
    if l1 == l2:
        return True
    return False


def main():
    minRatio = 10
    minN = 0
    for i in range(2, 10**7):
        p = phi(i)
        if isPerm(i,p) == False:
            continue
        ratio = i/p
        if ratio < minRatio:
            minRatio = ratio
            minN = i
    return minN

print(main())
