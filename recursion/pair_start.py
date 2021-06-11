# Pair star
# Given a string S, compute recursively a new string where identical chars
# that are adjacent in the original string are separated from each other by a "*".

import sys

sys.setrecursionlimit(100000)


def pair_star(string):
    # string to store return value

    # base case - 0 or 1 character
    if len(string) < 2:
        return string

    # check first element and second then check the rest of the string
    # starting from second element
    if string[0] == string[1]:
        temp = string[0] + "*" + pair_star(string[1:])
    else:
        temp = string[0] + pair_star(string[1:])

    return temp


s = input()
print(pair_star(s))
