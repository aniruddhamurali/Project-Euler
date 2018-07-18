def nonMersenne_prime():

    x = 28433*(2**7830457) + 1
    xlist = list(str(x))
    xlist.reverse()
    digitsList = xlist[:10]
    digitsList.reverse()

    tendigits = ''

    for item in digitsList:
        tendigits = tendigits + str(item)

    return int(tendigits)
        
