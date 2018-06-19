def prob8():
    fileName = input("Enter file name: ")
    file = open(fileName, 'r')
    file = str(file)
    product = 0

    while len(file) >= 13:
        fragment = 1
    for i in range(0,13):
        fragment = fragment * int(file[i])
    if fragment > product:
        product = fragment
    file = file[1:]
    return product
    
    
