# Problem 108
# Answer: 180180

import math
import time
import itertools

def main():
    for n in itertools.count(1000000):
        if (count_divisors_squared(n) + 1) // 2 > 4000000:
            print(n)
            return n

# Returns the number of divisors of n^2
def count_divisors_squared(n):
    count = 1
    end = math.floor(math.sqrt(n))
    for i in itertools.count(2):
        if i > end: break
        if n % i == 0:
            j = 0
            while True:
                n //= i
                j += 1
                if n % i != 0: break
            count *= j*2+1  # n^2 has 2*j+1 times as many factors
    return count



main()
