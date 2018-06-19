def prob16(a,b):
    c = a**b
    numList = list(map(int, str(c)))
    digitsSum = sum(numList)
    return digitsSum
    
