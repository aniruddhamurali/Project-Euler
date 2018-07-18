def prob13():
    
    fileName = "Problem13.txt"
    file = open(fileName, 'r')
    total = 0

    for line in file:
        line = line.rstrip()
        num = int(line)
        total = total + num

    return total
        
