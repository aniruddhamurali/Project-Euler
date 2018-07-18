# Problem 96
# Answer: 24702

# Displays the grid
def print_grid(matrix):
    for row in matrix:
        print(row)


# Returns whether an entry is unassigned
# If there is an unassigned entry, set l to be equal to [row, column]
# l is used in solve() to test different cases
def has_empty_entry(matrix, l):
    for row in range(0,9):
        for col in range(0,9):
            if matrix[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False


# Returns whether n is used in a certain row (row)
def in_row(matrix, row, n):
    for col in range(0,9):
        if matrix[row][col] == n:
            return True
    return False


# Returns whether n is used in a certain column (col)
def in_col(matrix, col, n):
    for row in range(0,9):
        if matrix[row][col] == n:
            return True
    return False


# Returns whether n is used in a certain box (determined with row and col)
def in_box(matrix, row, col, n):
    # Iterate over each row in the box
    for i in range(0,3):
        # Iterate over each column in the box
        for j in range(0,3):
            if matrix[row+i][col+j] == n:
                return True
    return False


# Check is n can be assigned to matrix[row][col]
# Does checking with row, column, and box
def entry_assignable(matrix, row, col, n):
    if not in_row(matrix, row, n) and not in_col(matrix, col, n) and not in_box(matrix, row - row%3, col - col%3, n):
        return True
    return False


def solve(matrix):
    l = [0,0]

    # If all entries are filled, the grid has been solved
    if not has_empty_entry(matrix, l):
        return True

    # Test out any entries that have been unassigned
    row = l[0]
    col = l[1]

    for n in range(1,10):
        # If n seems to work, try it
        if entry_assignable(matrix, row, col, n):
            matrix[row][col] = n

            # Grid is solved - success!
            if solve(matrix) == True:
                return True

            # Failed, so reset the entry and try again
            matrix[row][col] = 0

    return False


# Driver main function
if __name__ == "__main__":
    total = 0 # sum of the 3-digit numbers found in the top left corner of each solution grid
    grids = []
    file = open('p096_sudoku.txt', 'r')
    grid = [] # temp variable to store grids from file
    lineCount = 0 # Used to differentiate lines
    for line in file:
        row = []
        line = line.strip()
        
        # If we come to a line saying "Grid [number]", continue
        if line.isnumeric() == False:
            lineCount += 1
            continue
        
        for n in line:
            row.append(int(n))
        grid.append(row)

        # If we are on the final row of a grid, add the grid to the grids variable
        if lineCount % 10 == 9:
            grids.append(grid)
            grid = []
        lineCount += 1

    for grid in grids:
        solve(grid)
        three_digit_num = str(grid[0][0]) + str(grid[0][1]) + str(grid[0][2])
        total += int(three_digit_num)

    print(total)







        
