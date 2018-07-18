def max_exp():
    name = "Problem99.txt"
    file = open(name, 'r')
    maxNum = None
    track = 1

    for line in file:
        comma = line.find(',')
        base = line[:comma]
        exp = line[comma+1:]
        base = float(base)
        exp = (int(exp))/700000
        num = float(base**exp)

        if maxNum == None or num > maxNum:
            maxNum = num
            maxLine = track
        track = track + 1

    return maxLine
        

        
        

    
