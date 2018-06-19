import time

def main():
    start = time.time()
    total = 0

    track = []
    trackProducts = []

    for a in range(1, 100):
        for b in range(1, 10000):
            if [b,a] in track:
                continue
            if hasCommonDigits(a,b) == True:
                continue

            c = a*b
            if c in trackProducts:
                continue
            
            if isNinePandigital(a,b,c) == True:
                track.append([a,b])
                trackProducts.append(c)
                print(a,b,c)
                total += c

    end = time.time()
    print(end-start)
    return total

    


def hasCommonDigits(a,b):
    strA = str(a)
    strB = str(b)

    for i in strA:
        for j in strB:
            if i == j:
                return True

    return False


def isNinePandigital(a,b,c):
    digits = list(str(a) + str(b) + str(c))
    digits.sort()

    if digits == ['1','2','3','4','5','6','7','8','9']:
        return True
    else:
        return False


# Answer: 45228
