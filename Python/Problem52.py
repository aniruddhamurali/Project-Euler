def same_digits():
    count = 1
    while True:
        x = count
        y = 2 * count
        z = 3 * count
        a = 4 * count
        b = 5 * count
        c = 6 * count
        
        x = list(map(int, str(x)))
        y = list(map(int, str(y)))
        z = list(map(int, str(z)))
        a = list(map(int, str(a)))
        b = list(map(int, str(b)))
        c = list(map(int, str(c)))

        x.sort()
        y.sort()
        z.sort()
        a.sort()
        b.sort()
        c.sort()

        if x == y == z == a == b == c:
            return count
        else:
            count = count + 1
        
