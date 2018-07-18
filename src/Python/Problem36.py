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


def binary_palindromes(n):
    total = 0
    
    for n in range(1,n):
        if palindrome(n) == True:
            binary_str = bin(n)
            binary_str = binary_str.lstrip('0b')
            binary_int = int(binary_str)

            if palindrome(binary_int) == True:
                total = total + n

    return total

# The answer is 872187               
