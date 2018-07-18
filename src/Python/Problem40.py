def champernownes_constant(n):
    string = ''
    for count in range(1,n+1):
        string = string + str(count)

    champernoweList = list(string)

    a = int(champernoweList[0])
    b = int(champernoweList[9])
    c = int(champernoweList[99])
    d = int(champernoweList[999])
    x = int(champernoweList[9999])
    y = int(champernoweList[99999])
    z = int(champernoweList[999999])

    answer = a * b * c * d * x * y * z
    return answer
        
