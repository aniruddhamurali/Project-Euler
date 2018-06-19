
def count_summations(n):
    ways = [1] + [0]*n
    
    for i in range(1,n):
        for j in range(i, n+1):
            ways[j] += ways[j-i]
    
    return ways[n]

# Answer: 190569291
