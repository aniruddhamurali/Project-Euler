import math

def prob9():
    for a in range(0, 500):
        for b in range(0,500):
            c = math.sqrt(a**2 + b**2)
            if (a+b+c) == 1000:
                product = a*b*c
                return product
                break
        
            
    
