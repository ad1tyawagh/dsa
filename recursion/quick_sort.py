import sys

sys.setrecursionlimit(1000000)


def partition(arr, start, end):
    pivot = arr[start]
    element_count = 0

    # check number of elements smaller than pivot element
    for i in range(len(arr)):
        if pivot > arr[i]:
            element_count += 1

    # swap pivot with it's correct position
    arr[start], arr[start + element_count] = arr[start + element_count], arr[start]

    # put smaller elements on the left, larger elements on thr right of the pivot
    i = start
    j = end

    while i != pivot or j != pivot:

        if arr[i] > pivot:
            # arr[i] > pivot and arr[j] < pivot
            if arr[j] < pivot:
                # swap them
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            # arr[i] > pivot and arr[j] > pivot, decrease j.
            else:
                j -= 1
        else:
            # arr[i] < pivot and arr[j] > pivot, check the next elements by increasing both i and j.
            if arr[j] > pivot:
                i += 1
                j -= 1
            # if arr[i] < pivot and arr[j] < pivot, increase
            else:
                i += 1

    # return the pivot value of the partitioned array
    return element_count


def quicksort(arr, start, end):
    # Please add your code here

    # base case
    if start >= end:
        return arr

    # partitioning
    pivot_index = partition(arr, start, end)

    # sorting the parts
    quicksort(arr, start, pivot_index - 1)
    quicksort(arr, pivot_index + 1, end)
