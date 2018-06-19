
def main():
    count = 0
    p = 1
    q = 1

    for i in range(1,1001):
        numerator = p + 2*q
        denominator = p + q

        if len(str(numerator)) > len(str(denominator)):
            count += 1

        p = numerator
        q = denominator

    return count

# Answer: 153
