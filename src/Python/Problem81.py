# Problem 81
# Answer: 427337

def main():
    name = "p081_matrix.txt"
    file = open(name, 'r')
    matrix = list()

    for line in file:
        line = line.split(',')
        line = [int(i) for i in line]
        matrix.append(line)
    
    for i in reversed(range(0,len(matrix))):
        for j in reversed(range(0,len(matrix[i]))):
            if i+1 < len(matrix) and j+1 < len(matrix[i]):
                temp = min(matrix[i+1][j], matrix[i][j+1])               
            elif i+1 < len(matrix):
                temp = matrix[i+1][j]
            elif j+1 < len(matrix[i]):
                temp = matrix[i][j+1]
            else:
                temp = 0
            matrix[i][j] += temp

    print(matrix[0][0])
    return matrix[0][0]


main()
