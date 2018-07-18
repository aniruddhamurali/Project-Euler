import math

def sum_divisors(n):
    divisorList = []
    for divisor in range(1, round(math.sqrt(n)) + 1):
        
        if n % divisor == 0:
            divisorList.append(divisor)
            
            if divisor == n//divisor:
                continue
            if divisor == 1:
                continue
            else:
                divisorList.append(n//divisor)

    return sum(divisorList)


def amicable_sum():
    total = 0
    amicableNum = []
    
    for count in range(1,10000):
        if count in amicableNum:
            continue
        
        sumDivisors = sum_divisors(count)
        
        if sumDivisors >= 10000:
            continue
        else:
            if sum_divisors(sumDivisors) == count:
                amicableNum.append(count)
                if sumDivisors in amicableNum:
                    continue
                amicableNum.append(sumDivisors)
                total = total + count + sumDivisors

    print(amicableNum)
    return total

# The answer is 31626               
    
