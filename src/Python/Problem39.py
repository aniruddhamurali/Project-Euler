
def checkPythag(a,b,c):
    if c**2 == a**2 + b**2:
        return True
    else:
        return False



def main(p):
    mydict = dict()   #mydict[perimeter] = number of triples
    counts = []
    perimeters = []

    for i in range(1,p+1):
        mydict[str(i)] = 0

    
    for c in range(1,p):
        for b in range(1,c):
            
            for a in range(1,c):
                perimeter = a+b+c
                
                if perimeter > p:
                    break
                
                elif checkPythag(a,b,c) == True:
                    mydict[str(a+b+c)] += 1


    for key in mydict.keys():
        perimeters.append(key)

    for item in mydict.values():
        counts.append(item)

    print(max(counts)/2)
    print(perimeters[counts.index(max(counts))])


# Answer: 840

                
                    
                    
