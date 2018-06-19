import itertools
import time

'''def main(n):
    count = 0

    for startNum in range(1, n):
        print(startNum)
        digits = list(map(int, str(startNum)))
        digitTotal = 0

        for i in itertools.count(1):
            #print(count)
            for digit in digits:
                digitSquare = pow(digit, 2)
                digitTotal = digitTotal + digitSquare

            if digitTotal == 89 or digitTotal == 85 or digitTotal == 145 or
            digitTotal == 42 or digitTotal == 20 or digitTotal == 4 or
            digitTotal == 16 or digitTotal == 37 or digitTotal == 58:
                count = count + 1
                break

            if digitTotal == 44 or digitTotal == 32 or digitTotal == 13 or
            digitTotal == 10 or digitTotal == 1:
                break

    return count'''



def main(n):
    start = time.time()
    count = 0

    for i in range(1,n):
        sds = squareDigitSum(i)
        #print(count)

        for j in itertools.count(1):
            sds = squareDigitSum(sds)
            if sds != 89 and sds != 1:
                #print(sds)
                continue
            elif sds == 1:
                #print(count)
                break
            else:
                count += 1
                break

    end = time.time()
    print(end-start)
    return count
                
    

           
def squareDigitSum(n):
    total = 0

    for digit in str(n):
        total += pow(int(digit),2)

    return total


# Answer:8581146
    
