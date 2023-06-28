def search_insert(arr, val):
    # setting initial values
    low = 0
    high = len(arr) - 1
    mid = high // 2

    while low <= high:
        if val > arr[mid]:
            # target is bigger than middle
            mid += 1
            # mid and low are increasing
            low = mid
        else:
            # target is lower than of middle
            mid -= 1
            # mid and high are decreasing
            high = mid
    return low


print(search_insert([1, 3, 5, 6], 7))
