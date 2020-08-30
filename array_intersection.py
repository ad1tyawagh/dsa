def intersection(arr1, arr2):
    # Please add your code here
    arr1.sort()
    arr2.sort()

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] == arr2[j]:
            print(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1


# Main
n1 = int(input())
arr1 = list(int(i) for i in input().strip().split(" "))
n2 = int(input())
arr2 = list(int(i) for i in input().strip().split(" "))
intersection(arr1, arr2)
