def fibonacci_even(n):
    '''Finds the sum of even valued terms below n in the
    Fibonacci series.'''

    x = 1
    y = 2
    total = 2
    while True:
        z = x + y
        if z > n:
            break
        
        if z % 2 == 0:
            total = total + z
        
        x = y
        y = z
        
    print('The sum of the even terms in the Fibonacci series less than ' + str(n) + ' is ' + str(total))

# The answer is 4613732
