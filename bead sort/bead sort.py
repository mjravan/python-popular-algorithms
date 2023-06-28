def bead_sort(arr):
    # checking input for receiving a valid list
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise TypeError('sequence must be list of non-negative integer')
    # sorting list
    for _ in range(len(arr)):
        for i, (rod_upper, rod_lower) in enumerate(zip(arr, arr[1:])):
            if rod_upper > rod_lower:
                # replacing two number and sorting
                arr[i] -= rod_upper - rod_lower
                arr[i + 1] += rod_upper - rod_lower
    return arr


print(bead_sort([3, 5, 2, 6, 1]))
