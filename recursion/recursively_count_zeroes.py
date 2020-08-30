# Count zeroes recursively
import sys

sys.setrecursionlimit(10000)


def count_zeroes(number):
    # convert the number to string
    temp = str(number)

    # base case - 0 digit or 1 digit
    if len(temp) == 0:
        return 0
    if len(temp) == 1:
        if temp == '0':
            return 1
        else:
            return 0

    # counting zeroes
    if temp[0] == '0':
        zeroes = 1 + count_zeroes(temp[1:])
    else:
        zeroes = count_zeroes(temp[1:])
    return zeroes


n = int(input())
print(count_zeroes(n))
