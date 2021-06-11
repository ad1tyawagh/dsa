# # Read input as specified in the question.
# # Print output as specified in the question.
# from itertools import combinations


def print_triplet(p, q, r):

    nums = [p, q, r]
    nums.sort()
    print(nums[0], nums[1], nums[2])


# def triplet_sum(a, x):

#     for p, q, r in combinations(a, 3):
#         if p + q + r == x:
#             print_triplet(p, q, r)


def triplet_sum(a, x):

    n = len(a)
    a.sort()
    for i in range(0, n - 2):
        l = i + 1
        r = n - 1
        while l < r:
            if a[i] + a[l] + a[r] == x:
                print_triplet(a[i], a[l], a[r])
            elif a[i] + a[l] + a[r] < x:
                l += 1
            else:
                r -= 1


# Main
n = int(input())
arr = list(int(i) for i in input().strip().split(" "))
total = int(input())
triplet_sum(arr, total)
