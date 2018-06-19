import math

def main():
    count = 0
    
    name = "p102_triangles.txt" # file containing all triangles
    file = open(name,'r')

    for line in file:
        coords = line.split(',')  # makes a list of coordinates for each triangle
        
        # set coordinates as variables
        x1 = int(coords[0])
        y1 = int(coords[1])
        x2 = int(coords[2])
        y2 = int(coords[3])
        x3 = int(coords[4])
        y3 = int(coords[5])

        # calculate areas of the 4 triangles
        area = triangleArea(x1,y1,x2,y2,x3,y3)
        area1 = triangleArea(x1,y1,x2,y2,0,0)
        area2 = triangleArea(x1,y1,x3,y3,0,0)
        area3 = triangleArea(x2,y2,x3,y3,0,0)

        # compare areas
        if area == area1+area2+area3:
            count += 1

    return count



def triangleArea(x1,y1,x2,y2,x3,y3):
    '''Calculates the area of a triangle'''

    area = abs((x1-x3)*(y2-y1) - (x1-x2)*(y3-y1))/2
    return area


# Answer is 228
