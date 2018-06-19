
def main():
    sumRMax = 0

    for a in range(3,1001):
        if a % 2 == 1:
            rmax = a*(a-1)
        elif a % 2 == 0:
            rmax = a*(a-2)
        sumRMax += rmax

    return sumRMax

# Answer: 33082500
