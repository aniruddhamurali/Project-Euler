from decimal import *
getcontext().prec = 102

import math

def main():
    total = 0

    for i in range(1, 101):
        sqrt = math.sqrt(i)

        if int(sqrt) == float(sqrt):
            #print(i)
            continue
        else:
            decimal = Decimal(i).sqrt()
            hds = hundredDigitSum(decimal)
            total += hds

    return total



def hundredDigitSum(decimal):
    digits = list(str(int(decimal*pow(10,99))))
    #print(digits)
    #digits.remove(digits[0])

    for pos in range(0, len(digits)):
        digits[pos] = int(digits[pos])
        
    return sum(digits)

# Answer: 40886
