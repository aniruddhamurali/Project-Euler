def main():
    numList = []
    
    for count in range(2, 6 * pow(9,5)):
        total = 0
        digits = list(map(int, str(count)))
        
        for digit in digits:
            total = total + pow(digit, 5)

        if count == total:
            numList.append(count)

    return sum(numList)

# The answer is 443839
