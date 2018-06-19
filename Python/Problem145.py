import time

def reverse_digits(num):
    '''Reverses a number.'''
    
    string = str(num)
    reverse = string[::-1]
    return int(reverse)


def main(limit):
    start = time.time()
    count = 0
    

    for n in range(12, limit):
        if n % 2 == 0:      # only looking at odd numbers; compensated at end
            continue

        nList = list(str(n + reverse_digits(n)))

        for i in range(0,len(nList)):
            if i == (len(nList) - 1): # if i is at the last index of the list
                if int(nList[i]) % 2 == 1:
                    count += 1
                    
            elif int(nList[i]) % 2 == 1: # checking if each digit is odd
                continue
            
            else:       # if a digit is not odd, break
                break

    end = time.time()
    print(end-start)
    return 2*count

# Answer: 608720
