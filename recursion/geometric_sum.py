# Geometric sum using recursion
# first term = 1
# ratio = 1/2
# # of terms = k (variable)


def gp_sum(n):

    # base case
    if n == 0:
        return 1

    # sum of n terms
    gpsum = (1 / 2) ** n + gp_sum(n - 1)

    # return the sum
    return gpsum


k = int(input())
print("%.5f" % gp_sum(k))
