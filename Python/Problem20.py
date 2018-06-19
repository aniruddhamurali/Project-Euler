def prob20(n):
    factorialNum = 1

    for i in range(1,n+1):
        factorialNum = factorialNum * i

    numList = list(map(int, str(factorialNum)))
    digitSum = sum(numList)
    return digitSum
