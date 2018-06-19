import time
import math


def main():
    target = 2000000
    limit = int(math.sqrt(target)) + 1
    rectList = ((w, h) for w in range(1, limit) for h in range(1, limit))
    func = lambda wh: abs(num_rectangles(wh[0], wh[1]) - target)
    ans = min(rectList, key=func)
    return ans[0] * ans[1]


def num_rectangles(m, n):
    return (m+1)*m*(n+1)*n//4


# Answer: 2772
