
# Problem 94
# Answer: 518408346
# Time: .09s

import time
start = time.time()

# Use's Pell's Equation to make solution very quick
def main():
    x = 2
    y = 1
    limit = 1000000000
    result = 0
     
    while True:
        #b = a+1
        aTimes3 = 2*x - 1
        areaTimes3 = y*(x - 2)
        if (aTimes3 > limit):
            break
     
        if (aTimes3 > 0 and areaTimes3 > 0 and aTimes3 % 3 == 0 and areaTimes3 % 3 == 0):
            a = aTimes3/3
            area = areaTimes3/3
            result += 3*a + 1
     
        #b = a-1
        aTimes3 = 2*x + 1
        areaTimes3 = y*(x + 2)
     
        if (aTimes3 > 0 and areaTimes3 > 0 and aTimes3 % 3 == 0 and areaTimes3 % 3 == 0):
            a = aTimes3 /3
            area = areaTimes3/3
            result += 3*a - 1
     
        nextX = 2*x + y*3
        nextY = y*2 + x
     
        x = nextX
        y = nextY

    return result

print(main())
elapse = time.time()
print(elapse-start)
    
