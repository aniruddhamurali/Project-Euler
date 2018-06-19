import math
import itertools
import time


def reverse_digits(num):
    '''Reverses a number.'''
    
    string = str(num)
    reverse = string[::-1]
    return int(reverse)


def palindrome(num):
    '''prints True or False according to whether or not
    num is a palindrome.'''
    
    if num == reverse_digits(num):
        return True
    else:
        return False



def main(limit):
    start = time.time()
    palindromicSums = set()

    for i in range(1, int(math.sqrt(limit)) + 1):
        total = 0
        
        for length in itertools.count(2):
            total += (i+length-2)**2

            if total > limit:
                break
            elif length == 2:
                continue
            elif total in palindromicSums:
                continue
            elif palindrome(total) == False:
                continue
            elif palindrome(total) == True:
                palindromicSums.add(total)

    end = time.time()
    print(end-start)
    return sum(palindromicSums)

# Answer: 2906969179
