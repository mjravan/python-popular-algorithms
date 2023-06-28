def binary_search(arr, target):
    # low & high keep  track of which part you search
    low = 0
    high = len(arr)-1

    while low <= high:
        # check the middle
        mid = (high + low) // 2
        guess = arr[mid]
        # found the item
        if guess == target:
            return mid
        # guess was too low
        elif guess < target:
            low = mid + 1
        # guess was too high
        else:
            high = mid - 1
    # the number doesn't exist
    return -1


print(binary_search([2, 3, 4, 6, 17, 19, 21], 4))
