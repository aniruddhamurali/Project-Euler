import time

def main():
    start = time.time()
    triList = []
    letterDict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
    count = 0
    
    for n in range(1,25):
        triNumber = n * (n+1)//2
        triList.append(triNumber)

    file = open("p042_words.txt", 'r')

    for line in file:
        words = line.split(',')

    for word in words:
        letters = list(word)
        letters.pop(0)
        letters.pop(len(letters)-1)
        wordsum = 0
            
        for letter in letters:
            wordsum = wordsum + letterDict[letter]

        if wordsum in triList:
            count = count + 1

    elapse = time.time()
    print(elapse-start)
    return count

# The answer is 162
            
