# Recursively check whether a string is a palindrome or not.


def is_palindrome(s, start, end):

    # base case - empty/single character
    if start >= end:
        return True

    # if the first and last element are equal
    # check for the smaller string excluding them.
    if s[start] == s[end]:
        if is_palindrome(s, start + 1, end - 1):
            return True
    else:
        return False


string = input()

if is_palindrome(string, 0, len(string) - 1):
    print("true")
else:
    print("false")
