# Problem 78
# Answer: 55374
# Link to refer to learn more about the partition algorithm:
# https://en.wikipedia.org/wiki/Partition_(number_theory)#Partition_function

'''
The number of partitions is given by the following:
p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + p(n-12) + p(n-15) - p(n-22) - ...
where p(0) = 1 and p(n) = 0 for n < 0.

The sequence to use is that of generalized pentagon numbers:
P(k) = k*(3k-1)/2, where k = 1, -1, 2, -2, 3, ...
'''

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
