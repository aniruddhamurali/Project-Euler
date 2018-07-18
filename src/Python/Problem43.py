import itertools

def main():
    pandigitalDigits = [0,1,2,3,4,5,6,7,8,9]
    total = 0

    permutationList = list(itertools.permutations(pandigitalDigits,10))

    for tup in permutationList:
        digits = list(tup)

        if digits[0] == 0:
            continue

        '''for digit in digits:
            digit = str(digit)'''

        if int(''.join(map(str,digits[1:4]))) % 2 == 0:
            if int(''.join(map(str,digits[2:5]))) % 3 == 0:
                if int(''.join(map(str,digits[3:6]))) % 5 == 0:
                    if int(''.join(map(str,digits[4:7]))) % 7 == 0:
                        if int(''.join(map(str,digits[5:8]))) % 11 == 0:
                            if int(''.join(map(str,digits[6:9]))) % 13 == 0:
                                if int(''.join(map(str,digits[7:10]))) % 17 == 0:
                                    print(digits)
                                    total = total + int(''.join(map(str,digits)))

    return total

        
# The answer is 16695334890
        
        
        
