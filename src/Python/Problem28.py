def main(n):
    total = 1
    loopcount = 2

    for looplength in range(3,n+1,2):
        topright = pow(looplength,2)
        topleft = topright - (looplength - 1)
        bottomright = topright - 6 * (loopcount - 1)
        bottomleft = bottomright + (looplength - 1)

        total = total + topright + topleft + bottomright + bottomleft
        loopcount = loopcount + 1

    return total

# The answer is 669171001
