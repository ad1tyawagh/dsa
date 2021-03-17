def move_discs(n, source, destination, auxiliary):
    # base case
    if n == 0:
        return

    if n == 1:
        print(source, destination)
        return

    # move top n-1 discs from source to auxiliary
    move_discs(n - 1, source, auxiliary, destination)

    # move the nth disc from source to destination
    print(source, destination)

    # move the top n-1 discs from auxiliary to destination
    move_discs(n - 1, auxiliary, destination, source)


n_disks = int(input())
move_discs(n_disks, "a", "c", "b")
