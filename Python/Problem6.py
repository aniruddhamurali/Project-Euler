def sumSquareDiff(n):
    total = 0
    amount = 0
    for count in range(1,n+1):
        total = total + count**2
        amount = amount + count
    othertotal = amount**2
    
    if total > othertotal:
        answer = total - othertotal
        print(answer)
    else:
        answer = othertotal - total
        print(answer)
        
        
