import math
import time

def main():
    start = time.time()
    count = 0

    for n in range(1,101):
        for r in range(1,n):
            combinations = math.factorial(n)/(math.factorial(r) * math.factorial(n-r))

            if combinations > 1000000:
                count = count + 1

    elapse = time.time()
    print(elapse-start)
    return count
            
# The answer is 4075
