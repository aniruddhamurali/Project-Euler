from fractions import Fraction
import time

def ordered_fractions(d):
    start = time.time()
    quotientDict = dict()
    quotients = []

    for denominator in range(2,d+1):
        for numerator in range(1,denominator):
            quotient = Fraction(numerator,denominator)

            if quotient >= 3/7:
                break
            
            if not quotient in quotients:
                quotients.append(quotient)
                quotientDict[str(quotient)] = quotient.numerator

    quotientlist = list(quotientDict.keys())
    quotientlist = sorted(quotientlist,key=Fraction,reverse=False)
    
    index = quotientlist.index('3/7')
    fraction = quotientlist[index-1]
    answer = quotientDict[str(fraction)]

    elapse = time.time()
    print(elapse-start)
    return answer
    
    
    
    

            
            
                
                
        
    
