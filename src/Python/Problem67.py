def main():
    triangle = []
    
    name = "p067_triangle.txt"
    file = open(name, 'r')

    for line in file:
        line = line.split(' ')

        # convert each item in the line into an integer
        for item in range(0,len(line)):
            line[item] = int(line[item])

        # append all lines in the file into the list triangle
        triangle.append(line) 

    # reverse the list triangle to start from the bottom of the triangle
    triangle.reverse()

    for i in range(0, len(triangle)):

        '''for each item in the above row, add the max of row[j] and row[j+1]
        to it. The max path sum will be the last item in triangle.reverse()'''
        for j in range(0, len(triangle[i]) - 1):
            triangle[i+1][j] += max(triangle[i][j], triangle[i][j+1])

    return triangle[len(triangle)-1][0]

# The answer is 7273
        
