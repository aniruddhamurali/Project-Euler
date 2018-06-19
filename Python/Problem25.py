def fibonacci_digits(n):
    x = 1
    y = 1
    count = 2

    while True:
        z = x + y
        count = count + 1
        digitList = list(map(int, str(z)))
        if len(digitList) == n:
            print(count)
            break
        x = y
        y = z
            
            
        
