def fibonacci_pandigital(n):
    x = 1
    y = 2
    total = 2
    count = 4

    while True:
        z = x + y
        #if len(str(z)) >= 4000:
        if count >= n:
            #lastNine = z % 10**9
            #lastNine = list(str(lastNine))
            zList = list(str(z))
            firstNine = zList[:9]
            zList.reverse()
            lastNine = zList[:9]
            firstNine.sort()
            lastNine.sort()
            
            if firstNine == ['1','2','3','4','5','6','7','8','9'] and lastNine == ['1','2','3','4','5','6','7','8','9']:
                return count

        x = y
        y = z
        count = count + 1
            

    
