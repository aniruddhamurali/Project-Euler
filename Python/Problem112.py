import itertools
import time

def increasing_number(n):
    digits = list(map(int, str(n)))
    maxDigit = None

    for digit in digits:
        if maxDigit == None or digit >= maxDigit:
            maxDigit = digit
            continue
        else:
            return False

    return True


def decreasing_number(n):
    digits = list(map(int, str(n)))
    minDigit = None

    for digit in digits:
        if minDigit == None or digit <= minDigit:
            minDigit = digit
            continue
        else:
            return False

    return True


def main():
    start = time.time()
    count = 0

    for n in itertools.count(101):
        if increasing_number(n) == False and decreasing_number(n) == False:
            count = count + 1

        proportion = count/n

        if proportion == 0.99:
            elapse = time.time()
            print(elapse-start)
            return n

# The answer is 1587000
    
