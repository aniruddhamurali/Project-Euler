# Problem 132
# Answer: 843296

def sieve(n):
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

    return result


def main():
    primes = sieve(1000000)
    total = 0
    count = 0

    for p in primes:
        if pow(10, 10**9, 9*p) == 1:
            total += p
            count += 1
        if count == 40:
            break

    print(total)
    return total

main()
