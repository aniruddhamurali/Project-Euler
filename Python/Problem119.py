import math

def digit_power_sum(n):
    a = 1
    nlist = []

    while True:
        for base in range(7,101):
            if base % 10 == 0:
                continue
            
            for exp in range(2,11):
                power = pow(base,exp)
                powerlist = list(map(int, str(power)))
                
                if sum(powerlist) == base:
                    nlist.append(power)

                    if a == n:
                        nlist.sort()
                        print(nlist)
                        print(a)
                        return nlist[a-1]
                    
                    else:
                        a = a + 1
            
            
            
            
            
        













    
