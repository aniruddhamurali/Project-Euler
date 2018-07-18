import math

def lattice_paths(n):
    "Returns the total number of possible paths in an n-by-n grid from one corner to the opposite corner."
    routes = (math.factorial(2*n)/pow(math.factorial(n),2))
    return int(routes)

    
