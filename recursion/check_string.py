# Check AB
# Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that
# checks if the string was generated using the following rules: a. The string begins with an 'a' b. Each 'a' is
# followed by nothing or an 'a' or "bb" c. Each "bb" is followed by nothing or an 'a' If all the rules are followed
# by the given string, return true otherwise return false.

import sys

sys.setrecursionlimit(100000)


def check_string(string):
    # base case
    if len(string) == 0:
        return True

    # check whether the first char is a
    if string[0] == 'a':
        if len(string[1:]) == 0:
            return True
        elif string[1] == 'a':
            return check_string(string[1:])
        elif string[1] == 'b':
            if string[2] == 'b' and len(string[3:]) == 0:
                return True
            elif string[2] == 'b' and string[3] == 'a':
                return check_string(string[3:])

    return False


s = input()

if check_string(s):
    print('true')
else:
    print('false')
