# Recursive sum of digits


def sumofdigits(number, start, end):

    # base case - 0 or single digit
    if start > end:
        return 0

    if start == end:
        return int(number[end])

    # add first digit to sum of rest of the digits
    return int(number[start]) + sumofdigits(number, start + 1, end)


n = input()

print(sumofdigits(n, 0, len(n) - 1))
