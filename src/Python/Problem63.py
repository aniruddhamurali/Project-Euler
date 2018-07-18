def digit_power(n):
    answer = 0
    for count in range(1, n):
        stringNum = str(count)
        lengthNum = len(stringNum)
        for i in range(1,10):
            if i**lengthNum == count:
                answer = answer + 1
    return answer

# alternative sum(map(int, map(lambda a: 1.0/(1.0-log(a)/log(10)), range(1, 10))))
        
