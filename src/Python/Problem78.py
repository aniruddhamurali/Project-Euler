# Problem 78
# Answer: 55374

partitions = [1]
n = 1
while True:
    i = 0
    pentagonal = 1
    partitions.append(0)

    while pentagonal <= n:
        # Every two terms in the p(n) expression are the same sign
        if i % 4 >= 2:
            sign = -1
        else:
            sign = 1
        partitions[n] += sign * partitions[n-pentagonal]
        partitions[n] %= 1000000
        i += 1

        # Calculate the next pentagonal number
        if i % 2 == 0:
            j = i//2 + 1
        else:
            j = -1*(i//2 + 1)
        pentagonal = int(j * (3*j - 1)/2)

    # The last element is the number of possible partitions
    if partitions[n] == 0:
        break
    n += 1

print(n)
