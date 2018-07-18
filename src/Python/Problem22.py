def main():
    file = open("p022_names.txt", 'r')
    letterDict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}

    total = 0
    
    for line in file:
        names = line.split(',')

    names.sort()

    for name in names:
        letters = list(name)
        letters.pop(0)
        letters.pop(len(letters)-1)
        score = 0

        for letter in letters:
            score = score + letterDict[letter]

        score = score * (names.index(name) + 1)
        total = total + score

    return total

# The answer is 871198282
    

    
