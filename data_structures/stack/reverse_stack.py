from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


auxStack = []


def reverseStack(inputStack, extraStack):

    global auxStack
    for _ in range(len(inputStack)):
        extraStack.append(inputStack.pop())

    for _ in range(len(extraStack)):
        auxStack.append(extraStack.pop())

    for _ in range(len(auxStack)):
        inputStack.append(auxStack.pop())


"""-------------- Utility Functions --------------"""


# Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack):
    return len(stack) == 0


# Taking input using fast I/o method
def takeInput():
    size = int(stdin.readline().strip())
    inputStack = list()

    if size == 0:
        return inputStack

    values = list(map(int, stdin.readline().strip().split(" ")))
    inputStack = values

    return inputStack


# Main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack):
    print(inputStack.pop(), end=" ")
