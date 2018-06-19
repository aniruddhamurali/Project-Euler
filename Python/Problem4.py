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

def max_product(n):
    answer = 0
    for i in range(n//10,n):
        for count in range(n//10,n):
            if palindrome(i*count) == True and i*count > answer:
                answer = i*count
    print(answer)
            

    
    
     
