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


def lychrel(limit):
    start = time.time()
    count = 0

    for n in range(1, limit):
        p1 = n
        
        for i in range(1,50):
            p2 = reverse_digits(p1)
            total = p1 + p2

            if palindrome(total) == True:
                p1 = total
                break

            p1 = total
            if (i == 49): count += 1

    end = time.time()
    print(end-start)
    return count
            
# Answer: 249
