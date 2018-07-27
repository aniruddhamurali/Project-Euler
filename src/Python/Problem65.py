# Problem 65
# Answer: 272

def main():
    n0 = 1
    n1 = 2
    for i in range(2, 101):
        # n[k] = a[k] * n[k-1] + n[k-2]
        n0, n1 = n1, n0 + n1 * (1 if i%3 else 2 *i//3)

    return sum(map(int,str(n1)))
