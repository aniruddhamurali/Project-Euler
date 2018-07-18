def self_powers(n):
    power = 1
    total = 0
    tenDigits = []
    stringNum = ''
    
    for num in range(1,n+1):
        power = num**num
        total = total + power
        
    digitList = list(map(int, str(total)))
    length = len(digitList)
    
    for digits in range(0,10):
        tenDigits.append(digitList[length-digits-1])

    for item in range(0,10):
        stringNum = stringNum + str(tenDigits[item])
    
    reverse = stringNum[::-1]
    return reverse
        
        
    
