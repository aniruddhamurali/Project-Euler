def main():
    maxdigitSum = None

    for a in range(1, 100):
        for b in range(1, 100):
            num = pow(a,b)
            digits = list(map(int, str(num)))
            digitSum = sum(digits)

            if maxdigitSum == None or digitSum > maxdigitSum:
                maxdigitSum = digitSum

    return maxdigitSum

# The answer is 972
