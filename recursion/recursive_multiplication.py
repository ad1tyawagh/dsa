# Recursive multiplication using + and - only.
import sys

sys.setrecursionlimit(1000000)


def recursive_multiply(a, b):
    # base case - no more m's or single m
    if a == 0 or b == 0:
        return 0
    if b == 1:
        return a

    # add m to m * n-1
    return a + recursive_multiply(a, b - 1)


m = int(input())
n = int(input())

print(recursive_multiply(m, n))
