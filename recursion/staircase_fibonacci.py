# A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. Implement
# a method to count how many possible ways the child can run up to the stairs. You need to return number of possible
# ways W.

import sys

sys.setrecursionlimit(100000)


def ways(steps):
    # base cases
    wys = [-1 for _ in range(steps + 1)]
    wys[0] = 1
    wys[1] = 1
    wys[2] = 2

    for i in range(3, steps + 1):
        wys[i] = wys[i - 1] + wys[i - 2] + wys[i - 3]

    return wys[steps]


n = int(input())
print(ways(n))
