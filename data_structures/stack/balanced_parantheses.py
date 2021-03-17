from sys import stdin


def isBalanced(expression):
    # Your code goes here
    vc = ["(", "{", "["]
    s = []
    if len(expression) == 0:
        return True

    for char in expression:
        if char in vc:
            s.append(char)
        elif char == ")":
            if not s or s[-1] != "(":
                return False
            s.pop()
        elif char == "}":
            if not s or s[-1] != "{":
                return False
            s.pop()
        elif char == "]":
            if not s or s[-1] != "[":
                return False
            s.pop()

    if len(s) == 0:
        return True
    else:
        return False


# main
expression = stdin.readline().strip()

if isBalanced(expression):
    print("true")

else:
    print("false")
