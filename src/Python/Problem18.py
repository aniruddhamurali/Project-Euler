def main():
    triangle = []
    
    name = "Problem18.txt"
    file = open(name, 'r')

    for line in file:
        line = line.split(' ')
        for item in range(0,len(line)):
            line[item] = int(line[item])
        triangle.append(line)

    triangle.reverse()
    print(triangle)

    for i in range(0, len(triangle)):
        
        for j in range(0, len(triangle[i]) - 1):
            triangle[i+1][j] += max(triangle[i][j], triangle[i][j+1])

    return triangle[len(triangle)-1][0]
        
        
