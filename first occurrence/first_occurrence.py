def first_occurrence(arr, element):
    # setting low and high
    low, high = 0, len(arr) - 1

    while low <= high:
        # find the middle of list
        mid = (low + high) // 2

        if low == high:
            # empty list
            break
        if arr[mid] < element:
            # guess number little than target(element)
            low = mid + 1
        else:
            # guess number bigger than target(element)
            high = mid

    if arr[low] == element:
        # found the first occurrence
        return low


# print(first_occurrence([2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 4))
def show(arr, key):
    return first_occurrence(arr, key)


print(show([2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 4))
