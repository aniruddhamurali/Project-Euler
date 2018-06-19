def main():
    pentagonNumbers = set(n*(3*n-1)/2 for n in range(1,10000))
    '''pentagonNumbers.add(1)
    pentagonNumbers.add(5)
    pentagonNumbers.add(12)
    pentagonNumbers.add(22)
    pentagonNumbers.add(35)
    pentagonNumbers.add(51)
    pentagonNumbers.add(70)'''
    #n = 8

    for p1 in pentagonNumbers:
        for p2 in pentagonNumbers:
            if p1 == p2 or p1 > p2:
                '''pentagonNumbers.add(n*(3*n-1)/2)
                n += 1'''
                continue
            else:
                diff = abs(p2-p1)
                total = p1+p2

                if diff in pentagonNumbers and total in pentagonNumbers:
                    return p1, p2, diff
                '''else:
                    pentagonNumbers.add(n*(3*n-1)/2)
                    n += 1'''

# Answer: 5482660
