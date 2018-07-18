def smallestMultiple(n):
    x = 1
    for i in range(2,n):
        y = x
        while y % i != 0:
            y += x
        x = y
    print(x)
