import itertools

def lexicographic_permutations():
    start = time.time()
    digits = [0,1,2,3,4,5,6,7,8,9]
    answer = ''

    permutationList = list(itertools.permutations(digits,len(digits)))

    for digit in permutationList[999999]:
        answer = answer + str(digit)
        
    return int(answer)

# The answer is 2783915460
