def prob14(num):
    numList = []
    lengthList = []
    item = 0
    for n in range(2,num):
        while n >= 2:
            if n % 2 == 0:
                numList.append(n)
                n = n//2
            else:
                numList.append(n)
                n = 3*n + 1
                
        if n == 1:
            numList.append(1)
            chain = len(numList)
            lengthList.append(chain)
            numList = []

    maxLength = max(lengthList)
    maxStarter = lengthList.index(maxLength) + 2
    return maxStarter
            
        
