import math
import time

def smpf(n):
    for divisor in range(3,round(math.sqrt(n))+1,2):
        if n % divisor == 0:
            return divisor
        else:
            continue


def sum_smpf(n):
    total = 0
    start = time.time()
    
    for i in range(3,n+1,2):
        
        f = smpf(i)
        
        if f == None:
            total = total + i
            
        else:
            total = total + f
            
    if n % 2 == 0:
        total = total + n
    else:
        total = total + n - 1
        
    elapse = time.time()
    print(elapse-start)
    answer = total % 10**9
    return answer

# The answer is 44389811




