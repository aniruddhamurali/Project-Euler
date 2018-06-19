# Problem 601
# Answer: 1617243

from math import floor

def gcd(x, y):
    """Return greatest common divisor using Euclid's Algorithm."""
    while y:      
        x, y = y, x % y
    return x

def lcm(nums):
    lcm = nums[0]
    for i in range(1, len(nums)):
        n = nums[i]
        lcm = lcm*n // gcd(lcm,n)
    return lcm


def P(s, N):
    if s == 1: return (N-1) // 2
    
    allP = (N-2) // lcm([i for i in range(2,s+1)])
    removeP = (N-2) // lcm([i for i in range(2,s+2)])
    return allP - removeP


def main():
    total = 0
    
    for i in range(1,32):
        total += P(i, 4**i)

    print(total)
    return total


main()
