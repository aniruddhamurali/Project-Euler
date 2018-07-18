def sum_multiples(n):
    '''Finds the sum of all the multiples of 3 or 5 below n.'''
    total = 0
    for count in range(1,n):
        if (count % 3 == 0) or (count % 5 == 0):
              total = total + count
    print('The sum of all multiples of 3 or 5 below ' + str(n) + ' is ' + str(total))
        
# The answer is 233168
