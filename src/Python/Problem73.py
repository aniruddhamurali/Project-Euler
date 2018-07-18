from fractions import gcd
import time
import math


def main(limit):
    start = time.time()
    count = 0
    maxD = limit
    
    for d in range(2, maxD+1):
        for n in range(math.floor(d/3), d):

            if gcd(n,d) != 1 or n/d <= 1/3:
                continue
            elif n/d >= 1/2:
                break
            else:
                count += 1

    end = time.time()
    print(end-start)
    return count
            
# Answer: 7295372
