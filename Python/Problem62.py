import itertools
import time
from decimal import *

getcontext().prec = 15
getcontext().rounding = ROUND_UP

def cubic_permutations():
    for i in range(345,346):
        cubrtList = []
        cube = pow(i,3)

        digits = list(map(int, str(cube)))
        permutationList = list(itertools.permutations(digits,len(digits)))

        for item in permutationList:
            num = ''
            
            for digit in item:
                num = num + str(digit)

            cubrt = Decimal(int(num))**Decimal(1/3)

            if int(cubrt) == float(cubrt):
                if not cubrt in cubrtList:
                    cubrtList.append(cubrt)

        if len(cubrtList) == 3:
            return int(pow(min(cubrtList), 3))


"Alternative approach"
def cubic_permutations2():
    start = time.time()
    cubeList = []

    for i in range(1,10000):
        cube = pow(i,3)
        cubeList.append(cube)

    for x in cubeList:
        count = 0
        
        xdigits = list(map(int, str(x)))
        xdigits.sort()

        for y in cubeList:
            ydigits = list(map(int, str(y)))
            ydigits.sort()

            if ydigits == xdigits:
                count = count + 1

        if count == 5:
            elapse = time.time()
            print(elapse-start)
            return x

# The answer is 127035954683, or 5027**3


            
            
        
