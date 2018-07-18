import itertools
import time

def main():
    start = time.time()
    
    for count in itertools.count(1010000000, 10):
        square = pow(count, 2)
        digits = list(map(int, str(square)))

        if len(digits) < 19:
            continue

        if digits[0] == 1 and digits[2] == 2 and digits[4] == 3 and digits[6] == 4 and digits[8] == 5 and digits[10] == 6 and digits[12] == 7 and digits[14] == 8 and digits[16] == 9 and digits[18] == 0:
            elapse = time.time()
            print(elapse-start)
            return count

# The answer is 1389019170
