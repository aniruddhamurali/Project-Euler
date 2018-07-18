import math

def digit_factorials():
    total = 0
    
    for n in range(10, math.factorial(9)*7):
        digitfactorialSum = 0
        digits = list(map(int, str(n)))
        
        for digit in digits:
            digitfactorialSum = digitfactorialSum + math.factorial(int(digit))

        if digitfactorialSum == n:
            print(n)
            total = total + n

    return total

# The answer is 40730
