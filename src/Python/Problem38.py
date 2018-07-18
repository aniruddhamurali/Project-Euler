import itertools
import time

def main():
    start = time.time()
    maxPandigitalNumber = 0

    # only number 1 to 9999 will yield less than 10 digits
    for i in range(1, 10000):
        numString = ""

        for n in itertools.count(1):
            numString += str(i*n)

            if len(numString) > 9:
                break
            
            elif len(numString) == 9:
                if isNinePandigital(numString) == True:
                    if int(numString) > maxPandigitalNumber:
                        maxPandigitalNumber = int(numString)

    end = time.time()
    print(end-start)
    return maxPandigitalNumber
        

def hasCommonDigits(a,b):
    strA = str(a)
    strB = str(b)

    for i in strA:
        for j in strB:
            if i == j:
                return True

    return False


# Answer: 932718654

def isNinePandigital(n):
    digits = list(n)
    digits.sort()

    if digits == ['1','2','3','4','5','6','7','8','9']:
        return True
    else:
        return False
