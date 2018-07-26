# Problem 64
# Answer: 1322

# Resources:
# http://web.math.princeton.edu/mathlab/jr02fall/Periodicity/mariusjp.pdf
# http://www2.math.ou.edu/~shankar/research/cfrac.pdf
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

import math

def period(S):
    m = [0]
    d = [1]
    a = [math.floor(math.sqrt(S))]
    index = 1

    while True:
        m.append(d[index-1]*a[index-1] - m[index-1])
        d.append((S - (m[index])**2)/d[index-1])
        a.append(math.floor((a[0] + m[index])/d[index]))

        # If we get a value of a that's twice a[0], we've completed a period.
        if a[len(a)-1] == 2*a[0]:
            break
        
        index += 1

    return index


def main():
    count = 0

    for N in range(2,10001):
        # period() does not work for square numbers
        if int(math.sqrt(N)) == float(math.sqrt(N)):
            continue
        
        p = period(N)
        if p % 2 == 1:
            count += 1

    return count


print(main())
