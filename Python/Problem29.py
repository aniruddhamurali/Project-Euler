def distinct_powers(n):
    terms = []
    count = 0
    
    for a in range(2,n+1):
        for b in range(2,n+1):
            power = a**b
            
            if power in terms:
                continue
            
            else:
                terms.append(power)
                count = count + 1
                
    return count
